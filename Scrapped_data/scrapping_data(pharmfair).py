import requests
import pandas as pd

url = "Place Url Here"

payload = {
      "Place payload here like"
    'draw': '1',
    'columns[0][data]': '0',
    'columns[0][name]': 'license',
}

files=[

]

response = requests( url, data=payload, files=files, verify=False)

print(response.text)
print(type(response))

data = response['data']
columns = ["Place columns data here",'License', 'DosageForm']

# Creating a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save DataFrame to CSV
df.to_csv('pharmfair.csv')

print("pharmfair.csv file saved successfully.")