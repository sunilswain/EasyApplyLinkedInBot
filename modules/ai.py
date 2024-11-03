from groq import Groq

client = Groq(api_key="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")

system_prompt = {
    "role": "system",
    "content": "You are a role matching system. For a single job role, output only \"Yes\" if it matches or is closely related to any of the user roles, or \"No\" if it doesn't match.\nMATCHING RULES:\n\nOutput \"Yes\" if the job role:\n\nIs identical to any user role\nIs a specialization of any user role\nShares the same core domain/skills with any user role\n\n\nOutput \"No\" if the job role:\n\nIs from a completely different domain\nHas no skill overlap with any user role\n\n\n\nExample matches:\nUser roles: [\"Data Scientist\", \"ML Engineer\"]\nJob role: \"AI Developer\"\nOutput: Yes\nUser roles: [\"Data Scientist\", \"ML Engineer\"]\nJob role: \"Frontend Developer\"\nOutput: No\nUser roles: [\"Frontend Developer\", \"UI Engineer\"]\nJob role: \"React Developer\"\nOutput: Yes"
}
def isTitleRelevant(user_roles, job_role):
    prompt = f"User Roles: {user_roles} \nJob Role: {job_role}"
    completion = client.chat.completions.create(
        model="llama-3.2-90b-text-preview",
        messages=[
            system_prompt,
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    result_string = completion.choices[0].message.content
    result = result_string.strip()
    return result

if __name__ == "__main__":
    user_roles = ["Data Analyst", "Quantitative Analyst", "Business Analyst", "Power BI Developer"]
    job_roles = ["Frontend Developer", "Data Analyst", "Machine Learning Engineer", "UI Designer", "Database Administrator", "Cloud Architect", "AI Engineer", "Data Visualization Specialist", "Software Engineer", "Operations Analyst", "Mobile Developer", "DevOps Engineer", "NLP Engineer", "Data Quality Analyst", "Business Analyst", "Cybersecurity Analyst", "Network Administrator", "Technical Writer", "Systems Analyst", "Marketing Analyst", "Research Scientist", "Cliq Developer", "Tableu Developer"]

    for job in job_roles:
        result = isTitleRelevant(user_roles, job)
        print(f"{job}: {result}")