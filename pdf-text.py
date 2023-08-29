import PyPDF2

#Enter PDF location
pdf_name = input('Enter Name of the PDF File..... ')
pdf_location = input('Enter File Path of PDF File.... ')

#Read and Open both PDF and text file
#If text file does not exist, a new one will be made. If exists, it will be overwritten.
with open(pdf_location, 'rb') as pdf_file, open(pdf_name, 'x') as text_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)
    
    #Extract text in loop and then write into text file.
    for i in range(len(read_pdf.pages)):
        page = read_pdf.pages[i]
        text = page.extract_text()
        text_file.write(text)



