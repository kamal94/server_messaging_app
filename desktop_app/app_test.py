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

def post_message(url, message_info):
	json_message = json.dumps(message_info)
	req = Request(url, urlencode(json_message).encode())
	post = urlopen(req).read().decode()	#unsure about decode()?

def get_message(url):
	json_message = urlopen(url).read().decode("utf-8") 
	message_info = json.load(json_message)
	return message_info

# Converts json (string) into a python dictionary and displays message info
def show_messages(message_info):
	parsed_message = literal_eval(message_info)
	# The rest of this depends on message format upon retrieval

