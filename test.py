import requests

url = 'https://portal.vspu.ru/login'

response = requests.post(url, data={'loginform-username':'baykinaea@mail.ru', 'loginform-password':'vova10021962'})

if response.status_code == 200:
    print(response.text)
else:
    print(f'Server error: {response.status_code}')