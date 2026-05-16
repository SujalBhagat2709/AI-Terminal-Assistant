from explain import explain_command

suggestions = {
    "create folder": "mkdir new_folder",
    "list files": "ls",
    "delete file": "rm file.txt"
}

def suggest_command(task):
    
    task = task.lower()
    
    for key in suggestions:
        
        if key in task:
            return suggestions[key]
    
    return "No command suggestion found"


if __name__ == "__main__":
    
    task = "create folder for project"
    
    command = suggest_command(task)
    
    print("Suggested Command:", command)
    
    print("Explanation:", explain_command(command))