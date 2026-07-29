import re
from pathlib import Path


class MetadataBuilder:

    def build_metadata(self, text, source_file):

        metadata = {
            "source": Path(source_file).name,
            "chapter_number": None,
            "chapter_title": ""
        }

        lines = [line.strip() for line in text.splitlines() if line.strip()]

        # Document title
        # for line in lines[:20]:
        #     if 2 < len(line) < 50:
        #         metadata["title"] = line
        #         break

        # Chapter and chapter title
        for i, line in enumerate(lines):

            match = re.match(r"CHAPTER\s+(\d+)", line, re.IGNORECASE)

            if match:
                metadata["chapter_number"] = int(match.group(1))

                if i + 1 < len(lines):
                    metadata["chapter_title"] = lines[i + 1]

                break

        return metadata