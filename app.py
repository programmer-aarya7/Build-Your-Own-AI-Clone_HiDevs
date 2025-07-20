import streamlit as st
import os
from dotenv import load_dotenv
from utils.chunking import chunk_pdf, chunk_url
from rag_pipeline import build_rag_chain

load_dotenv()

st.set_page_config(page_title="Askie the Bot 🤖", layout="wide")
st.markdown("<h1 style='text-align: center;'>ASKIE 🤖 - Your Personalized AI Clone Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>📚 Upload. 🌐 Link. ❓ Ask. 💡 Answer </h4>", unsafe_allow_html=True)
st.divider()

# File upload and URL input
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("📄 Upload a PDF", type="pdf")
with col2:
    url = st.text_input("🌐 Or enter a website URL")

chunks, rag_chain = [], None

with st.spinner("🔍 Processing content..."):
    if uploaded_file:
        file_path = f"./data/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        chunks = chunk_pdf(file_path)
    elif url:
        chunks = chunk_url(url)

if chunks:
    st.success("✅ Content successfully chunked and embedded!")
    rag_chain = build_rag_chain(chunks)

if rag_chain:
    prompt = st.chat_input("💭 Ask your AI clone something...")
    if prompt:
        result = rag_chain(prompt)

        st.markdown("⭐ Response")
        st.info(result["result"])

        st.markdown("Source Documents")
        for i, doc in enumerate(result["source_documents"]):
            with st.expander(f"📄 Document {i+1}"):
                st.code(doc.page_content[:500] + "...")

        # Optional: Log to Arize
        try:
            from arize.pandas.logger import Client
            from arize.utils.types import ModelTypes

            arize_client = Client(
                space_key="your-arize-space",
                api_key=os.getenv("ARIZE_API_KEY")
            )

            arize_client.log(
                model_id="mistral-rag-bot",
                model_version="v1",
                model_type=ModelTypes.LLM,
                prediction_id=st.session_state.get("session_id", "local"),
                prompt=prompt,
                response=result["result"]
            )
        except Exception as e:
            st.warning(f"Arize logging failed: {e}")
