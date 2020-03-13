Trenton Lyke
3/13/2020
Happy_Smile_Bot 1.0.0

Purpose:
I wanted to make a project that could be used to make people happy.

Goals:
For this project, I decided to make a Twitter bot out of my Raspberry Pi that could be controlled remotely using Node.js. I also decided to add additional features that went along with the bot’s name Happy_Smile_Bot. These features included smile detection and LEDs that could be controlled to light up a smile.

Capabilities:
The twitter bot can tweet out random compliments and reply to its mentions that contain #complimentme with a random compliment periodically, stating what it is tweeting or replying out loud as well. The Raspberry Pi can also detect smiles and light up LEDs in the shape of a smile when smiles are detected. The Raspberry Pi can also light up the LED’s with a smile and say that it is smiling.

Necessary Hardware:
USB Webcam
Speaker with 3.5 mm audio connector
Bread board
2 male to female wires
14 male to male wires
7 LEDs
Microusb charger
Hotspot/Ethernet cord

Software:
Node.js
Python Libraries
Twitter API - tweepy
Facial/Smile Recognition OpenCV - cv2/numpy
LED Control - gpiozero (LED)
Text to Speech - pygame (mixer)/gtts/tempfile
Retrieving compliments from Complimentr.com/api - json/requests
Periodic code execution - time

Directions:
Plug the Raspberry Pi in.
Connect the webcam into a usb port
Connect the speaker into the 3.5 mm audio jack
Connect your female end of your ground female to male wire into the outside gpio pin in row 3 and connect the male end into the negative strip on the outside of the bread board.
Connect your the female end of your other female to male wire into the outside gpio pin in row 6 (i.e. pin 18) and connect the male end into the positive strip on the outside of the bread board.
Stick LED’s in the board longer ends (positive side of LED) facing towards the top of the bread board, making sure that no ends of the LEDs are in the same row going across the bread board. 
Then plug one end of male to male wires into the negative strip that the original male to female wire was plugged into and plug the other ends into each row that contains the short pin of the LED. 
Then plug one end of male to male wires into the positive strip that the original male to female wire was plugged into and plug the other ends into each row that contains the long pin of the LED. 
Next connect your computer with a hotspot or ethernet cord and ssh into the Raspberry Pi.
Username: pi
Password: Lyke5005166
Open up terminal enter: cd QuarterProject
Then enter ifconfig to determine the ip address of the Raspberry Pi on the shared network of it and the computer
Then enter: nodemon index.js
Finally type the ip address of the Raspberry Pi on the shared network of it and the computer into a web browser followed by :3000.
You will now see a webpage that you can use to interact with the Raspberry Pi.

Learning:
I learned a lot about python and how to access APIs which was very new to me. Now that I have learned how to access them, I feel like I can make so many more cool things with python. I also learned how to use gpio pins with python which was very cool for controlling LEDs. Nevertheless, the most enjoyable thing that I learned was how to do smile recognition with cv2.

Experience:
Starting out with the Raspberry Pi, the APIs, and the general python on the Raspberry Pi was very difficult because a lot of the tutorials were outdated. So in the end I had to make most of my own code relying on stack overflow mostly other than adapting things from older videos. As time progressed though, I began to feel much more comfortable working with the Raspberry Pi and became very efficient and creative with my ideas.

Sources:
https://stackoverflow.com/
https://www.youtube.com/
https://www.youtube.com/watch?v=88HdqNDQsEk
https://www.youtube.com/watch?v=W0wWwglE1Vc
https://www.youtube.com/watch?v=_Q8wtPCyMdo
https://www.raspberrypi.org/forums


