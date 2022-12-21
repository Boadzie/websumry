import pycurl
import json
from io import BytesIO
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
from nltk.corpus import stopwords
from typing import Optional, List

# download language models 
nltk.download('punkt')
# download stop words
nltk.download('stopwords')


def get_html(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    return buffer.getvalue().decode('iso-8859-1')


# stopwords
stop_words = set(stopwords.words("english"))

def summarize_website(url:str, num_sentences:int, bonus_words:Optional[List]):
    # Retrieve the HTML of the website
    html = get_html(url)

    # Extract the text from the HTML
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()

    # Preprocess the text (optional)
    text = text.lower()
    text = text.replace("\n", " ")

    # Create a Sumy PlaintextParser object
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Create a Sumy LsaSummarizer object
    summarizer = LsaSummarizer()

    # Set the number of sentences in the summary and the stop and bonus words
    summarizer.stop_words = stop_words
    summarizer.bonus_words = bonus_words

    # Summarize the text
    summary = summarizer(parser.document, num_sentences)

    # Return the summary
    summary_text = ""
    for sentence in summary:
        summary_text += str(sentence) + " "
        
    return summary_text
