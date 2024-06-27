# bro.py
import pyautogui

def open_new_tab(url=None):
    if url:
        # If URL is provided, perform actions to open the specified URL
        pyautogui.hotkey("ctrl", "t")  # Open a new tab
        pyautogui.write(url)           # Write the URL
        pyautogui.press("enter")       # Press Enter to navigate to the URL
        return f"Opening new tab with URL: {url}"
    else:
        # If no URL is provided, perform default action to open a new tab
        pyautogui.hotkey("ctrl", "t")
        return "Opening new tab"

def search(query):
    pyautogui.hotkey("ctrl", "l")
    pyautogui.write(query)
    pyautogui.press("enter")
    return f"Searching for: {query}"

def close_tab():
    pyautogui.hotkey("ctrl", "w")
    return "Closing current tab"

def switch_tab(direction):
    if direction.lower() == "left":
        pyautogui.hotkey("ctrl", "shift", "tab")
        return "Switching to the left tab"
    elif direction.lower() == "right":
        pyautogui.hotkey("ctrl", "tab")
        return "Switching to the right tab"

def open_private_window():
    pyautogui.hotkey("ctrl", "shift", "n")
    return "Opening a private window"
