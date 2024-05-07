from PyPDF2 import PdfFileMerger
import os

# print(os.listdir("day_8/pdfs"))
merger = PdfFileMerger()
files = [file for file in os.listdir("day_8/pdfs") if(file.endswith(".pdf"))]
# print(files)
for pdf in files:
    print(pdf)
    merger.append(f"day_8/pdfs/{pdf}")

merger.write(f"day_8/pdfs/merged-pdf.pdf")
merger.close()