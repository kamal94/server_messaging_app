from urllib.parse import urlencode
from urllib.request import Request, urlopen
from ast import literal_eval
from multiprocessing import Process
from threading import Thread
import requests
import json
import time
import os

def send_message():
	EXITING = False
	SWITCHING = True
	user_name = input("Please enter your user name: ")
	while not EXITING:
		chat_room = input("What chat room would you like to enter? ")
		SWITCHING = False
		print("Type 'Exit' to quit the app.\nType 'Switch' to switch chat rooms. ")
		while not SWITCHING and not EXITING:
			message = input(user_name + ": ")
			if message == 'Switch':
				SWITCHING = True
			elif message == 'Exit':
				EXITING = True
			else:
				message_info = {"user_name": user_name, "chat_room": chat_room, "message": message}
				post_message(message_info)

	return 1

# Clears the terminal in Mac, Linux, and Windows (I think).
def clear_terminal():
	os.system('cls||clear')


def post_message(message_info, url_post="http://kamalaldin.com:3000/send"):
	requests.post(url_post, json = message_info)
	print("sending", message_info['message'], "in room", message_info['chat_room'])
	
def get_messages(url_get="http://kamalaldin.com:3000"):
	message_info_list = requests.get(url_get).json()
	return message_info_list

def show_messages(message_info_list):
	clear_terminal()
	message_list = get_messages()
	for message_info in message_list:
		print(message_info['user_name'] + ": " + message_info['message'])

def update_messages():
	show_messages(get_messages())
	
if __name__=='__main__':
	clear_terminal()
	p1 = Process(target = get_messages()).start()
	p2 = Process(target = send_message()).start()
