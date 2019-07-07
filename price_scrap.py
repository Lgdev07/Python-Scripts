import requests, smtplib
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

msg = []

def get_price_gearvita():
    urls_wanted_price = {'https://gearvita.com/xiaomi-huami-amazfit-bip-2-smartwatch.html': 60,
                         'https://gearvita.com/xiaomi-redmi-airdots-tws-bluetooth-5-0-earphones.html':50}
    site_name = 'Gearvita'

    for site, wanted_price in urls_wanted_price.items():
        page = requests.get(site, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')    
        title = soup.find("span", attrs={'class': 'base'}).text
        price = soup.find("span", attrs={'class': 'price'})
        # print(f'\n{title.text}\n')
        if float(price.text[1:]) <= wanted_price:
            msg.append(f'O produto do site {site_name} está menor!!\n\n{title} - {float(price.text[1:])}\n\n\n')

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('from_email','from_password')

    if msg:
        server.sendmail(
            'from_email',
            'to_email',
            ''.join(msg).encode('utf-8')
        )
        print('Email has been sent!')

    server.quit()

get_price_gearvita()
send_mail()