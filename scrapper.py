import os
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

def stores_data():
    # Create the "logs" folder if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Fetch the website data
    url = 'https://hotpoint.co.ke/stores/?gclid=Cj0KCQjwzdOlBhCNARIsAPMwjbwxLfqdX49U2hmPC5229iaGfASk6-qzf_3nH68UzPc4mVPRWi1zAlcaAg0tEALw_wcB'
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML and extract data
    soup = BeautifulSoup(html_content, 'html.parser')
    store_details = []
    store_elements = soup.find_all('div', class_='stores-store-body')
    for store_element in store_elements:
        name = store_element.find('h3').text.strip()
        location = store_element.find('address').text.strip()
        tel = store_element.find('p', class_='mb-0').text.strip()
        email = store_element.find('a', class_='email').text.strip()
        store_details.append((name, location, tel, email))

    # Create an Excel workbook and select the "stores" sheet
    wb = Workbook()
    sheet = wb.active
    sheet.title = "stores"

    # Write the headers
    sheet['A1'] = "Store Name"
    sheet['B1'] = "Location"
    sheet['C1'] = "Telephone"
    sheet['D1'] = "Email"

    # Write the store details to the Excel sheet
    for i, details in enumerate(store_details, start=2):
        sheet.cell(row=i, column=1).value = details[0]  # Store Name
        sheet.cell(row=i, column=2).value = details[1]  # Location
        sheet.cell(row=i, column=3).value = details[2]  # Telephone
        sheet.cell(row=i, column=4).value = details[3]  # Email

    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Generate the file name with the current date and time
    file_name = f"hotpoint_data_{current_datetime}.xlsx"

    # Specify the path to the "logs" folder
    folder_path = os.path.join(os.getcwd(), "logs")

    # Save the Excel file in the "logs" folder
    file_path = os.path.join(folder_path, file_name)
    wb.save(file_path)

def categories_data():
    # Fetch the website data for categories
    url = 'https://hotpoint.co.ke/categories'
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML and extract data for categories
    soup = BeautifulSoup(html_content, 'html.parser')
    category_details = []
    category_elements = soup.find_all('a', class_='nav-link dropdown-toggle')
    for category_element in category_elements:
        name = soup.a['title']
        category_details.append((name))

    # Select the "categories" sheet in the existing Excel file
    wb = Workbook()
    sheet = wb.create_sheet(title="categories")

    # Write the headers for categories
    sheet['A1'] = "Category Name"

    # Write the category details to the Excel sheet
    for i, details in enumerate(category_details, start=2):
        sheet.cell(row=i, column=1).value = details[0]  # Category Name

    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Generate the file name with the current date and time
    file_name = f"hotpoint_data_{current_datetime}.xlsx"

    # Specify the path to the "logs" folder
    folder_path = os.path.join(os.getcwd(), "logs")

    # Save the Excel file in the "logs" folder
    file_path = os.path.join(folder_path, file_name)
    wb.save(file_path)


# Call the functions to scrape and save the data
stores_data()
categories_data()