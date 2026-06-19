import ollama
from pydantic import BaseModel, Field
import chromadb
from ingestion.embedder import collection
from ingestion.store import save_entites, save_relationships

class ER_entity(BaseModel):
  name: str = Field(description="Name of the entity")
  role: str = Field(description="What is the entity? is it a person, organization, something else")

class ER_relation(BaseModel):
  origin: str = Field(description="From who/what exact entity is the relation originating")
  destination: str = Field(description="To what/who exact entity is the origin related")
  label: str = Field(description="Why/what is the relation between the origin and destination")

class EntityRelationship(BaseModel):
  entities: list[ER_entity] = Field(description="all the major entities of the data")
  relationships: list[ER_relation] = Field(description="The major direct relations between the entities")
  

def entity_json(text, ReturnAsPythonClass= True):
  response = ollama.generate(
    model='llama3.1',
    prompt=f""" 
            Extract all major Entities such as people, organizations etc, 
            and what their relation is to each other,
            where all origin and destination names must be an exact entity name,
            from this text: {text} 
            """,
    format=EntityRelationship.model_json_schema(),
    options={'temperature': 0},
    stream=False
  )
  if ReturnAsPythonClass:
    return EntityRelationship.model_validate_json(response['response'])
  else:
    return response['response']

def extract_from_document(document_id):
  document_chunks=  (collection.get(where= {"document_id": str(document_id)}))
  chunk_ids= document_chunks['ids']
  chunk_texts = document_chunks["documents"]

  for id, chunk in zip(chunk_ids, chunk_texts):
    try:
      chunk_ER = entity_json(text=chunk, ReturnAsPythonClass=True)
    except Exception as e:
      print(f"Chunk Number{id} failed, continuing to next chunk \n Error: \n {e}")
      continue

    
    for entity in chunk_ER.entities:
      save_entites(
        document_id= document_id,
        name= entity.name, 
        role= entity.role
        )
    for relationship in chunk_ER.relationships:
      save_relationships(
        document_id=document_id,
        origin=relationship.origin,
        destination=relationship.destination,
        label=relationship.label
        )
    
    




if __name__ == "__main__":
  print(entity_json(""" So, I was looking over the file for Clara Vance—she's 42 this year,
                     born in '84 if my math holds up. Her supervisor, 
                    Marcus, mentioned she’s been absolutely crushing it at her current gig as a Lead Data Architect over at FinTech Corp,
                     where she's already clocked in 4 years.
                     Before that, she spent 3 years grinding as a Senior Analyst at DataGlobe Inc. Skill-wise,
                     she’s a powerhouse; she practically lives in SQL and Python, and lately, 
                    she’s been doing a ton of cloud orchestration with AWS. Write a quick snippet summarizing her profile. """
                    # , ReturnAsPythonClass=False
                    ))