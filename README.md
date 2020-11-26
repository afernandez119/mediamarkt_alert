# Mediamarkt price products alert:

Script for monitoring prices of several products on Mediamarkt.es and get alerted via email

<br>
<center>
<img src="./img/logo.png">
</br>


Part I - published at https://antonio-fernandez-troyano.medium.com/monitorizar-precios-mediamarkt-python-blackfriday-i-95cf6032fbb9

Part II - published at https://antonio-fernandez-troyano.medium.com/monitorizar-precios-mediamarkt-python-pre-blackfriday-parte-ii-70e12ee8c105

Other articles https://antonio-fernandez-troyano.medium.com/

# Data needed for monitoring:
**Product url:** You need to write down the url of the products that you would like to monitoring inside the "products.txt" file

**Price for being alerted:** In addition, you need to include in "prices.txt" file the price from which you would like to be notified via email

# Data needed for email alert:
In order to be notified when the price of a product drops below your target price you need to set up a valid Gmail account with:
- Gmail account (user)
- it's password (pwd) 
- recipient email adress (recipient)

# Where and how to run the script?
It's possible to use:
- Google Cloud Platform services: Cloud Functions + Cloud Scheduler
- Google Cloud Platform services: Compute Engine + Screen
- Raspberry Pi + Cronjob + Screen


*Antonio Fernández Troyano*

<br>
<center>
<img src="./img/profile.png">
</br>
