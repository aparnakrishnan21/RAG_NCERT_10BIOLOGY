from ingestion.loader import DocumentLoader

loader = DocumentLoader()

documents = loader.load_folder("docs")

print(f"\nTotal documents loaded: {len(documents)}")

for doc in documents:
    print("=" * 60)
    print("File:", doc["filename"])
    print(doc["text"][:300])   # First 300 characters

