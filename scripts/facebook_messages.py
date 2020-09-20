# =================================================================
# IMPORT REQUIRED LIBRARIES
# =================================================================
import json, time, os

# =================================================================
# READ DATA
# =================================================================
# Read in Facebook messages
# Replace "Facebook.json" with your file's name
facebook_in_location = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/raw/Facebook.json'))
f = open(facebook_in_location, 'r')
chat_log = f.read()
f.close()

chat_dict = json.loads(chat_log)

# =================================================================
# TRANSFORM AND CLEANSE DATA
# =================================================================
messages = chat_dict['messages']
converted_messages = ''
for aMessage in messages:
    sender = aMessage['sender_name'].split()[0]
    timestamp = time.strftime('%-d/%-m/%y, %-I:%M:%S %p', time.localtime(aMessage['timestamp_ms'] // 1000)).lower()
    messageType = aMessage['type']
    if 'photos' in aMessage:
        content = '‎image omitted'
    elif 'videos' in aMessage:
        content = 'video omitted'
    elif 'gifs' in aMessage:
        content = 'GIF omitted'
    elif 'audio_files' in aMessage:
        content = 'audio omitted'
    elif 'files' in aMessage:
        content = 'file omitted'
    elif 'sticker' in aMessage:
        content = 'sticker omitted'
    elif 'share' in aMessage:
        linkObj = aMessage['share']
        if 'link' in linkObj:
            content = linkObj['link']
        else:
            content = 'location omitted'
    elif 'sent an attachment' in aMessage['content']:
        content = 'file omitted'
    elif 'missed your call' in aMessage['content'] or 'missed a call' in aMessage['content']:
        content = '‎Missed voice call'
    elif 'You called' in aMessage['content'] or 'called you' in aMessage['content']:
        content = 'Voice call'
    elif 'missed your video chat' in aMessage['content'] or 'missed a video chat' in aMessage['content']:
        content = '‎Missed video call'
    else:
        content = aMessage['content'].encode("latin_1").decode()

    messageText = '[' + timestamp + '] ' + sender + ': ' + content + "\n"
    converted_messages += messageText

# =================================================================
# EXPORT DATA
# =================================================================
# Replace "Facebook 2018-07 to 2020-04.txt" with your file's name
facebook_out_location = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/processed/Facebook.txt'))
f = open(facebook_out_location, 'w')
f.write(converted_messages)
f.close()
