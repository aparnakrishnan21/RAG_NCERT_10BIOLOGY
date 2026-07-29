# from pathlib import Path

# from ingestion.loader import DocumentLoader
# from ingestion.cleaner import TextCleaner
# from ingestion.metadata_builder import MetadataBuilder
# from chunking.chunker import DocumentChunker

# loader = DocumentLoader()
# cleaner = TextCleaner()
# metadata_builder = MetadataBuilder()
# chunker = DocumentChunker()

# pdf_files = sorted(Path("docs").glob("*.pdf"))

# print(f"Found {len(pdf_files)} PDF(s)\n")

# for pdf_path in pdf_files:

#     print("=" * 60)
#     print(f"Processing: {pdf_path.name}")

#     text = loader.load_document(str(pdf_path))

#     clean_text = cleaner.clean(text)

#     metadata = metadata_builder.build_metadata(
#         clean_text,
#         str(pdf_path)
#     )

#     chunks = chunker.chunk_document(clean_text)

#     print(f"Chapter Number : {metadata['chapter_number']}")
#     print(f"Chapter Title  : {metadata['chapter_title']}")
#     print(f"Total Chunks   : {len(chunks)}")

#     if chunks:
#         print("\nFirst Chunk:\n")
#         print(chunks[0][:500])
#         print("\n2nd Chunk:\n")
#         print(chunks[1][:500])
#         print("\n3rd Chunk:\n")
#         print(chunks[2][:500])  


#             # Print first 300 characters only

#     print("\n")


from pathlib import Path

from ingestion.loader import DocumentLoader
from ingestion.cleaner import TextCleaner
from ingestion.metadata_builder import MetadataBuilder
from chunking.chunker import DocumentChunker
from chunking.chunk_saver import ChunkSaver

loader = DocumentLoader()
cleaner = TextCleaner()
metadata_builder = MetadataBuilder()
chunker = DocumentChunker()
chunk_saver = ChunkSaver()

pdf_files = sorted(Path("docs").glob("*.pdf"))

print(f"Found {len(pdf_files)} PDF(s)\n")

for pdf_path in pdf_files:

    print("=" * 60)
    print(f"Processing: {pdf_path.name}")

    text = loader.load_document(str(pdf_path))

    clean_text = cleaner.clean(text)

    metadata = metadata_builder.build_metadata(
        clean_text,
        str(pdf_path)
    )

    chunks = chunker.chunk_document(clean_text)

    output_file = f"data/chunks/{pdf_path.stem}_chunks.json"

    chunk_saver.save_chunks(
        chunks,
        metadata,
        output_file
    )

    print(f"Chapter Number : {metadata['chapter_number']}")
    print(f"Chapter Title  : {metadata['chapter_title']}")
    print(f"Total Chunks   : {len(chunks)}")
    print()