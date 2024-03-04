import pathlib
import textwrap
import csv
API_KEY='AIzaSyA6zIjic5VY7a4m026zboRL_8qHTCOj0EU'
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=API_KEY)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("""write a similar text for blurry screen  in going from main menu to google page where the actual output is a clear screen without blur and as a random issue.
                                  issue type: random
                                  steps to reproduce : home -> main menu -> google page
                                  
L103 23.02.24 3:08pm
On continuous clicking of phone bazzle button , the previous screen is displayed for a split second

Issue type: sporadically

Steps to reproduce
1) tap on the  phone bazzle button continuously. 


Expected output
The ivi should remain on phone screen. 

Actual output
Ivi displayed the previous page ie the music screen for a split second
                                  
                                  """)
# Display the generated content using Markdown
# markdown_response = to_markdown(response.text)
# display(markdown_response)

if response._error:
    print("Error occurred:", response._error)
else:
    # Convert the generated content to Markdown format
    print(response.text)

    # Display the generated content using Markdown
    
import os
os.system("python main.py")