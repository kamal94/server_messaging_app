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
	default_chat_room = "general"
	EXITING = False
	SWITCHING = True
	user_name = input("Please enter your user name: ")
	while not EXITING:
		chat_room = input("What chat room would you like to enter? (general)")
		if chat_room == "":
			chat_room = default_chat_room
		SWITCHING = False
		print("Type 'Exit' to quit the app.\nType 'Switch' to switch chat rooms. ")
		while not SWITCHING and not EXITING:
			message = input(chat_room + " - " + user_name + ": ")
			if (message.replace(" ","") == '') == False:
				if message == 'Switch':
					SWITCHING = True
				elif message == 'Exit':
					EXITING = True
				else:
					message_info = {"user_name": user_name, "chat_room": chat_room, "message": message}
					post_message(message_info)
			update_messages(chat_room)

# Clears the terminal in Mac, Linux, and Windows (I think).
def clear_terminal():
	os.system('cls||clear')

def post_message(message_info, url_post="http://kamalaldin.com:3000/send"):
	requests.post(url_post, json = message_info)
	print("sending", message_info['message'], "in room", message_info['chat_room'])
	
def get_messages(chat_room, url_get="http://kamalaldin.com:3000", since_minutes=5):
	print("Receiving messages in chatroom", chat_room)
	message_info_list = requests.get(url_get, json={"chat_room":chat_room, "since_minutes": since_minutes}).json()
	return message_info_list

def show_messages(message_info_list):
	clear_terminal()
	for message_info in message_info_list:
		print(message_info['chat_room'] + " - " + message_info['user_name'] + ": " + message_info['msg'])

def update_messages(chat_room):
	show_messages(get_messages(chat_room=chat_room))
	
if __name__=='__main__':
	clear_terminal()
	# p1 = Process(target = update_messages()).start()
	p2 = Process(target = send_message()).start()
