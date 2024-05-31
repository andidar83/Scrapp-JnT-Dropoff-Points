import requests
import pandas as pd
import json



df = pd.read_excel('list_area.xlsx')

# Base URL
base_url = 'https://www.jet.co.id/index/router/index.html'

# Additional headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Iterate through rows and compose URLs
output = []
counter = 1
for index, row in df.iterrows():
    print("scraping data row ke = ",counter)
    url_params = {
        'method': 'query/findSiteList',
        'data[province]': row['province'],
        'data[city]': row['city'],
        'data[countyarea]': row['area'],
        'pId': '8aa5f3518d2870bb0bc30068a589e6bf',
        'pst': '73ecfe3236045a1771c42b669266d4bc'
    }

    # Construct the full URL
    full_url = f"{base_url}?{'&'.join([f'{key}={value}' for key, value in url_params.items()])}"

    # Print or use the URL as needed

    # Send POST request with additional headers
    response = requests.post(full_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON content
        json_data = response.json()

        # Extract the "data" section
        data_list = json_data.get('data', [])

        # Create a DataFrame
        df_response = pd.DataFrame(data_list)

        # Display the DataFrame
        output.append(df_response)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
    counter = counter+1
output = pd.concat(output)
output.to_excel('test_output.xlsx')
print(output)

