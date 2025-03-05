import requests

def get_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[crypto]["usd"]

if __name__ == "__main__":
    crypto = input("Enter cryptocurrency (e.g., bitcoin): ").lower()
    price = get_price(crypto)
    print(f"The price of {crypto} is ${price}")
