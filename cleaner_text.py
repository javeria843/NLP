import streamlit as st
import nltk
import re
import string
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Cleaning functions
def clean_text(text, lowercase, remove_punct, remove_nums, remove_stops):
    if lowercase:
        text = text.lower()
    if remove_punct:
        text = text.translate(str.maketrans("", "", string.punctuation))
    if remove_nums:
        text = re.sub(r"\d+", "", text)
    if remove_stops:
        text = " ".join([word for word in text.split() if word.lower() not in stop_words])
    return text

# Streamlit UI
st.title("🧼 Simple Text Cleaning App")

uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
if uploaded_file:
    raw_text = uploaded_file.read().decode("utf-8")
    st.text_area("Original Text", raw_text, height=150)

    st.subheader("Choose Cleaning Options:")
    lowercase = st.checkbox("Lowercase")
    remove_punct = st.checkbox("Remove punctuation")
    remove_nums = st.checkbox("Remove numbers")
    remove_stops = st.checkbox("Remove stopwords")

    cleaned = clean_text(raw_text, lowercase, remove_punct, remove_nums, remove_stops)
    st.text_area("Cleaned Text", cleaned, height=150)

    st.download_button("Download Cleaned Text", cleaned, file_name="cleaned.txt", mime="text/plain")
