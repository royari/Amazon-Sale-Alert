import optparse
import requests
from bs4 import beautifulSoup 
import smtplib

URL= "https://www.amazon.in/Generic-Purpose-Melt-Glue-Sticks\
/dp/B01E0QJXWK/ref=sr_1_6?crid=S72R947KTI8N&keywords=glue+gun\
+sticks+11mm&qid=1562789570&s=gateway&sprefix=glue+gun+s%2Caps%2C413&sr=8-6"

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}



def check_price(T_price):

	page=requests.get(URL,headers=headers)

	soup=beautifulSoup(page.content,'html.parser')
	title=soup.find(id="productTitle").get_text()
	price=soup.find(id="priceblock_ourprice").get_text()
	converted_price=float(price[:5])
	if converted_price<T_price:
		send_mail()
	#print(title.strip())

def send_mail():
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login("alpharoy14@gmail.com","password") #add your pass

	subject="price fell down down down"
	Body =f'check the amazon LINK {URL}'

	message=f'subject:{subject}\n\n{Body}'

	server.sendmail(
		'alpharoy14@gmail.com',
		"alpharoy14@gmail.com",
		message

		)
	print("Hey Email Has been sent")
	server.quit()
###sleep(60*60)

def main():
	parser=optparse.OptionParser("usage: %prog" + " -s <site> -p <price>")
	parse.add_option('-p',dest="T_price",type='float',help='specify the price')
	parse.add_option('-s',dest="Site",type='string',help='specify the site')
	(options,args)=parse.parse_args()
	if(options.T_price==None):
		print(parse.usage)
		exit(0)
	else:
		URL=options.Site
		T_price=options.T_price

	while True:
		check_price(T_price)
		sleep(60*60)






