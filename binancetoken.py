import requests

class binance:
    def __init__(self):
        self.api_url="https://api.binance.com/api/v3/ticker/price"

    def sembol(self):
        response = requests.get(self.api_url)
        return response.json()
    
semboller = binance()

for sembol in semboller.sembol(): 
    print(sembol["symbol"])

while True:
    istek = input("Öğrenmek istediğiniz coini giriniz, çıkmak için: q ")

    if istek == "q":
        break
    else:
        for sembol in semboller.sembol():
            if sembol["symbol"] == istek:
                print(sembol["price"])
