//set up database
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/messages');
var Message = mongoose.model('Message', { user_name: String, chat_room: String, msg:String, date: Date});

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
	return_history(chat_room, res)
	{
		Message.find({ chat_room: chat_room}).exec(function(err, msgs) {
			if(err) console.error("Got an error when loading message history for" + chat_room + err);
			console.log("returning found messages:", msgs);
			res.send(msgs);
		});
	}
}
