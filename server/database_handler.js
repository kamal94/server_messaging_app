//set up database
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/messages');
var Message = mongoose.model('Message', { user_name: String, chat_room: String, msg:String, date: Date});

// define functions to export
module.exports = {
	// expects object { user_name: user_name, chat_room:chat_room, date:new Date(), msg:msg}
	save_message(message_dict)
	{
		var message = new Message({ user_name: message_dict.user_name, chat_room: message_dict.chat_room, date:new Date(), msg:message_dict.msg});
		console.log("saving messsage", message);
		
		message.save(function (err) {
			if (err) {
				console.log(err);
			} else {
				console.log('Message added sucessfully!');
			}
		})
	},

	// returns the chat history of the chat room passed, then sending a json object using 
	// the response object passed
	return_history(chat_room, since_minutes, res)
	{
		since_date = new Date(new Date().getTime() - since_minutes*60000);
		Message.find({ chat_room: chat_room, date :{$gte: new Date().}}).exec(function(err, msgs) {
			if(err) console.error("Got an error when loading message history for" + chat_room + err);
			console.log("returning found messages:", msgs);
			res.send(msgs);
		});
	}
}
