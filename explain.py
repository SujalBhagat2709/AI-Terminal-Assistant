command_docs = {
    "ls": "Lists files and folders",
    "cd": "Changes current directory",
    "mkdir": "Creates a new folder",
    "rm": "Deletes files or folders"
}

def explain_command(command):
    
    base_command = command.split()[0]
    
    return command_docs.get(
        base_command,
        "Command explanation not found"
    )


if __name__ == "__main__":
    
    result = explain_command("mkdir projects")
    
    print(result)