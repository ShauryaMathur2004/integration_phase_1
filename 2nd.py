import streamlit as st
from io import BytesIO
from PyPDF2 import PdfReader
from streamlit_option_menu import option_menu
from fpdf import FPDF

def extract_and_concatenate_text(pdf_file):
    # Create a PDF reader object from the uploaded file
    reader = PdfReader(pdf_file)

    # Initialize a list to store all extracted text
    all_text = []

    # Iterate through all pages and extract text
    for page in reader.pages:
        text = page.extract_text()
        if text:
            # Split the text into words and concatenate with a space
            words = text.split()
            concatenated_text = ' '.join(words)
            all_text.append(concatenated_text)

    # Join text from all pages
    return '\n'.join(all_text)

if 'selected' not in st.session_state:
    st.session_state.selected = "Home"

with st.sidebar:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("Desktop/logo.png", width=200)
    st.markdown("<h1 style='text-align: center; font-size: 150%; font-weight: bold;'>PDF SENSITIVE INFORMATION MASKER</h1>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Upload File", "About"],
        icons=["house", "cloud-upload", "info"],
        default_index=0,
    )
    st.session_state.selected = selected

if st.session_state.selected == "Home":
    st.title("Welcome to My App")
    st.write("""
    <style>
    @keyframes fadeInSlideUp {
      0% {
        opacity: 0;
        transform: translateY(20px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .animated-text {
      animation: fadeInSlideUp 1s ease-out;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p class='animated-text'>PDF Sensitive Information Masker is a web application designed to safeguard your sensitive data by effectively redacting confidential information from PDF documents. Our tool utilizes advanced algorithms to identify and obscure sensitive data points such as social security numbers, credit card details, and personal addresses, ensuring compliance with data privacy regulations and protecting your sensitive information from unauthorized access.</p>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

elif st.session_state.selected == "Upload File":
    st.title("Upload a File")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Extract and concatenate text from the uploaded PDF
        concatenated_text = extract_and_concatenate_text(uploaded_file)

        # Display the extracted and concatenated text
        st.write("Extracted and Concatenated Text from PDF:")
        st.write(concatenated_text)

        # Create a sample PDF for download
        def create_sample_pdf():
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="This is a sample PDF file.", ln=True, align='C')

            pdf_output = BytesIO()
            pdf.output(pdf_output)
            pdf_output.seek(0)
            return pdf_output

        # Generate and display the download button for the sample PDF
        sample_pdf = create_sample_pdf()
        st.download_button(
            label="Download Sample PDF",
            data=sample_pdf,
            file_name="sample_file.pdf",
            mime="application/pdf"
        )

elif st.session_state.selected == "About":
    st.title("About")
    st.write("This is the about page.")




















