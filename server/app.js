var express = require('express');
var app = express();
var fs = require('fs');
var bodyParser = require("body-parser");
var database_handler = require(".database_handler");

// enable accepting parameters in post
app.use(bodyParser.json());

app.get('/', function (req, res) {
	console.log("receiving get request");
	chat_room = req.body.chat_room;
	message_history = database_handler.return_history(chat_room);
  res.send(message_history)
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
