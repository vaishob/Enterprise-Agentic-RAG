import logfire
from pypdf import PdfReader


def parse_pdf(file_path: str) -> str:
    """
    Extract text from a PDF locally using pypdf.
    Falls back to pdfplumber for pages that yield no text (e.g., image-heavy pages).

    Args:
        file_path (str): The path to the PDF file.
    """
    with logfire.span("📄 PDF Parsing (local)", filename=file_path):
        try:
            reader = PdfReader(file_path)
            total_pages = len(reader.pages)
            logfire.info(f"PDF has {total_pages} pages.")

            text_parts: list[str] = []
            blank_pages: list[int] = []

            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                if text.strip():
                    text_parts.append(text)
                else:
                    blank_pages.append(i + 1)

            # Fallback to pdfplumber for blank pages
            if blank_pages:
                logfire.info(
                    f"pypdf return blank on pages {blank_pages} - retrying with pdfplumber.")
                try:
                    import pdfplumber
                    with pdfplumber.open(file_path) as pdf:
                        for page_num in blank_pages:
                            # pdfplumber uses 0-based indexing
                            page = pdf.pages[page_num - 1]
                            fallback_text = page.extract_text() or ""
                            if fallback_text.strip():
                                text_parts.append(fallback_text)
                except Exception as plumber_err:
                    logfire.warning(
                        f"❌ pdfplumber fallback failed: {plumber_err}")

            full_text = "\n".join(text_parts)

            if not full_text.strip():
                logfire.warning(
                    f"❌ PDF Parse Failed - No text extracted from {file_path}.")
            else:
                logfire.info(
                    f"✅ PDF Parse Successful - Extracted text from {file_path}.")

            return full_text

        except Exception as e:
            logfire.error(f"❌ PDF Parse Failed for {file_path}: {e}")
            raise e
