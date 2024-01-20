import google.generativeai as genai

genai.configure(api_key='AIzaSyAucuuDu5GxCy59VW2u1WhB5v5deyssYAU')
model = genai.GenerativeModel(model_name='gemini-pro')

def getai(query):
    response = model.generate_content('The opposite of hot is')
    return (response.text)