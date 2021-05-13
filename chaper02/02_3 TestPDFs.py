import pdf
pdfFile = 'sample-one-line.pdf'
pdfFileEncrypted = 'sample-one-line.protected.pdf'
print('PDF1: \n', pdf.getTextPDF(pdfFile))
print('PDF2: \n', pdf.getTextPDF(pdfFileEncrypted,'tuffy'))