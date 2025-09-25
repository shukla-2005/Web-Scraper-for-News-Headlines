import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

# URL of the news website to scrape (BBC News as an example)
url = "https://www.bbc.com/news"

try:
    # Send HTTP GET request to fetch the webpage
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <h2> tags containing headlines (adjust tag/class as per website structure)
    headlines = soup.find_all('h2')

    # Create a .txt file with a timestamp in the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"headlines_{timestamp}.txt"

    # Write headlines to the .txt file
    with open(output_file, 'w', encoding='utf-8') as file:
        for idx, headline in enumerate(headlines, 1):
            headline_text = headline.get_text().strip()
            if headline_text:  # Ensure non-empty headlines
                file.write(f"{idx}. {headline_text}\n")

    print(f"Headlines successfully saved to {output_file}")

except requests.RequestException as e:
    print(f"Error fetching the webpage: {e}")
except Exception as e:
    print(f"An error occurred: {e}")