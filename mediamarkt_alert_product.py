# -*- coding: utf-8 -*-
"""
Created on 2020

@author: Antonio Fernández Troyano
"""
import requests
import bs4
import time
import random
import datetime

#Leemos fichero con urls de productos y precio objetivo       
def read_file(name, numbers=False):
    with open(name, mode='r') as f:
        if numbers:
            l =[float(l.replace("\n", "")) for l in f.readlines()]
            return l
        else:
            l =[l.replace("\n", "") for l in f.readlines()]
            return l
    
#Función para pasar url producto y obtener soup parseada    
def get_soup_url(url, headers):
    try:
        web = requests.get(url,headers=headers,timeout=10)

        soup = bs4.BeautifulSoup(web.text, 'html.parser')

        return soup
    except:
        raise Exception("Parece que hay un error con la URL")

#Función para "parar" ejecución    
def sleep_scrap (max_seg=15):
        seg = random.randint(1,max_seg)
        print(f"Esperamos {seg} segundos")    
        time.sleep(seg)
        

##IMPORTANT: you need to set a Gmail account (user), it's password (pwd) and the recipient email adress (recipient)

def send_email(subject, body, user='here_your_account@gmail.com', pwd='here_your_password', recipient='here_recipient_email_adress@gmail.com'):
    
    import smtplib
    from email.mime.text import MIMEText

    msg = MIMEText(body)
    
    msg['Subject'] = subject
    msg['From'] = "Alerta Mediamarkt"
    msg['To'] = recipient


    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, recipient, msg.as_string())
        server.close()
        print('Successfully sent the mail')
    except:
        print('Failed to send mail')
        
#Cargamos los headers, podríamos utilizar cualquier 
headers_list = [{"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"},
               {"User-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"},
               {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"}]

url_list = read_file('products.txt')

price_list = read_file('prices.txt', numbers=True)

print(price_list)

for i, url in enumerate(url_list):
       
    product_data = []
    
    date_time = datetime.datetime.now(datetime.timezone.utc)
    
    headers = random.choice(headers_list)
    
    print(f"\n\nEmpezamos a escrapear el producto {i+1}")
    
    sleep_scrap ()
    
    try:
        soup = get_soup_url(url, headers)
        
        print(f"Descargada la información de {i+1}")
        
        producto = soup.find('div', attrs={'id':'product-details'})

        product_data.append(producto.find('h1', attrs={'itemprop':'name'}).text)
        
        try:
            product_data.append(float(producto.find('meta', attrs={'itemprop':'price'}).get('content')))
            product_data.append(date_time)
            print(product_data[0])
            
            if product_data[1]<=price_list[i]:
                #Preparamos información a enviar:
                producto = product_data[0]
                discount = round((price_list[i]-product_data[1])/product_data[1]*-100,1)
                subject=f"Alerta bajada de precio: {producto}"
                body=f"""\nEl producto {producto} está un {discount}% por debajo de tu alerta.\n\nVisita la siguiente url para comprar: {url}"""
                
                #Enviamos email con la información:
                send_email(subject=subject, body=body)
            
            else:
                print("El precio del producto es superior al de la alerta")
            
        except:
            agotado = soup.find('span', attrs={'class':'offline-text'})
            
            if agotado != None:
                print("El producto está agotado")
                
            else:
                print(f"Revisa la url del producto {i}")
        
    except:
        print(f"Verifica la URL del producto {i+1}")        