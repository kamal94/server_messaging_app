from urllib.parse import urlencode
from urllib.request import Request, urlopen
from ast import literal_eval
import json
import time
import requests

def send_message():
	sender = input("Please enter your name: ")
	while True:
		chat_room = input("What chat room would you like to enter? ")
		print("Type 'Exit' to quit the app.\nType 'Switch' to switch chat rooms. ")
		while True:
			date = time.strftime("%c")
			message = input("Write your message: ")
			message_info = {"sender": sender, "chat_room": chat_room, "date": date, "message": message}
			post_message(message_info)
			if message == 'Switch':
				break
			if message == 'Exit':
				return 1
		print (list)
	return 1

def post_message(message_info, url_post="http://kamalaldin.com:3000/send"):
	requests.post(url_post, json = message_info)
	
def get_messages(url_get="http://kamalaldin.com:3000", chat_room="Testing", since_minutes=5):
	message_info = requests.get(url_get, json={"chat_room":chat_room, since_minutes: since_minutes}).json()
	return message_info

def show_messages(message_info_list):
	for message_info in message_info_list:
		print(message_info)

# post_message(get_message_info())
# show_messages(get_messages())
print(get_messages())