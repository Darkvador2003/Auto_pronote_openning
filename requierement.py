import os 

print("This script will try to install chromedriver on your machine.\n\
To procede at this installation this programm must be run with root or admin powers.\n")
if os.uname()[0] == 'Linux' :
	os.system("sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install chromedriver")
elif os.uname()[0] == 'Windows':
	print("You can use this link to install properly chromedriver\nhttps://www.kenst.com/2019/02/installing-chromedriver-on-windows/")
else:
	print("You may look on the internet to see how you can install chromedriver")
