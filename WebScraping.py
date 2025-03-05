import requests
from bs4 import BeautifulSoup

url = "https://www.mediamarkt.com.tr/tr/category/laptop-504926.html"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
# URL'den HTML içeriğini al
# Get HTML content from the URL
html = requests.get(url, headers=headers).content

# HTML içeriğini BeautifulSoup ile ayrıştır
# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Belirtilen sınıfa sahip div'leri bul, ilk 10 tanesini al
# Find divs with the specified class, limit to the first 10
list = soup.find_all("div", {"class": "sc-5357e6a3-0 cbHULG"}, limit=10)

# Her bir ürün için bilgileri al ve yazdır
# Retrieve and print information for each product
for item in list:
    # Ürün adını al
    # Get the product name
    productName = item.find("a", {"class": "sc-35c6ad71-1 dxFAqR sc-75f73975-0 gEfSZX"}).string
    
    # Ürün fiyatını al
    # Get the product price
    productPrice = item.find("span", {"class": "sc-d571b66f-0 nRwOI sc-9504f841-2 lgovom"}).string
    
    # Ürün bağlantısını al
    # Get the product link
    productLink = item.find("a", {"class": "sc-35c6ad71-1 dxFAqR sc-75f73975-0 gEfSZX"}).get("href")
    
    # Fiyatı virgülden ayır
    # Split the price by comma
    productPrice = productPrice.split(",")
    
    # Ürün bilgilerini yazdır
    # Print the product information
    print(f'Ürün Adı: {productName}\nÜrünün Fiyatı: {productPrice[0]}\nÜrünün Linki: https://www.mediamarkt.com.tr{productLink}\n')