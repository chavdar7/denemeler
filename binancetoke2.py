import json
import requests

class binance:
    def __init__(self):
        self.api_url="https://api.binance.com/api/v3/ticker/price"

    def sembol(self):
        response = requests.get(self.api_url)
        return response.json()
    
semboller = binance()
text = json.dumps(semboller.sembol())
semboller_arr = [sembol["symbol"] for sembol in semboller.sembol()]
print(text)
#print([sembol["symbol"] for sembol in semboller.sembol()])
while True:
    istek = input("öğrenmek istediğiniz coini giriniz. Çıkmak için : 'q'")
    if istek=="q":
        break
    if istek not in semboller_arr:
        print("düzgün gir gevşekk")
        continue
    print(text.split(istek)[1].split('", "price": "')[1].split('"')[0])

    
