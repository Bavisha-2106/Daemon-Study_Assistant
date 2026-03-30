import chromadb
import PyPDF2

def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    return text

def read_multiple_pdfs(file_paths):
    text = ""
    for path in file_paths:
        text += read_pdf(path)
    return text

def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    for i in range (0, len(words), chunk_size):
        chunk = " ". join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def store_chunks(chunks):
    client = chromadb.Client()
    collection = client.create_collection("os_notes")
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            ids=[f"chunk_{i}"]
        )
    return collection

def retrieve(collection, query, n_results=2):
    results = collection.query(
        query_texts = query,
        n_results = n_results
    )
    return results['documents'][0]