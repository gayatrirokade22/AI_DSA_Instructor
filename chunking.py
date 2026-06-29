from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step 1: Load the PDF
loader = PyPDFLoader("data/dsa_notes.pdf")
documents = loader.load()

print("Number of pages:", len(documents))

# Step 2: Create the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

# Step 3: Split the document into chunks
chunks = text_splitter.split_documents(documents)

print("Number of chunks:", len(chunks))

# Step 4: Print the first chunk
print("\nFirst Chunk:\n")
print(chunks[0].page_content)