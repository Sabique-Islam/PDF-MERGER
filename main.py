import PyPDF2 as pdf
pdfFiles = ["P1.pdf", "P2.pdf"]
merger = pdf.PdfMerger()
for i in pdfFiles:
    pdfFile = open(i, 'rb')
    pdfReader = pdf.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("MERGED.pdf")