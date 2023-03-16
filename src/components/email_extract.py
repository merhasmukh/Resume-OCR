import spacy
from spacy.matcher import Matcher

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)

def extract_email(resume_text):
    try:
        nlp_text = nlp(resume_text)

        # First name and Last name are always Proper Nouns
        pattern = [{'LIKE_EMAIL': True}]

        matcher.add('EMAIL',[pattern])

        matches = matcher(nlp_text)

        for match_id, start, end in matches:
            span = nlp_text[start:end]
            return span.text
    except Exception as e:
       return str(e),500

# name = extract_name(text)
# print(name)