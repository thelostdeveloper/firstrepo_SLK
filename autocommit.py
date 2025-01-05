import os
import random
from datetime import datetime, timedelta
import subprocess

# Configuration
REPO_PATH = r"C:\Users\priya\OneDrive\Desktop\git\firstrepo_SLK"  # Replace with your repo path
COMMITS_PER_DAY = random.randint(6, 8)  # Number of commits per day
END_DATE = datetime(2026, 1, 1)  # End date for commits

# Function to make a single commit
def make_commit(commit_date):
    # Write a line to a file to simulate a change
    with open(os.path.join(REPO_PATH, "commit.txt"), "a") as file:
        file.write(f"Commit on {commit_date}\n")
    
    # Stage and commit the change
    subprocess.run(["git", "add", "."], cwd=REPO_PATH)
    subprocess.run(
        ["git", "commit", "-m", f'Auto-commit on {commit_date}', "--date", commit_date],
        cwd=REPO_PATH
    )

# Function to make daily commits
def make_daily_commits():
    current_date = datetime.now()

    if current_date >= END_DATE:
        print("Reached end date. No more commits.")
        return

    # Generate 6-8 commits for the current day
    for _ in range(COMMITS_PER_DAY):
        random_time = current_date + timedelta(seconds=random.randint(0, 86399))  # Random time today
        commit_date = random_time.strftime("%Y-%m-%dT%H:%M:%S")
        make_commit(commit_date)
    
    # Push today's commits to GitHub
    subprocess.run(["git", "push", "origin", "main"], cwd=REPO_PATH)
    print(f"Pushed {COMMITS_PER_DAY} commits for {current_date.strftime('%Y-%m-%d')}.")

# Execute the daily commit process
make_daily_commits()
