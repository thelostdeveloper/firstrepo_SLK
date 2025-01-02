import os
import random
from datetime import datetime, timedelta
import subprocess

REPO_PATH = r"C:\Users\priya\OneDrive\Desktop\git\firstrepo_SLK"
USERNAME = "thelostdeveloper"
EMAIL = "priyanshubharadwajp9@gmail.com"

start_date = datetime(2025, 1, 1)  # Starting date
end_date = datetime(2026, 1, 1)    # Ending date

def make_commit(date):
    with open(os.path.join(REPO_PATH, "commit.txt"), "a") as file:
        file.write(f"Commit on {date}\n")
    subprocess.run(["git", "add", "."], cwd=REPO_PATH)
    subprocess.run(["git", "commit", "-m", f'Auto-commit on {date}', "--date", date], cwd=REPO_PATH)

current_date = start_date
while current_date < end_date:
    current_date += timedelta(days=random.randint(1, 5))
    make_commit(current_date.strftime("%Y-%m-%dT%H:%M:%S"))

subprocess.run(["git", "push", "origin", "main"], cwd=REPO_PATH)
