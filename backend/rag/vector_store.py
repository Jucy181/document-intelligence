import chromadb
def simple_embedding(text):
    vec = [ord(c) for c in text][:50]
    while len(vec) < 50:
        vec.append(0)
    return vec


client = chromadb.Client()
collection = client.get_or_create_collection(name="books")


def add_books(book_id, text):
    embedding = simple_embedding(text)

    collection.upsert(
        ids=[str(book_id)],
        embeddings=[embedding],
        documents=[text]
    )


def search_books(query):
    query_embedding = simple_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    return results
