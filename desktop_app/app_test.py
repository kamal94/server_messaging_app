from urllib.parse import urlencode
from urllib.request import Request, urlopen
from ast import literal_eval
import requests
import json
import time

def get_message_info():
	list= [];
	y_n = 'y';
	sender = input("Please enter your name: ")
	while y_n == 'y':
		receiver = input("Who would you like to send your message to? ")
		date = time.strftime("%c")
		message = input("Write your message: ")
		y_n = input("Send another message? (y/n)")
		message_info = {"sender": sender, "receiver": receiver, "date": date, "message": message}
		list.append(message_info)
	print (list)
	return list

def post_message(message_info, url_post="http://kamalaldin.com/send:3000"):
	requests.post(url_post, json = message_info)
	
def get_messages(url_get="http://kamalaldin.com:3000"):
	message_info = requests.get(url_get).json()
	return message_info

def show_messages(message_info_list):
	for message_info in message_info_list:
		print(message_info)
		# Add formatting here

#ost_message(get_message_info())
#show_messages(get_messages())
get_messages()