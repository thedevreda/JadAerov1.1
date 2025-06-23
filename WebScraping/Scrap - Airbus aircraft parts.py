import requests
from bs4 import BeautifulSoup
import csv
import time
import os 



def scrape_boeing_parts():
    # List to store all the parts data
    all_parts = []
    
    # Loop through pages 1 to 23
    for page_num in range(1, 24):
        print(f"Scraping page {page_num}...")
        
        # Create the URL for each page
        page_url = f'https://www.aerospacepurchasing.com/manufacturer/airbus-industries/page-{page_num}/'

        # Get the webpage content
        response = requests.get(page_url)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Find the main table with Boeing parts
        table_div = soup.find('div', {'class': 'manufacturers-inner-table'})
        
        # Find the actual table inside the div
        table = table_div.find('table')
        
        # Find all table rows in the tbody (skip the header)
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
        
        # Extract data from each row
        for row in rows:
            # Find all table cells in this row
            cells = row.find_all('td')
            
            # Get part number from first cell
            part_number_cell = cells[0]
            part_number = part_number_cell.find('a').text.strip()
            
            # Get description from second cell
            description = cells[1].text.strip()
            
            # Get aircraft model from third cell
            aircraft_model = cells[2].text.strip()

            # Add the data to our list
            part_data = {
                'Part Number': part_number,
                'Description': description,
                'Aircraft Model': aircraft_model
            }
            
            all_parts.append(part_data)
        
        print(f"Found {len(rows)} parts on page {page_num}")
        
        # Be nice to the server - wait a bit between requests
        time.sleep(1)
    
    return all_parts

# Get the current working directory and define the file path
pwd = os.getcwd()
file_path = os.path.join(pwd, r'\Data\Data - Airbus_parts.csv')

def save_to_csv(parts_data, filename=file_path):
    # Save the scraped data to a CSV file
    # Create CSV file with headers
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Part Number', 'Description', 'Aircraft Model']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header row
        writer.writeheader()
        
        # Write all the parts data
        for part in parts_data:
            writer.writerow(part)
    
    print(f"Data saved to {filename}")

# Main execution
if __name__ == "__main__":
    # Scrape all the data
    scraped_parts = scrape_boeing_parts()
    
    # Save to CSV file
    save_to_csv(scraped_parts)