from parser import parse_resume
import os

def main():
    # Specify the folder where resumes are stored
    resume_folder = './resume_data/'

    # Specify where to save the output results
    output_folder = './output/'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all resumes in the resume_data folder
    for resume_file in os.listdir(resume_folder):
        resume_path = os.path.join(resume_folder, resume_file)
        result = parse_resume(resume_path)
        
        # Save the result to CSV or JSON (optional)
        result_file = os.path.join(output_folder, f"{os.path.splitext(resume_file)[0]}_parsed.json")
        result.to_json(result_file)

        print(f"Parsed data saved to {result_file}")

if __name__ == "__main__":
    main()
