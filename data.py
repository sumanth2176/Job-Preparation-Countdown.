data = {
    "project_title": "T-Minus Countdown: Job Preparation",
    "target_device": "Android",
    "aspect_ratio": "9:16",
    "style": "Neon Cyberpunk",
    "palette": [
        "black",
        "electric purple",
        "blue",
        "neon pink"
    ],
    "reference_date": "2026-11-25",
    "deadline_date": "2026-12-15",
    "days_remaining_at_reference": 20,
    "headline": "T-MINUS COUNTDOWN: JOB PREPARATION",
    "quote": "Discipline turns preparation into readiness.",
    "milestones": [
        {
            "code": "T-14",
            "date": "2026-12-01",
            "label": "December 1",
            "task": "Revise Java and SQL.",
            "completed": False
        },
        {
            "code": "T-7",
            "date": "2026-12-08",
            "label": "December 8",
            "task": "Practice coding and aptitude.",
            "completed": False
        },
        {
            "code": "T-3",
            "date": "2026-12-12",
            "label": "December 12",
            "task": "Take mock interviews.",
            "completed": False
        },
        {
            "code": "T-1",
            "date": "2026-12-14",
            "label": "December 14",
            "task": "Final revision and rest.",
            "completed": False
        }
    ]
}

if __name__ == "__main__":
    print("Project:", data["project_title"])
    print("Deadline:", data["deadline_date"])
    print("Milestones:")
    for milestone in data["milestones"]:
        print(
            milestone["code"],
            "-",
            milestone["label"],
            ":",
            milestone["task"]
        )
