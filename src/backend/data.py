# src/backend/data.py

employees = [
    {
        "id": "1",
        "name": "Jane Doe",
        "role": "Software Engineer",
        "department": "Engineering",
        "skills": ["Python", "Machine Learning", "API Development"],
        "contact": "jane.doe@example.com",
        "projects": [
            {
                "project_id": "101",
                "name": "Project Alpha",
                "description": "Developed a machine learning model to predict customer behavior.",
                "role": "Lead Developer",
                "duration": {"start": "2022-01-01", "end": "2022-06-01"},
                "technologies_used": ["Python", "TensorFlow", "SQL"],
                "team_members": ["John Smith", "Emily Zhang"]
            }
        ]
    },
    {
        "id": "2",
        "name": "John Smith",
        "role": "Data Analyst",
        "department": "Data Science",
        "skills": ["SQL", "Data Visualization", "Python"],
        "contact": "john.smith@example.com",
        "projects": [
            {
                "project_id": "102",
                "name": "Project Beta",
                "description": "Analyzed customer data to improve the model.",
                "role": "Data Analyst",
                "duration": {"start": "2021-07-01", "end": "2021-12-01"},
                "technologies_used": ["SQL", "Python", "Power BI"],
                "team_members": ["Jane Doe"]
            }
        ]
    }
]
