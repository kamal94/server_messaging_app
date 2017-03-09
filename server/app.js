var express = require('express')
var app = express()
var fs = require('fs');

function writeFile(jsonarray)
{
	fs.writeFile(writeSource, "Writing to a file from node.js", {"encoding":'utf8'}, function(err){
		if ( err ) { throw err; }
		console.log("*** File written successfully");
		//Now reading the same file to confirm data written
		fs.readFile(writeSource, "utf8", function(err, data){
		if ( err ){ throw err;}
		console.log("*** Reading just written file");
		console.log(data);
		});
	});
}



app.get('/try', function (req, res) {
	console.log("receiving get request for /try");
	res.send("this is the kamalaldin.com/try page");
})


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
})

app.post('/send', function (req, res) {
	console.log("receiving post requst");
	console.log(req.body);
	var user_id = req.param('sender');
	var token = req.param('receiver');
	var date = req.param('date');  
	var msg = req.param('message');
	//save info to history file
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})

"kamalaldin.com/send:3000"
