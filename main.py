import PyPDF2 as pdf
pdfFiles = ["name of pdf 1.pdf", "name of pdf 2.pdf"] # Add all the PDFs you want to merge
merger = pdf.PdfMerger()
for i in pdfFiles:
    pdfFile = open(i, 'rb')
    pdfReader = pdf.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("MERGED PDF.pdf")
