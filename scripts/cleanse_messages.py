import nltk
import emoji

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('vader_lexicon')
stopwords = set(nltk.corpus.stopwords.words('english'))

def removeMetaData(text):
    # replace "You" with your name
    # replace "Them" with the name of the person your texts are with
    text = text.replace("You: ‎image omitted", "")
    text = text.replace("Them: ‎image omitted", "")
    text = text.replace("You: ‎image omitted", "")
    text = text.replace("Them: ‎image omitted", "")
    text = text.replace("You: ", "")
    text = text.replace("Them: ", "")
    text = text.replace("You: ‎", "")
    text = text.replace("Them: ", "")
    text = text.replace("pm", "")
    text = text.replace("am", "")
    text = text.replace("omitted", "")
    return text

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).
def stripNonAlphaNum(text):
    import re
    # https://stackoverflow.com/questions/6053541/regex-every-non-alphanumeric-character-except-white-space-or-colon
    stripped_text = re.sub('[^\’a-zA-Z\s]', "", text)
    return stripped_text.split()

# Given a list of words, remove any that are
# in a list of stop words.
def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

def performStemming(wordlist):
    ps = nltk.stem.porter.PorterStemmer()
    stemmed = [ps.stem(word) for word in wordlist]
    return stemmed

def performLemmatization(wordList):
    lm = nltk.stem.WordNetLemmatizer()
    lemmized = [lm.lemmatize(word) for word in wordList]
    return lemmized
