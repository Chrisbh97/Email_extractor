import requests
from bs4 import BeautifulSoup
import re

def find_emails_on_website(url):
    # Make a request to the website
    response = requests.get(url)
    
    # If the request was successful, proceed
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all text from the website
        text = soup.get_text()
        
        # Define a regex pattern for emails
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        # Find all matches of the pattern
        emails = re.findall(email_pattern, text)
        
        return emails
    else:
        print(f"Failed to retrieve {url}")
        return []

def save_results(emails, filename):
    with open(filename, 'w') as file:
        for email in emails:
            file.write(email + '\n')

# Example usage
url = 'https://about.google/contact-google/'
emails = find_emails_on_website(url)
save_results(emails, 'email_results.txt')
