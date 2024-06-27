import pyautogui
import pytesseract
import time
from PIL import Image
from exeapp import open_application

# Path to the Tesseract executable (change this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def hovermouseto(text_to_find):
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Save the screenshot as a temporary image file
    temp_image_path = "temp_screen_capture.png"
    screenshot.save(temp_image_path)

    # Use pytesseract to find all occurrences of the text on the screen
    image = Image.open(temp_image_path)
    text_locations = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    found = False  # Flag to check if text is found

    # Convert the text to find to lowercase
    text_to_find_lower = text_to_find.lower()

    # Loop through all text occurrences and find the one we're interested in
    for i in range(len(text_locations['text'])):
        # Convert the found text to lowercase
        found_text_lower = text_locations['text'][i].strip().lower()
        if found_text_lower == text_to_find_lower:
            x = text_locations['left'][i]
            y = text_locations['top'][i]
            width = text_locations['width'][i]
            height = text_locations['height'][i]
            
            # Calculate the center of the found text region
            center_x = x + width // 2
            center_y = y + height // 2

            # Move the mouse to the center of the found text region
            pyautogui.moveTo(center_x, center_y, duration=0.5)

            # Add a short delay after hovering
            time.sleep(2)
            
            found = True  # Set flag to True
            break  # Exit the loop once the first occurrence is found

    # Delete the temporary image file
    image.close()
    del image
    del screenshot

    # Return appropriate message if text is not found
    if not found:
        return False
    else:
        return True


def open(text_to_find):
    if hovermouseto(text_to_find):
        pyautogui.doubleClick()
        return f"Opening {text_to_find}..."
    elif open_application(text_to_find):
        return f"Opening {text_to_find}..."
    else:
        return f"'{text_to_find}' not found or couldn't be opened"
        
def copy(text_to_find):
    if hovermouseto(text_to_find):
        pyautogui.hotkey('ctrl', 'c')
        return f"Text copied from '{text_to_find}' to clipboard."
    else:
        return f"'{text_to_find}' not found."

def move(text_to_find):
    if hovermouseto(text_to_find):
        pyautogui.hotkey('ctrl', 'x')
        return f"Text moved (cut) from '{text_to_find}' to clipboard."
    else:
        return f"'{text_to_find}' not found."

def paste():
    pyautogui.hotkey('ctrl', 'v')
