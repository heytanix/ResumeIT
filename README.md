# ResumeIT - Resume Parser with NLP

This project is a **Resume Parser** that extracts relevant information from resumes such as contact information, skills, work experience, and education using **Natural Language Processing (NLP)**. The tool supports resume files in PDF, DOCX, and TXT formats and outputs the parsed data in structured JSON or CSV format, making it easier for users to identify the best resumes for AI/ML training or job applications.

## Features

- **Multi-format Support**: Parse resumes in PDF, DOCX, and TXT formats.
- **Contact Information Extraction**: Extracts email addresses and phone numbers using regular expressions.
- **Skill Extraction**: Matches user-defined skill sets with the resume content.
- **Experience Extraction**: Extracts work experience using Named Entity Recognition (NER) from spaCy.
- **Education Extraction**: Identifies educational qualifications like Bachelor's, Master's, and Ph.D. degrees.
- **Structured Output**: Parsed data is saved in JSON format, making it easy to integrate with other applications.
- **Customizable Skills**: Easily modify the skill set to search for in the resumes.

## Project Structure

```plaintext
resume_parser/
│
├── main.py         # Entry point to the resume parser
├── parser.py       # Parsing logic for different file types and extraction
├── resume_data/    # Folder to store resumes in PDF, DOCX, or TXT formats
└── output/         # Folder to store parsed results in CSV or JSON format
