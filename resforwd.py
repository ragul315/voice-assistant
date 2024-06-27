import re
from responce import get_response  # Assuming get_response is defined in a separate file
from weather import get_weather
from expops import *
from bro import *
from gbard import getai

patterns = [
    
    
    (r'open new tab', open_new_tab),
    (r'close tab', close_tab),
    (r'switch tab (left|right)', switch_tab),
    (r'open private window', open_private_window),
    (r'open (.+)', open),
    (r'search (.+)', search),
        # Copy pattern
    (r'copy (.+)', copy),
    
    # Move pattern
    (r'move (.+)', move),
    
    # Paste pattern
    (r'paste to (.+)', paste),
        
    # Asking for weather
    (r'what is the weather(?: at)?(?: in)? (.+)', get_weather), 
    (r'(?:how to|which is|which can|what is|what was)\s+(.+)', getai),
     # Default response pattern
    (r'.*', get_response),  # Pass get_response directly to the pattern
]


# Function to respond to user input based on patterns
def respond(message):
    for pattern, func in patterns:
        match = re.search(pattern, message.lower())
        if match:
            if match.groups():
                return func(*match.groups())
            else:
                return func(message)
    return get_response(message)

