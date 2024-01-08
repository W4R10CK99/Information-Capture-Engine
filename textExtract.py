import streamlit as st
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'Tesseract-OCR\\tesseract.exe'

# Function to extract text from image
def extract_text_from_image(img):
    text = tess.image_to_string(img)
    return text

# Function to format text
def format_text(text):
    formatted_text = text.strip()
    lines = formatted_text.split('\n\n')  # or '\n' depending on your needs
    formatted_text = '\n'.join(lines)
    return formatted_text

# Streamlit app
def main():
    st.title("Image Text Extraction App")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform text extraction
        extracted_text = extract_text_from_image(image)

        # Perform text formatting
        formatted_text = format_text(extracted_text)

        # Save formatted text to a temporary text file
        with st.expander("Download Formatted Text"):
            st.write(formatted_text)
            st.markdown(get_download_link(formatted_text, 'formatted_output.txt'), unsafe_allow_html=True)

# Function to create a download link for a text file
def get_download_link(text, filename):
    """Generates a link allowing the text content to be downloaded."""
    href = f'<a href="data:text/plain;charset=utf-8,{text}" download="{filename}">Download {filename}</a>'
    return href

# Run the Streamlit app
if __name__ == "__main__":
    main()
