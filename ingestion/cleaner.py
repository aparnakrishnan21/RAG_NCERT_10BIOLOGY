
# import re


# class TextCleaner:
#     """
#     Cleans extracted text before chunking.
#     """

#     def clean(self, text: str) -> str:
#         # Convert Windows line endings
#         text = text.replace("\r\n", "\n")

#         # Remove leading/trailing spaces from every line
#         lines = [line.strip() for line in text.split("\n")]

#         # Remove empty lines
#         lines = [line for line in lines if line]

#         # Join lines back
#         text = "\n".join(lines)

#         # Replace multiple spaces with a single space
#         text = re.sub(r"[ \t]+", " ", text)

#         # Collapse multiple blank lines into one
#         text = re.sub(r"\n{2,}", "\n", text)

#         return text.strip()
import re


class TextCleaner:
    """
    Cleans extracted PDF text for RAG ingestion.
    """

    def clean(self, text: str) -> str:

        # -------------------------
        # 1. Normalize line endings
        # -------------------------
        text = text.replace("\r\n", "\n")

        # -------------------------
        # 2. Remove leading/trailing spaces
        # -------------------------
        lines = [line.strip() for line in text.split("\n")]

        # -------------------------
        # 3. Remove empty lines
        # -------------------------
        lines = [line for line in lines if line]

        # -------------------------
        # 4. Remove page headers
        # -------------------------
        cleaned = []

        for line in lines:

            # Science
            if line.lower() == "science":
                continue

            # page number
            if re.fullmatch(r"\d{1,3}", line):
                continue

            # Reprint
            if "Reprint" in line:
                continue

            cleaned.append(line)

        lines = cleaned

        # -------------------------
        # 5. Merge chapter titles
        # -------------------------

        merged = []

        i = 0

        while i < len(lines):

            line = lines[i]

            # CHAPTER + title
            if (
                line.startswith("CHAPTER")
                and i + 2 < len(lines)
            ):
                merged.append(line)

                title = lines[i + 1]

                j = i + 2

                while (
                    j < len(lines)
                    and len(lines[j]) < 40
                    and not lines[j].endswith(".")
                    and not lines[j].startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9."))
                ):
                    title += " " + lines[j]
                    j += 1

                merged.append(title)

                i = j
                continue

            merged.append(line)
            i += 1

        lines = merged

        # -------------------------
        # 6. Join wrapped paragraphs
        # -------------------------

        paragraphs = []

        i = 0

        while i < len(lines):

    # Preserve chapter heading and title
            if lines[i].startswith("CHAPTER"):

                paragraphs.append(lines[i])

                if i + 1 < len(lines):
                    paragraphs.append(lines[i + 1])
                    i += 2
                else:
                    i += 1

                continue

    # Preserve section headings
            if re.match(r"^\d+\.\d+", lines[i]):
                paragraphs.append(lines[i])
                i += 1
                continue

    # Join normal paragraph
            paragraph = lines[i]
            i += 1

            while (
                i < len(lines)
                and not lines[i].startswith("CHAPTER")
                and not re.match(r"^\d+\.\d+", lines[i])
            ):
                paragraph += " " + lines[i]
                i += 1

            paragraphs.append(paragraph)

        text = "\n\n".join(paragraphs)
        # -------------------------
        # 7. Normalize spaces
        # -------------------------
        text = re.sub(r"[ \t]+", " ", text)

        # Collapse 3+ blank lines into 2
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()