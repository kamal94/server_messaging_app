from urllib.parse import urlencode
from urllib.request import Request, urlopen
from ast import literal_eval
import json
import time

def get_message_info():
	sender = input("Please enter your name: ")
	receiver = input("Who would you like to send your message to? ")
	date = time.strftime("%c")
	message = input("Write your message: ")
	message_info = {"sender": sender, "receiver": receiver, "date": date, "message": message}
	return message_info

def post_message(message_info, url_post="http://kamalaldin.com/send:3000"):
	with urlopen(url_post, urlencode(message_info).encode()) as f:
		print(f.read().decode('utf-8'))
	#req = Request(url_post, urlencode(message_info).encode())
	#post = urlopen(req).read().decode()

def get_messages(url_get="http://kamalaldin.com:3000"):
	with urlopen(url_get)as response:
		json_message = response.read().decode("utf-8") 
	message_info = json.loads(json_message)
	return message_info

def show_messages(message_info_list):
	for message_info in message_info_list:
		print(message_info)
		# Add formatting here

post_message(get_message_info())
show_messages(get_messages())