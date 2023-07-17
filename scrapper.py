import requests
from bs4 import BeautifulSoup

url = 'https://hotpoint.co.ke/'

# Send a GET request to the website and retrieve the content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Example: Extract product names
product_names = []
product_elements = soup.find_all('div', class_='product-info')
for product_element in product_elements:
    name = product_element.find('a').text.strip()
    product_names.append(name)

# Print the extracted product names
for name in product_names:
    print(name)
