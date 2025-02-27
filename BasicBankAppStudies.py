#************Basic Bank Application************
SadikAccount = {
    'name' : 'Sadık Turan',
    'accountNo' : '12345678',
    'balance' : 3000,
    'addAccount' : 2000
}

AliAccount = {
    'name' : 'Ali Turan',
    'accountNo' : '12345679',
    'balance' : 2000,
    'addAccount' : 1000
}

# Para çekme fonksiyonu - hesap ve para çekme tutarı alıyoruz
# Withdrawal function - we get account and withdrawal amount
def money_pull(account, amount):
    print(f"Hello {account['name']}")
    # Hesapta yeterli bakiye varsa para çekilebilir
    # If there is sufficient balance in the account, money can be withdrawn.
    if(account['balance'] >= amount):
        account['balance'] -= amount
        print('You can get your money')
    else:# Eğer yeterli bakiye yoksa. -- If there is not enough balance. 
        total = account['balance'] + account['addAccount']
        # Ek hesap ve mevcut bakiyenin toplamı istenilen miktardan fazlaysa.
        # If the sum of the additional account and the available balance is more than the requested amount.
        if(total >= amount):
            addAccountUsage = input('Use additional account?(E/H): ')   

            if addAccountUsage.upper() == 'E':# Ek hesabı kullanmak isteyip istemediğimizi soruyoruz. -- # We are asked if we want to use the additional account.
                addAccountUsageBalance = amount - account['balance']
                account['balance'] = 0 # Ana hesap sıfırlanıyor. -- The main account is resetting.
                account['addAccount'] -= addAccountUsageBalance # Ek hesap bakiyesi düşürülüyor. -- Additional account balance is reduced.
                print('You can get your money')
            else:    
                print(f"You have a balance of {account['balance']} and an additional balance of {account['addAccount']} in your account number {account['accountNo']}.")    
        else:
            print("Insufficient funds!")
# Hesap bakiyesi sorgulama fonksiyonu.
# Account balance inquiry function.
def balance_quest(account):
    print(f"\n****************\nAccount No: {account['accountNo']}\nThere is a balance of {account['balance']} in your account.\nThere is a balance of {account['addAccount']} in your additional account.\n****************\n")

# Fonksiyonları test etme.
# Testing functions.
money_pull(SadikAccount,3000)
balance_quest(SadikAccount)
money_pull(SadikAccount,2000)
balance_quest(SadikAccount)