import streamlit as st

from generator import generate_letter


st.set_page_config(page_title="AI Application Generator", layout="centered")

st.title("AI Application Generator")
st.write("Generiere ein Motivationsschreiben basierend auf deinem Profil, einer Job Description und optional einer hochgeladenen Datei.")

job_title = st.text_input("Job Title")
job_description = st.text_area("Job Description", height=200)

uploaded_file = st.file_uploader("Datei hochladen (optional)", type=["json", "txt"])

file_content = None
if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")
    st.success(f"Datei hochgeladen: {uploaded_file.name}")

if st.button("Generate"):

    if job_title and job_description:

        with st.spinner("Generiere Text..."):

            text = generate_letter(job_title, job_description, file_content)

        st.subheader("Ergebnis")
        st.write(text)

    else:
        st.error("Bitte Job Title und Job Description eingeben.")
