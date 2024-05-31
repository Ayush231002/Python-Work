import PyPDF2

def remove_pdf_password(input_path, output_path, password):
    # Open the encrypted PDF file in read-binary mode
    with open(input_path, 'rb') as input_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(input_file)
        
        # Check if the PDF is encrypted
        if pdf_reader.isEncrypted:
            # Decrypt the PDF using the provided password
            pdf_reader.decrypt(password)
            
            # Create a PDF writer object
            pdf_writer = PyPDF2.PdfFileWriter()
            
            # Add all pages to the PDF writer
            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))
            
            # Write the decrypted PDF to the output file
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            print("Password removed successfully.")
        else:
            print("The PDF file is not encrypted. No password removal needed.")

# Example usage
input_pdf = "File-Name"  # Path to the encrypted PDF file
output_pdf = "Save-File"  # Output path for the decrypted PDF file
password = "Password"  # Password to decrypt the PDF file

remove_pdf_password(input_pdf, output_pdf, password)
