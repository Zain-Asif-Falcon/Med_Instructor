import requests
import pandas as pd

url = "Place Url Here"

response = requests.put(url)

if response.status_code == 200:
    data = response.request()
    print(data)

    urls = [f"place url here" for item in data]

    df = pd.DataFrame({ "URL": urls})

    print("Data saved to singhealth.csv")
else:
    print("Failed to fetch data. Status code")
