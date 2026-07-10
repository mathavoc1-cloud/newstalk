from trafilatura import fetch_url, extract
from gtts import gTTS
from playsound3 import playsound



def extract_text(url):
    html = fetch_url(url)

    if html is None:
        return "Sorry! We couldn't extract the text."
    
    text = extract(html, include_comments=False, include_tables=False)

    if text is None:
        return "Sorry! We couldn't extract the text."
    else:
        return text
    


def read_text(text):
    tts = gTTS(text=text, lang="en")
    tts.save("new.mp3")
    playsound("new.mp3")
    
text = extract_text('https://akitaonrails.com/en/2026/06/24/why-llms-will-fail-at-your-company/')
read_text(text)