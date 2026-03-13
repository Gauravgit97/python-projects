# Esential module for this project
import PyPDF2 as pdf
import pdfplumber
import fitz
import camelot


# Marge pdf's
def marge_pdf(pdf_list: list, output_path: str):
    """
    pdf_list: The list of the pdf files.
    output_path: The output file name. ('output_path.pdf')
    """

    pdf_writer = pdf.PdfWriter()
    for file in pdf_list:
        pdf_reader = pdf.PdfReader(file)    # Read the pdf file

        # Read all pages of the pdf
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_path,'wb') as out:
        pdf_writer.write(out)

    print(f'mearge DF save as :{output_path}')


# Split the pdf in varias file's
def split_pdf(pdf_path,output_dir):
    """
    pdf_path: A single pdf entered here.
    output_dir: Path of the folder where you want to save the pdf file.
    """

    pdf_reader = pdf.PdfReader(pdf_path)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = pdf.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        output_path = f'{output_dir}/page_{page_num +1}.pdf'

        with open(output_path,'wb') as out:
            pdf_writer.write(out)
        print(f'saved {output_path}')


# Extract text from the pdf
def extract_text(pdf_path, output_text_path):
    """
    Requirment: `pip install pdfplumber`
    pdf_path: Path of the pdf file.
    output_text_path: output file name.
    """


    with pdfplumber.open(pdf_path) as file:
        full_text  = ''
        for page in file.pages:
            full_text += page.extract_text() + '\n'

        with open(output_text_path, 'w') as f:
            f.write(full_text)
        
        print(f'Extreacted text is saved as {output_text_path}')


# Extract images from the pdf
def extract_img(pdf_path,output_dir):
    """
    Requrment : `pip install pymupdf`  this provide the `fitz`
    pdf_path : pdf file path
    output_dir: output directory where file will store
    """

    pdf_document = fitz.open(pdf_path)
    for page_index in range(len(pdf_document)):
        page = pdf_document.load_page(page_index)
        image_list = page.get_images(full=True)      # full=True => this provide full information about the image present in the page(color channel,mata_data, position, size,etc..)
        
        for img_index, img in enumerate(image_list):
            xref = img[0]     # This xref number use to specify the diffrent image. it assigned automaticly(previsly)
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image['image']
            image_ext = base_image['ext']   # Provide the image type(extension)
            image_filename = f'{output_dir}/image_{page_index +1}_{img_index +1}.{image_ext}'

            with open(image_filename,'wb') as image_file:
                image_file.write(image_bytes)

            print(f'Saved {image_filename}')


# Create the encrypted pdf file
def encrypt_pdf(input_pdf, output_pdf, password):
    """
    Requirement: `pip install PyPDF2[crypto]`
    input_pdf: Pdf file or path
    output_pdf: output pdf name
    password: Password for the pdf file(str)
    """
    pdf_reader = pdf.PdfReader(input_pdf)
    pdf_writer = pdf.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    
    pdf_writer.encrypt(password)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f'Encryoted PDF file is saved as {output_pdf}')



# Decrypte the pdf file
def decrypt_pdf(input_pdf, output_pdf, password):
    """
    Requirement: `pip install PyPDF2[crypto]`
    input_pdf: input file path or file
    output_pdf: output file name
    password: This should be the real password of the given file (type 'str'), if you ender the worong password it will error.
    """

    pdf_reader = pdf.PdfReader(input_pdf)
    pdf_reader.decrypt(password)
    pdf_writer = pdf.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])


    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f'Decrypted PDF file is saved as {output_pdf}')


# Re- arranging pages in the pdf file
def rearrange_pages(input_path, output_path, page_order):
    """
    input_path : input pdf path
    output_path : output pdf name
    page_order : new order of the pages (type => 'list')
    This function can also remove the file page..
    """
    pdf_reader = pdf.PdfReader(input_path)
    pdf_writer = pdf.PdfWriter()

    for page_num in page_order:
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

    print(f'Re-arrange PDF is saved as {output_path}')



# Read metadata in a pdf
def read_metadata(pdf_file):
    """
    meta-data :information about the document(autor name,title of the document, subject, creation data, keywords etc)(useful for=>  searching , orgnizing, managing)
    """

    pdf_reader = pdf.PdfReader(pdf_file)
    metadata = pdf_reader.metadata
    print('Metadata of the Pdf:\n')
    for key, value in metadata.items():
        print(f'{key}:{value}')


# Add metadata to the PDF file(Title, Author, etc.)
def add_metadata(input_file,output_file,title, author='gaulien'):
    """
    input_file: Input pdf file.
    output_file: Where you want to save the metadata.
    title: Title of the pdf file
    author: who will be the author of the pdf file(this can be user name or as default we be 'gaulien')
    """
    pdf_reader = pdf.PdfReader(input_file)
    pdf_writer = pdf.PdfWriter()

    for page_num in range(len(pdf_reader.pages())):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    metadata = {
        '/Title':title,
        '/Author':author
    }
    pdf_writer.add_metadata(metadata)

    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

    print(f'pdf file with updated metadata is saved as {output_file}')



# Optimize the size of the pdf(compression)
def optimize_pdf(input_file, output_file):
    pdf_document = fitz.open(input_file)  # Conver the pdf into document format
    pdf_document.save(output_file, garbage=3, deflate=True)  # garbage=3 =>reduce redundent element form the file ,deflate=True => compress the file
    print(f'PDF compresed succesfully....')


def pdf_table_to_csv(pdf:str,page: int,output_name: str):
    """
    To use this function us have:
    1.pip install camelot-py
    2.pip install tk
    3.pip install ghostscript"""

    table = camelot.read_pdf(pdf,page=page)
    table.export(f'{output_name}.csv',f ='csv',compress=True)

if '__name___' == '__main__':
    print('Welcome to pdf maniputator:\n')
    while True :
        print('Oprations:\n1.Marge.\n2.Spllit.\n3.Extract all the text.\n4.Extract all the images.\n5.Encryptin.\n6.Decryption')
        try:
            user_input = int(input('Enter the operation: '))
        except ValueError:
            print('Enter a number.')
            continue
        
        opration_list = [marge_pdf(),]
        
