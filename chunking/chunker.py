from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunker:
    def __init__(
        self,
        chunk_size=500,
        chunk_overlap=100,
        separators=None,
    ):
        if separators is None:
            separators = [
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=separators
        )

    def chunk_document(self, text):
        return self.splitter.split_text(text)