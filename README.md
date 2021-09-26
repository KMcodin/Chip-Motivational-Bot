Hello and welcome to our team! 
Kevin, Gricelle, and Rogelio makes up the engineering team that brought Chip to life, your personal Motivational Companion. 

# Chip-Motivational-Bot
Chip, your personal Motivational Companion, is here to make you feel better! 
Thanks to Courier's API service, Chip is now able to send you daily motivational text messages! Whoo-hoo!"

## How we built it
We created 1 channel for an email notification and comes with the Google Form attached. Once we have this form filled out by a student or person, we wrote a python script that gets the names and phone numbers of everyone on the Response.csv and puts them in a txt file. Having the names and phone numbers helped us create 4 SMS channels that use this data to send inspirational quotes. Once again, we wrote a python script that with the txt file containing the names and phone numbers, we are able to send one quote to different students at the same time, or different quotes at different times. Python was the main language we used for this project, the team had some knowledge about it but after this project we are confident on the new skills we got.

## Challenges we ran into
The first challenge we ran into was setting up the SMS integration system with twilio. We couldn't get the messages to send when we would move the generated python script by Courier to a .py file in our computer. This was solved by overriding the event name which is the Notification ID for every channel and changing the recipient number for each channel. Next we had trouble retrieving information from an Excel sheet, hence, we decided to use the csv one instead due to our time limitations. Once we were able to send messages to individuals at different times, we wanted to send many messages at the same time, for this we had to add some lines to our python script that would iterate through the txt file with names and phone numbers and it would assign each name to the correct number. The setup for the email integration was very straightforward but we wished it would've let us use a personalized email we created for Chip, we couldn't achieve this so we went with one of our teammates email.

## Accomplishments that we're proud of
We are proud of the project we came up with during this exciting weekend. As first time Shellhackers, and first time ever at a Hackathon, we didn't know what to expect but the documentation available to us online through UPE, Shellhacks and the Sponsors, we were able to see Chip come to life. We are proud of having different channels that make Chip feel not as much as a Bot. We looked for many inspirational quotes that we believe will motivate people that are going through something in life. We are proud of using the google doc form and send it through an email that way if we partnered with a school or organization it would be easier to send to more people. Since the SMS for us feels more personal.

## What we learned
We learned how to implement the Courier API system with our code and add notifications to it. This API made it very easy for us to add that functionality to our code and be able to combine many things into our project. Like sending a google form through the SendGrid integration system, getting the names and numbers from that file and adding them to a txt file that is used by the twilio sms system to reach out to people! Overall, we familiarize ourselves with the Courier API, twilio, and SendGrid, as well as working with new things we hadn't before with Python.

![alt text](https://i.imgur.com/5rrB75C.jpg)
![alt text](https://i.imgur.com/zw5qIxB.jpg)
![alt text](https://i.imgur.com/Jm6e0R1.jpg)
![alt text](https://i.imgur.com/TENezRG.jpg)

## What's next for Chip - Motivational Companion Bot
The next step for chip would be to add a receive messages functionality. So far, it can only distinguish messages about opt-in or out, but the team wants to give Chip the ability to connect with the people that reach out to him in a more personal level. In the meantime we added the National Suicide Prevention Lifeline phone number and chat in case someone needs to talk with a person right away. Once we get Chip to be able to receive messages we would like to create a script that sends the messages automatically once or twice a day at a time between 8am and 9pm.

# Want to recieve messages?
Fill out this Google form and you can be added into Chip's phone book.
https://docs.google.com/forms/d/e/1FAIpQLSefxvj7hlNjCM2f25-lxbpVwIKbYuhAknyXN1s_-7bnv4P4UA/viewform?usp=sf_link

![alt text](https://i.imgur.com/C0gvEgI.jpg)
