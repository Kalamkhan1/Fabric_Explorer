import chromadb
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain.embeddings.base import Embeddings
from typing import List
from config import documents

class GeminiEmbeddingFunction(Embeddings):
    def __init__(self, document_mode=True):
        self.document_mode = document_mode
        # Initialize the Google GenAI Embeddings client
        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004"  # Specify the embedding model
        )

    def embed_documents(self, documents: List[str]) -> List[List[float]]:
        """Embed a list of documents."""
        embedding_task = "retrieval_document" if self.document_mode else "retrieval_query"
        # Use the `embed_documents` method from GoogleGenAIEmbeddings
        return self.embedding_model.embed_documents(documents)

    def embed_query(self, query: str) -> List[float]:
        """Embed a single query."""
        # Use the `embed_query` method for query-specific embeddings
        return self.embedding_model.embed_query(query)

    def __call__(self, input: List[str]) -> List[List[float]]:
        """Generate embeddings for the given input."""
        if self.document_mode:
            return self.embed_documents(input)
        else:
            return [self.embed_query(q) for q in input]


DB_NAME = "Fabrics"
embed_fn = GeminiEmbeddingFunction()
embed_fn.document_mode = True
chroma_client = chromadb.HttpClient(host='localhost', port=8000, tenant='default_tenant')
db = chroma_client.get_or_create_collection(name=DB_NAME, embedding_function=embed_fn)


# Get the current number of documents in the collection
current_document_count = len(db.get()["documents"])

# Check if there are less than 7 documents
if current_document_count < 7:
    # Calculate how many documents need to be added
    documents_to_add = documents[:7 - current_document_count]  # Add only the missing documents
    ids_to_add = [str(i) for i in range(current_document_count, current_document_count + len(documents_to_add))]
    
    # Generate embeddings for the documents to be added
    embeddings_to_add = embed_fn.embed_documents(documents_to_add)

    # Add the documents and their embeddings to the database
    db.add(documents=documents_to_add, embeddings=embeddings_to_add, ids=ids_to_add)
    print(f"Added {len(documents_to_add)} documents to the collection.")
else:
    print(f"The collection already contains {current_document_count} documents.")
