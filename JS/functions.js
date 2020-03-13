//sends post request that causes the bot to tweet a random compliment
function RandomComplimentTweet(){
	$.post("/RandomComplimentTweet",{},function(){});
}

//sends post request that causes the bot to respond with compliments to tweets 
//mentioning it with the hashtag #complimentme
function ReplyComplimentTweet(){
	$.post("/ReplyComplimentTweet",{},function(){});
}

//sends post request to make bot smile with LEDs and exclaim that it is smiling
function Smile(){
	$.post("/Smile",{},function(){});
}

//sends post request to make bot detect smiles with a webcam and smile when it sees a smile
function DetectSmile(){
	$.post("/DetectSmile",{},function(){});
}
