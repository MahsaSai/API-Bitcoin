import requests

# Using a api link of a smsserver (REST API),
# I have used Kavenegar that is a smsserver 
def inform_me(price):
    API_key = 'copy your api key of this smsserver here'
    url = 'https://api.kavenegar.com/v1/{}/sms/send.json'.format(API_Key)
    payload = {'receptor':'<add phone number here>', 'message':'Hi there, Bitcoin buy price is ${},\nFrom Mahsa'.format(price)}
    response=requests.post(url, data=payload)
    print(response)
    print('Hi there, Bitcoin buy price is ${},\nFrom <your name here>'.format(price))

my_buget = 40000
#buy USD price
# if it is not woring in your regin use proxies(proxy support)
response=requests.get("https://api.coinbase.com/v2/prices/buy?currency=USD")
price = float(response.json()['data']['amount'])
print('At this moment, bitcoin is',price)
if price <= my_buget:
    inform_me(price)
