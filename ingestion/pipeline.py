from reader import AutoFileReader
from store import save_document
from chunker import chunk_text
from embedder import embed_document

def ingest(filepath):
    filename, content = AutoFileReader(filepath)
    doc_id = save_document(filename, content)
    chunked_text = chunk_text(content)
    embed_document(document_id=doc_id, chunks=chunked_text)


if __name__ == "__main__":
    ingest(filepath="/home/piyushbanarjee/Projects/OSINT-Graph-Intelligence-Engine/Sample input/johnwick_charon.txt")