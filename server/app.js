var express = require('express');
var app = express();
var fs = require('fs');
var bodyParser = require("body-parser");
var database_handler = require("./database_handler");

// enable accepting parameters in post
app.use(bodyParser.json());

app.get('/', function (req, res) {
	console.log("receiving get request");
	since_minutes = req.body.since_minutes;
	chat_room = req.body.chat_room;

	//handle no minute request
	if (since_minutes == undefined)
	{
		since_minutes = 5;
	}
	//handle no char room
	if (chat_room == undefined)
	{
		chat_room = "general";
	}

	//get message history
	message_history = database_handler.return_history(chat_room, since_minutes, res);
});

app.post('/send', function (req, res) {
	console.log("receiving post requst on /send");
	console.log(req.body);
	var user_name = req.body.user_name
	var chat_room = req.body.chat_room
	var msg = req.body.message
	message_object = { user_name: user_name, chat_room:chat_room, date:new Date(), msg:msg}

	//save message into database
	database_handler.save_message(message_object);

	res.send("Okay!");
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
});

"kamalaldin.com/send:3000"
