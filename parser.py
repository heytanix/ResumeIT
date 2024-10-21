import re
import spacy
import PyPDF2
import docx
import pandas as pd

nlp = spacy.load("en_core_web_sm")

# 1. Extract text from PDF, DOCX, or TXT files
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        raise ValueError("Unsupported file format")

# 2. Regular Expressions for Name, Email, Phone
def extract_contact_info(text):
    # Email pattern
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    email = re.findall(email_pattern, text)

    # Phone pattern (US/International)
    phone_pattern = re.compile(r'\+?\d[\d -]{8,12}\d')
    phone = re.findall(phone_pattern, text)

    return {"email": email[0] if email else None, "phone": phone[0] if phone else None}

# 3. Extract Skills
def extract_skills(text, skillset):
    # Match the skills in the text with known skillset
    skills_found = []
    for skill in skillset:
        if re.search(fr"\b{skill}\b", text, re.IGNORECASE):
            skills_found.append(skill)
    return skills_found

# 4. Extract Work Experience using Named Entity Recognition (NER)
def extract_experience(text):
    doc = nlp(text)
    experiences = []
    for ent in doc.ents:
        if ent.label_ == "ORG":
            experiences.append(ent.text)
    return experiences

# 5. Extract Education Information
def extract_education(text):
    education_keywords = ["Bachelor", "Master", "B.Sc", "M.Sc", "B.Tech", "M.Tech", "PhD"]
    education_info = []
    for keyword in education_keywords:
        if re.search(keyword, text, re.IGNORECASE):
            education_info.append(keyword)
    return education_info

# 6. Parse Resume and structure output
def parse_resume(file_path):
    text = extract_text(file_path)

    # Define the skill set to look for
    skillset = ["Python", "Machine Learning", "Data Science", "Java", "SQL", "NLP", "Deep Learning"]

    # Extract relevant fields
    contact_info = extract_contact_info(text)
    skills = extract_skills(text, skillset)
    experience = extract_experience(text)
    education = extract_education(text)

    # Structuring output
    resume_data = {
        "Name": None,  # Extracting name can be done by advanced NER, not shown in this example
        "Email": contact_info['email'],
        "Phone": contact_info['phone'],
        "Skills": skills,
        "Experience": experience,
        "Education": education
    }

    # Convert to DataFrame for better output
    return pd.DataFrame([resume_data])
