from preprocessing import preprocess_job

# DATA PREPERATION
# todo call scrapers here
job_descriptions = [
    """At least five years of proven experience as a Python backend developer experience designing and maintaining production systems in microservices environments Strong familiarity with cloud platforms such as AWS, Azure, or Google Cloud. Desirable qualifications include experience working in a small startup, familiarity with AWS CloudFormation, and expertise with CI/CD pipelines.""",
    """- Two years of managerial experience
    - 4 years of experience in backend development
    - Extensive experience in Python development
    - Experience in developing with SQL over Linux
    - Bachelor's degree in software engineering/computer science - an advantage
    - Experience working with DevOps technologies, Docker/K8s - an advantage
    """,
    'Our company is seeking a sales representative with excellent communication skills and a proven track record of meeting sales targets']

# DATA PREPROCESSING
preprocessed_jobs = [preprocess_job(job_description) for job_description in job_descriptions]

for i in range(len(job_descriptions)):
    print("Original:\n", job_descriptions[i])
    print("Preprocessed:\n", preprocessed_jobs[i])
    print('\n\n')
