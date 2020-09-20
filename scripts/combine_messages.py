# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import cleanse_messages # text processing functions
import emoji            # identifying emoji characters
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer # nltk's sentiment analyser suited to social media
import pandas as pd     # data processing, to CSV
import os               # file I/O

# =================================================================
# READ DATA
# =================================================================
# Read in WhatsApp messages
# Replace "WhatsApp 2018-07 to 2020-04.txt" with your file's name
whatsapp_location = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/raw/WhatsApp.txt'))
f = open(whatsapp_location, 'r') # WhatsApp data
chat_log = f.read()
f.close()

# Read in Facebook messages
# Replace "Facebook 2018-07 to 2020-04.txt" with your file's name
facebook_location = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/processed/Facebook.txt'))
f = open(facebook_location, 'r') # Facebook data
chat_log += "\n"
chat_log += f.read()
f.close()

# =================================================================
# TRANSFORM AND CLEANSE DATA
# =================================================================
chat_log = chat_log.splitlines()

# Shift messages on a separate line back to the previous line
# Shifted messages:
#   1. [datetime] sender: messagea
#   2. messageb
#   3. [datetime] sender: messagec
# Ideal format:
#   1. [datetime] sender: messagea messageb
#   2. [datetime] sender: messagec
messages_clean = []
message_string = ""
for line in chat_log:
    try:
        line = line.replace(u"\u200e", "") # remove character before images/links
        # start a new line if it is in the ideal format
        if line[0] == "[":
            messages_clean.append(message_string)
            message_string = ""
            message_string += line
        # if it is shifted, add to the previous line
        else:
            message_string += line
    # ignore blank lines
    except:
        continue

# Initialise
dataset = []    # for messages
emoji_data = [] # for emojis
word_data = []  # for words
media_data = [] # for media
row_id = 0      # counter to assign an ID to messages
vader = SentimentIntensityAnalyzer() # for sentiment scores
for message in messages_clean:
    rowData = []
    row_id += 1
    rowData.append(row_id) # row_id
    rowData.append(message[message.find("[")+1:message.find("]")]) # message_date
    rowData.append(message[message.find("]")+1:message.find(": ")]) # sender
    message_text = message[message.find(": ")+1:].strip()
    rowData.append(message_text) # message_text
    rowData.append(vader.polarity_scores(message_text)['compound']) #vader_score
    rowData.append(len(message_text)) # message_length
    dataset.append(rowData)

    # shared media data
    if 'image omitted' in message_text:
        media_data.append([row_id, 'Image'])
    if 'video omitted' in message_text:
        media_data.append([row_id, 'Video'])
    if 'GIF omitted' in message_text:
        media_data.append([row_id, 'GIF'])
    if 'http' in message_text:
        media_data.append([row_id, 'Link'])

    # emoji data and word data by row
    # list emojis
    for char in message_text:
        if char in emoji.UNICODE_EMOJI:
            emoji_data.append([row_id, char])

    # list cleansed words
    message_text = cleanse_messages.removeMetaData(message_text)                            # remove metadata, e.g. sender name
    message_text = message_text.lower()                                                     # convert everything to lowercase to make grouping the same words easier
    fullwordlist = cleanse_messages.stripNonAlphaNum(message_text)                          # remove non-alphanumeric characters
    wordlist = cleanse_messages.removeStopwords(fullwordlist, cleanse_messages.stopwords)   # remove stopwords, e.g. 'the', 'is', 'are'
    wordlist = cleanse_messages.performLemmatization(wordlist)                              # group different inflected forms, e.g. cars -> car, running -> run
    for oneWord in wordlist:
        # don't include links in the list of words
        if 'http' not in oneWord and '[' not in oneWord:
            word_data.append([row_id, oneWord])

# =================================================================
# EXPORT DATA
# =================================================================
# create headers for messages data and export
cleaned_data_location = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/cleaned/'))

message_df = pd.DataFrame(dataset, columns=[  'RowID'
                                            , 'MessageDateTime'
                                            , 'MessageSender'
                                            , 'MessageText'
                                            , 'VaderScore'
                                            , 'MessageLength'])
message_df.to_csv(os.path.join(cleaned_data_location, 'messages.csv'))

# create headers for words data and export
media_df = pd.DataFrame(media_data, columns=[  'RowID'
                                             , 'Media'])
media_df.to_csv(os.path.join(cleaned_data_location, 'media_df.csv'))


# create headers for emojis data and export
emoji_df = pd.DataFrame(emoji_data, columns=[  'RowID'
                                             , 'Emoji'])
emoji_df.to_csv(os.path.join(cleaned_data_location, 'emoji_df.csv'))

# create headers for words data and export
word_df = pd.DataFrame(word_data, columns=[  'RowID'
                                             , 'Word'])
word_df.to_csv(os.path.join(cleaned_data_location, 'word_df.csv'))

