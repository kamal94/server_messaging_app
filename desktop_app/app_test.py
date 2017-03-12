from urllib.parse import urlencode
from urllib.request import Request, urlopen
from ast import literal_eval
from multiprocessing import Process
from threading import Thread
import requests
import json
import time


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

def post_message(message_info, url_post="http://kamalaldin.com:3000/send"):
	requests.post(url_post, json = message_info)
	print("sending", message_info['message'], "in room", message_info['chat_room'])
	
def get_messages(url_get="http://kamalaldin.com:3000"):
	message_info = requests.get(url_get).json()

def show_messages(message_info_list):
	message_info = get_messages()
	#for message_info in message_info_list:
	print(message_info['user_name'] + ": " + message_info['message'])
	
def hello_world(num):
	while True:
		time.sleep(1)
		print(num)

if __name__=='__main__':
	p1 = Process(target = get_messages()).start()
	p2 = Process(target = send_message()).start()
