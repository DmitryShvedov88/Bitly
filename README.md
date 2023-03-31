#Bitly URL shortener
This application is designed to create short links through the bitly service. You just need to enter your link and the program will return a short one.
It is also possible to check how many times a short link was accessed. To do this, give a short link to the program input and get a response.
Run the program in the terminal and enter either a link or a short link and get the desired result.
###How to install
Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies.
You should have TOKEN for autorisation.
Environment variables:
from requests.exceptions import MissingSchema
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
###pip install -r requirements.txt
Project Goals
This code was written for educational purposes as part of an online course for web developers at dvmn.org.