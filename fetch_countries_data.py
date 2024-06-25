import requests
import json
import os

# Function to fetch country data from API and save as JSON
def fetch_and_save_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        country_data = response.json()[0]  # Assuming the API returns data as a list with one element
        
        # Write data to JSON file
        filename = f"{country_name}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(country_data, f, ensure_ascii=False, indent=4)
            
        print(f"Successfully saved {country_name} data to {filename}")
    else:
        print(f"Failed to fetch data for {country_name}. Status code: {response.status_code}")

# List of countries
countries = ['india', 'us', 'uk', 'china', 'russia']

# Fetch and save data for each country
for country in countries:
    fetch_and_save_country_data(country)
