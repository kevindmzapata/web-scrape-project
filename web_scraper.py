import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def extract_data(urls):
    all_prices = []
    all_names = []

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        name_elements = soup.find_all('h3', class_='dynamic-carousel__title')
        for element in name_elements:
            name = element.text.strip()
            all_names.append(name)

        price_elements = soup.find_all('span', class_='dynamic-carousel__price')
        for element in price_elements:
            price = element.text.strip()
            price = re.sub(r'\D', '', price)
            all_prices.append(price)

    return all_names, all_prices

def main():
    urls = [
        'https://www.mercadolibre.com.co/c/celulares-y-telefonos',
    ]

    names, prices = extract_data(urls)

    data = {
        'Name': names,
        'Price': prices
    }

    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)

    print('Data extracted and saved to data.csv')

if __name__ == '__main__':
    main()
