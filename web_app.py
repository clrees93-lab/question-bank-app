import streamlit as st
from data_management import load_questions_from_json
from logic import check_answer, list_paper_tags

st.set_page_config(page_title="BPT Question Bank", layout="wide")

questions = load_questions_from_json()

st.title("BPT Question Bank")

st.write(f"Loaded {len(questions)} questions.")

specialties = sorted({q.specialty for q in questions})
selected_specialty = st.selectbox("Choose specialty", ["All"] + specialties)

if selected_specialty == "All":
    pool = questions
else:
    pool = [q for q in questions if q.specialty == selected_specialty]

st.write(f"{len(pool)} questions in this selection.")
