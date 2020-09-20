# text-messages
💬 Analysing Facebook and WhatsApp messages to understand messaging habits and language used. 

🛠 built with Python

# How to use
 1. Export your Facebook messages. See instructions [here](https://www.facebook.com/help/212802592074644/?ref=u2u).
 2. Export your WhatsApp messages. See "Export chat history" instructions [here](https://faq.whatsapp.com/android/chats/how-to-save-your-chat-history/?lang=en). 
 3. Place the files in the `data/raw` folder.
 4. Run `scripts/facebook_messages.py` if you have an export of your Facebook messages.
 5. Update `scripts/cleanse_messages.py` with the names of the sender and the receiver. No need to run this.
 6. Run `combine_message.py` to create the final outputs in `data/cleaned`.

# Screenshots


# License
MIT
