from pathlib import Path
from pypdf import PdfReader
import fitz 

class DocumentLoader:
    """
    Loads different document types and returns text.
    """
    def load_pdf(self, filepath):
        doc = fitz.open(filepath)

        text = ""

        for page in doc:
            text += page.get_text(sort=True)

        doc.close()

        return text
    

    def load_txt(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    def load_md(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    def load_document(self, filepath):
        filepath = Path(filepath)

        suffix = filepath.suffix.lower()

        if suffix == ".pdf":
            return self.load_pdf(filepath)

        elif suffix == ".txt":
            return self.load_txt(filepath)

        elif suffix == ".md":
            return self.load_md(filepath)

        else:
            raise ValueError(f"Unsupported file type: {suffix}")\
            
    def load_folder(self, folder_path):
        folder = Path(folder_path)

        documents = []

        for file in folder.iterdir():
            if file.suffix.lower() in [".pdf", ".txt", ".md"]:
                try:
                    text = self.load_document(file)
                    documents.append({
                        "filename": file.name,
                        "filepath": str(file),
                        "text": text
                    })
                    print(f"Loaded: {file.name}")
                except Exception as e:
                    print(f"Skipped {file.name}: {e}")

        return documents