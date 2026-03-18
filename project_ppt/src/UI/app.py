import streamlit as st
import requests

# Custom CSS for background and fonts
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    h1, h2, h3, h4, h5, h6 {
        color: black !important;
    }
    .stMarkdown, .stTitle, .stSubheader, .stText, .stFileUploader, .stSuccess, .stError {
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀✨ AI Powerpoint Generator ✨🚀")
st.subheader("Transform your documents into stunning presentations!")
st.write("Upload a file and let AI do the magic. Supported formats: **TXT, PDF, DOCX, CSV**.")

uploaded_file = st.file_uploader("📁 Choose a file", type=["txt", "pdf", "docx", "csv"])

if uploaded_file is not None:
    st.success(f"File '{uploaded_file.name}' uploaded successfully! 🎉")
    files = {"file": uploaded_file}
    upload_response = requests.post("http://127.0.0.1:8000/upload", files=files)

    if upload_response.status_code == 200:
        st.success("File uploaded! 🥳")
        if st.button("✨ Generate Presentation ✨"):
            with st.spinner("Generating slides..."):
                generate_response = requests.get("http://127.0.0.1:8000/generate/")
            if generate_response.status_code == 200:
                st.success("Slides generated successfully! 🤩")
                st.markdown("[⬇️ Download Presentation](output/generated_presentation.pptx)", unsafe_allow_html=True)
            else:
                st.error("Failed to generate slides.")
    else:
        st.error("Failed to upload file.")