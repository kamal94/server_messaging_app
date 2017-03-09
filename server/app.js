var express = require('express');
var app = express();
var fs = require('fs');
var bodyParser = require("body-parser");

// enable accepting parameters in post
app.use(bodyParser.json());

app.get('/', function (req, res) {
	console.log("receiving get request");
	var message_history=
	[
		{
			sender:"Kamal",
			receiver:"Jeremy",
			date:2222222,
			message:"hi!"
		},
		{
			sender:"Jeremy",
			receiver:"Kamal",
			date:2222444,
			message:"Hello back at you!"
		}
	]

  res.send(message_history)
});

app.post('/send', function (req, res) {
	console.log("receiving post requst on /send");
	//save info to history file
	res.send("Okay!");
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
});

"kamalaldin.com/send:3000"
