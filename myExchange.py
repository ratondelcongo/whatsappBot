import requests
apiKEY = '1e38b4cc549a16e16b8fb96b'
url = 'https://prime.exchangerate-api.com/v5/' + apiKEY + '/latest/PEN'

response = requests.get(url)
data = response.json()

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def get_exchange(coin,change):
    exchange = change/data['conversion_rates'][coin]
    exchange = truncate(exchange,2)
    strs = str(change) + ' ' + coin + ' = ' + 'S/.' + str(exchange)
    return  strs