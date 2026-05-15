import streamlit as st

from generator import generate_letter


st.set_page_config(page_title="AI Application Generator", layout="centered")

st.title("My AI Application Generator")
st.write("Generiere ein Motivationsschreiben basierend auf deinem Profil, einer Job Description und optional einer hochgeladenen Datei.")

job_title = st.text_input("Job Titel")
job_description = st.text_area("Job Description", height=200)

if st.button("Generate"):

    if job_title and job_description:

        with st.spinner("Generiere Text..."):

            text = generate_letter(job_title, job_description)

        st.subheader("Ergebnis")
        st.write(text)

    else:
        st.error("Bitte Job Titel und Job Description eingeben.")
