import requests
import json

apiKey = '3ede2355da2f43e921590dc5'
apiUrl = f'https://v6.exchangerate-api.com/v6/{apiKey}/latest/'


def exchangeRateCalculate(excnageRate):
    result = requests.get(excnageRate)
    resultJSON = json.loads(result.text)
    return resultJSON


while True:
    try:
        while True:
            resultChoices = input("""************************** Exchange Rate Calculate **************************
                                \n1 - TRY - USD\n2 - TRY - EUR\n3 - EUR - TRY\n4 - EUR - USD\n5 - USD - TRY\n6 - USD - EUR\n7 - Exit\nExchange Choices: """)
            if resultChoices == '7':
                break
            else:
                tryCurrency = 'TRY'
                usdCurrency = 'USD'
                eurCurrency = 'EUR'
                amount = input('Enter the amount of currency you are converting: ')
                if resultChoices == '1':
                    result = exchangeRateCalculate(apiUrl+tryCurrency)
                    print(f'{amount} TRY = {result['conversion_rates']["USD"]} USD')
                elif resultChoices == '2':
                    result = exchangeRateCalculate(apiUrl+tryCurrency)
                    print(f'{amount} TRY = {result['conversion_rates']["EUR"]} EUR')
                elif resultChoices == '3':
                    result = exchangeRateCalculate(apiUrl+eurCurrency)
                    print(f'{amount} EUR = {result['conversion_rates']["TRY"]} TRY')
                elif resultChoices == '4':
                    result = exchangeRateCalculate(apiUrl+eurCurrency)
                    print(f'{amount} EUR = {result['conversion_rates']["USD"]} USD')
                elif resultChoices == '5':
                    result = exchangeRateCalculate(apiUrl+usdCurrency)
                    print(f'{amount} USD = {result['conversion_rates']["TRY"]} TRY')
                elif resultChoices == '6':
                    paresult = exchangeRateCalculate(apiUrl+usdCurrency)
                    print(f'{amount} USD = {result['conversion_rates']["EUR"]} EUR')
                else:
                    print('Please enter a valid value!')
    except Exception as ex:
        print(f'Exception: {ex}')
            








import requests
import json


apiKey = '3ede2355da2f43e921590dc5' # API anahtarını tanımlıyoruz # Defining the API key
apiUrl = f'https://v6.exchangerate-api.com/v6/{apiKey}/latest/'# API URL'sini oluşturuyoruz # Creating the API URL


# Döviz kuru hesaplama fonksiyonu # Function to calculate exchange rates
def exchangeRateCalculate(excnageRate):
    result = requests.get(excnageRate)  # API'den veri alıyoruz     # We are fetching data from the API
    resultJSON = json.loads(result.text)  # JSON formatında veriyi yüklüyoruz # Loading the data in JSON format
    return resultJSON

while True:
    try:
        while True:
            resultChoices = input("""************************** Exchange Rate Calculate **************************
                                \n1 - TRY - USD\n2 - TRY - EUR\n3 - EUR - TRY\n4 - EUR - USD\n5 - USD - TRY\n6 - USD - EUR\n7 - Exit\nExchange Choices: """)
            if resultChoices == '7':
                break  

            else:
                tryCurrency = 'TRY'
                usdCurrency = 'USD'
                eurCurrency = 'EUR'
                amount = input('Enter the amount of currency you are converting: ')
                # Kullanıcının dönüştürmek istediği miktarı alıyoruz # Getting the amount the user wants to convert
                if resultChoices == '1':
                    result = exchangeRateCalculate(apiUrl+tryCurrency)
                    print(f'{amount} TRY = {result["conversion_rates"]["USD"]} USD')
                elif resultChoices == '2':
                    result = exchangeRateCalculate(apiUrl+tryCurrency)
                    print(f'{amount} TRY = {result["conversion_rates"]["EUR"]} EUR')
                elif resultChoices == '3':
                    result = exchangeRateCalculate(apiUrl+eurCurrency)
                    print(f'{amount} EUR = {result["conversion_rates"]["TRY"]} TRY')
                elif resultChoices == '4':
                    result = exchangeRateCalculate(apiUrl+eurCurrency)
                    print(f'{amount} EUR = {result["conversion_rates"]["USD"]} USD')
                elif resultChoices == '5':
                    result = exchangeRateCalculate(apiUrl+usdCurrency)
                    print(f'{amount} USD = {result["conversion_rates"]["TRY"]} TRY')
                elif resultChoices == '6':
                    result = exchangeRateCalculate(apiUrl+usdCurrency)
                    print(f'{amount} USD = {result["conversion_rates"]["EUR"]} EUR')
                else:
                    print('Please enter a valid value!')  
    except Exception as ex:
        print(f'Exception: {ex}')  # Hata durumunda mesaj yazdırıyoruz # Printing the error message in case of an exception
