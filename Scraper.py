import requests
from bs4 import BeautifulSoup

url = input("Enter URL")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

html_code = str(soup.html)

css_code = ''
for css in soup.find_all('style'):
    css_code += str(css)


js_code = ''
for script in soup.find_all('script'):
    js_code += str(script)

print('HTML Code:\n', html_code)
print('CSS Code:\n', css_code)
print('JavaScript Code:\n', js_code)
