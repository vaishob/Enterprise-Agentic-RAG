import logfire


def parse_text(file_path: str):
    """
    Parses plain text files.

    Args:
        file_path (str): The path to the text file.
    """
    with logfire.span("📄 Text Parsing", filename=file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception as e:
            logfire.error(f"❌ Text Parse Failed - {file_path}: {e}")
            raise e
