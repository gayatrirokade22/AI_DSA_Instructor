from pypdf import PdfReader

pdf = PdfReader("data/dsa_notes.pdf")

print("Number of pages:", len(pdf.pages))

for page in pdf.pages:
    text = page.extract_text()
    print(text[:500])