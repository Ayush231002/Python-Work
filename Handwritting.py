import pywhatkit as kit

# Define the text you want to convert
text = "This is a sample text converted to handwriting using pywhatkit."

# Convert the text to handwriting
kit.text_to_handwriting(text, save_to="handwriting.png")

print("Conversion complete! Check the handwriting.png file.")