# Amazon-Sale-Alert
Sends an email when there is a price drop for a specific item 

## Using 
Run the program in terminal while specefying the URL and the Price

```
python sale.py -s <URL> -p <Price>

```

## Built With

* [smtplib](https://docs.python.org/3/library/smtplib.html) - The library for eamil connection 
* [optparse](https://docs.python.org/2/library/optparse.html) - The library for getting command line arguments
* [requests](https://2.python-requests.org/en/master/) - To establish connection to the site
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - To parse the html file
