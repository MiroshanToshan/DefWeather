import requests


city = input("Введите город: ")
url = f"https://wttr.in/{city}"
params = {
    "nM": "",
    "lang": "ru"

}

response = requests.get(url, params=params)
response.raise_for_status()
print(response.text)