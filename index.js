//requires child module for running bash commands
const { spawn } = require('child_process');
//requires express to create webserver
var express = require('express');
var app = express();


//creates static directories for the webserver to use for the websites
app.use(express.static(__dirname+'/'));
app.use(express.static(__dirname+'/views'));
app.use(express.static(__dirname+'/public'));
app.use(express.static(__dirname+'/JS'));




//has the app listen at port 3000 where the website can be access and 
//runs the background child process for replying to tweets mentioning the 
//bot with the hashtag #complimentme and saying replies outloud
//using previously written python script
app.listen(3000, function(){
    console.log("Listing at port 3000")
    //background reply child process
    const ReplyComplimentTweetForever = spawn('python3', [ 'ReplyComplimentTweetForever.py']);
  ReplyComplimentTweetForever.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  ReplyComplimentTweetForever.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  ReplyComplimentTweetForever.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
  
});

//get request handler that renders the index with buttons to control the bot 
app.get('/',function(req,res){
  res.render("index",{})
});

//post request handler that runs python script in a child process to tweet out 
//a random compliment and say what it is tweeting outloud
app.post('/RandomComplimentTweet',function(req,res){
  const RandomComplimentTweet = spawn('python3', [ 'RandomComplimentTweet.py']);
  console.log("hi")
  RandomComplimentTweet.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  RandomComplimentTweet.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  RandomComplimentTweet.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
  res.send("")
});

//a post request handler that runs a python script in a child process to respond to tweets
//and say them out loud. (deprecated since it now always does this in the background)
app.post('/ReplyComplimentTweet',function(req,res){
  const ReplyComplimentTweet = spawn('python3', [ 'ReplyComplimentTweet.py']);
  ReplyComplimentTweet.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  ReplyComplimentTweet.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  ReplyComplimentTweet.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
  res.send("")
});

//post request handler that runs python script in a child process that turns
//on LEDs to make the bot look lke ts smiling and exclaim thats its simling 
//for 60 seconds
app.post('/Smile',function(req,res){
  const Smile = spawn('python3', [ 'Smile.py']);
  Smile.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  Smile.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  Smile.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
  res.send("")
});


//post request handler that runs python script in a child process that
//detects smiles using a webcam and triggers the LED's to light up
//when it detects a smile
app.post('/DetectSmile',function(req,res){
  const DetectSmile = spawn('python3', [ 'DetectSmile.py']);
  DetectSmile.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  DetectSmile.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  DetectSmile.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
  res.send("")
});
