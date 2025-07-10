# 🧼 Streamlit Text Cleaning App

An intuitive and lightweight web application built using **Streamlit**, designed to clean textual data efficiently. Whether you're preparing data for NLP models or just organizing messy text files, this tool lets you upload `.txt` files, apply essential cleaning operations, and download the cleaned output effortlessly.

---

## 🚀 Features

🔹 Upload `.txt` files  
🔹 Apply cleaning operations interactively:
- Convert text to lowercase  
- Remove punctuation  
- Remove numbers  
- Remove stopwords (English – powered by NLTK)  

🔹 View original and cleaned text side-by-side  
🔹 Download the cleaned version as a `.txt` file  

---

## ⚙️ Technologies Used

- [Streamlit](https://streamlit.io/)
- [NLTK](https://www.nltk.org/)
- Python libraries: `re`, `string`, `io`

---

## 📦 Installation

```bash
pip install streamlit nltk
python -m nltk.downloader stopwords
## Running the App
streamlit run cleaner_text.py
## Project Structure
text-cleaning-app/
├── cleaner_text.py          # Main Streamlit app
├── cleaned.txt              # Sample output (auto-generated)
└── README.md                # Project overview and instructions
✨ Author
Developed by Javeria 🔗 https://www.linkedin.com/in/javeria9138a5344/
 🔧 Passionate about building intelligent tools with Python, NLP, and Streamlit.
