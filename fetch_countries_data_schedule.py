import requests
import json
import os
import schedule
import time
from datetime import datetime, timedelta

# List of countries and their corresponding URLs
countries = {
    'India': 'https://restcountries.com/v3.1/name/india',
    'US': 'https://restcountries.com/v3.1/name/us',
    'UK': 'https://restcountries.com/v3.1/name/uk',
    'China': 'https://restcountries.com/v3.1/name/china',
    'Russia': 'https://restcountries.com/v3.1/name/russia'
}

# Directory to save JSON files
save_dir = './country_data/'

# Ensure the directory exists, create it if it doesn't
os.makedirs(save_dir, exist_ok=True)

# Function to fetch data from API and save as JSON
def fetch_and_save_country_data(country, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Extract data from response
        country_data = response.json()[0]  # API returns a list, take the first element

        # Save data to JSON file
        filename = os.path.join(save_dir, f'{country}.json')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(country_data, f, ensure_ascii=False, indent=4)
        print(f'Saved {country} data to {filename}')
    else:
        print(f'Failed to fetch data for {country}. Status code: {response.status_code}')

# Function to fetch and save data for all countries
def fetch_and_save_all_countries():
    for country, url in countries.items():
        fetch_and_save_country_data(country, url)

# Schedule tasks for 12:00 AM and 12:00 PM IST
def schedule_tasks():
    # Schedule for 12:00 AM IST
    schedule.every().day.at("00:00").do(fetch_and_save_all_countries)

    # Schedule for 12:00 PM IST
    schedule.every().day.at("12:00").do(fetch_and_save_all_countries)

    # Infinite loop to run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Start the scheduler
    schedule_tasks()
