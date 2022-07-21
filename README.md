# text-messages
💬 Analysing Facebook and WhatsApp messages to understand messaging habits and language used. 

🛠 built with Python (including pandas and nltk)

📊 visuals created with Tableau

# How to use
 1. Export your Facebook messages. See instructions [here](https://www.facebook.com/help/212802592074644/?ref=u2u).
 2. Export your WhatsApp messages. See "Export chat history" instructions [here](https://faq.whatsapp.com/android/chats/how-to-save-your-chat-history/?lang=en).
 3. Place the files in the `data/raw/` folder. 
 4. Run `scripts/facebook_messages.py` if you have an export of your Facebook messages.
 5. Update `scripts/cleanse_messages.py` with the names of the sender and the receiver. There's no need to run this one.
 6. Run `scripts/combine_message.py`, which will create the final outputs in `data/cleaned/`.
 7. Use the outputs in `data/cleaned/` to analyse the messages. See [screenshots](#screenshots) below for examples.

# Screenshots
![Top 10 emojis](https://github.com/priyalr/text-messages/blob/master/screenshots/Top%2010%20emojis.png)
![Top 10 words](https://github.com/priyalr/text-messages/blob/master/screenshots/Top%2010%20words.png)

<img src="https://github.com/priyalr/text-messages/blob/master/screenshots/Media%202.PNG" width="400" height="398" title="Media">


![Timeline](https://github.com/priyalr/text-messages/blob/master/screenshots/Timeline.PNG)
![Sender analysis](https://github.com/priyalr/text-messages/blob/master/screenshots/Sender%20analysis.PNG)
![Average text length](https://github.com/priyalr/text-messages/blob/master/screenshots/Avg%20text%20length.PNG)
![Hourly texts](https://github.com/priyalr/text-messages/blob/master/screenshots/Hourly%20texts.PNG)
![Hours by days](https://github.com/priyalr/text-messages/blob/master/screenshots/Hours%20by%20days%202.PNG)
![Hours by months](https://github.com/priyalr/text-messages/blob/master/screenshots/Hours%20by%20months%202.PNG)

# License
MIT
