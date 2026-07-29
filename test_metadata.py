from pathlib import Path
from ingestion.loader import DocumentLoader
from ingestion.cleaner import TextCleaner
from ingestion.metadata_builder import MetadataBuilder

loader = DocumentLoader()
cleaner = TextCleaner()
builder = MetadataBuilder()

for pdf in Path("docs").glob("*.pdf"):
    text = loader.load_document(str(pdf))
    cleaned = cleaner.clean(text)
    metadata = builder.build_metadata(cleaned, str(pdf))

    print(metadata)