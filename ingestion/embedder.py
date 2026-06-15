import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient("data/chromadb")

ollama_ef = embedding_functions.OllamaEmbeddingFunction(
    url='http://localhost:11434/api/embeddings', 
    model_name= 'nomic-embed-text')

collection = client.get_or_create_collection(name = "documents", embedding_function=ollama_ef)

def embed_document(document_id, chunks,target_collection= collection):
    batch_documents= []
    batch_ids= []
    batch_metadata= []

    for idx, chunk in enumerate(chunks):
        clean_chunk = chunk.replace('\n', " ").strip()
        chunk_id = f"{document_id}_{idx}"
        chunk_metadata = {"source_file": document_id, "chunk_index": idx}

        batch_documents.append(clean_chunk)
        batch_ids.append(chunk_id)
        batch_metadata.append(chunk_metadata)
    
    if batch_ids:
        target_collection.upsert(ids=batch_ids, documents=batch_documents, metadatas=batch_metadata)
        print(f"Successfully batch-indexed {len(batch_ids)} chunks for document: {document_id}")


if __name__ == '__main__':
    # Simulating a verification test-drive
    sample_document_name = "charon_dossier.txt"
    sample_chunks = [
        "Chunk block number 1 detail about the Continental concierge.",
        "Chunk block number 2 detailing tactical shotgun operations during the hotel defense.",
        "Chunk block number 3 tracking retribution targets across high table zones."
    ]
    embed_document(collection, sample_document_name, sample_chunks)