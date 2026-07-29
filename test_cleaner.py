from ingestion.loader import DocumentLoader
from ingestion.cleaner import TextCleaner

loader = DocumentLoader()
cleaner = TextCleaner()

documents = loader.load_folder("docs")

print(f"\nTotal documents loaded: {len(documents)}")

for doc in documents:
    print("=" * 60)
    print("File:", doc["filename"])

    cleaned_text = cleaner.clean(doc["text"])

    print(cleaned_text[:500])