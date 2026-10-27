import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Page
st.set_page_config(
    page_title="AI Resume Generator",
    page_icon="📄"
)

st.title("📄 AI Resume Generator")
st.write("Create a professional resume using AI")

# User input
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
education = st.text_area("Education")
skills = st.text_area("Skills")
experience = st.text_area("Experience")
projects = st.text_area("Projects")

# Generate button
if st.button("✨ Generate Resume"):

    if name == "":
        st.warning("Please enter your name.")
        st.stop()

    prompt = f"""
    Create a professional and ATS-friendly resume.

    Candidate Information:

    Name: {name}
    Email: {email}
    Phone: {phone}

    Education:
    {education}

    Skills:
    {skills}

    Experience:
    {experience}

    Projects:
    {projects}

    Create the following sections:

    1. Professional Summary
    2. Skills
    3. Experience
    4. Projects
    5. Education

    Make the resume professional and concise.
    Do not invent information.
    """

    with st.spinner("Generating your resume..."):

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )

    resume = response.choices[0].message.content

    st.success("Resume generated successfully!")

    st.subheader("Your Resume")

    st.markdown(resume)

    # Download
    st.download_button(
        label="⬇️ Download Resume",
        data=resume,
        file_name="resume.txt",
        mime="text/plain"
    )
