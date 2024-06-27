import os
import subprocess
import winshell

def open_application(app_name):
    program_folders = [
        "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs",
        "C:\\Users\\jragu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
    ]

    app_name_lower = app_name.lower()
    
    for folder in program_folders:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if app_name_lower in os.path.splitext(file.lower())[0]:
                    file_to_open = os.path.join(root, file)
                    if file.endswith(".lnk"):
            
                        target = winshell.shortcut(os.path.join(root, file)).path
                        file_to_open = target
                    try:
                        subprocess.Popen(file_to_open)
                        return True
                    except FileNotFoundError:
                        return False
    
    return False