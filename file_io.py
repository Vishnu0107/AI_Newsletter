from datetime import datetime

def save_markdown(task_output):
    print("Task output received:", task_output.result)
    if not task_output or not getattr(task_output, "result", None):
        print("No content to save. Task output is empty.")
        return
    today_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today_date}.md"
    with open(filename, "w") as file:
        file.write(task_output.result)
    print(f"Newsletter saved as {filename}")