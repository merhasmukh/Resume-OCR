import spacy
from spacy.matcher import Matcher
from src.logger import logging
# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)

def extract_name(resume_text):
    try:
        nlp_text = nlp(resume_text)
        
        # First name and Last name are always Proper Nouns
        pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
        
        matcher.add('NAME',[pattern])
        
        matches = matcher(nlp_text)
        
        for match_id, start, end in matches:
            span = nlp_text[start:end]
            return span.text
    except Exception as e:
        logging.info(str(e))


# name = extract_name(text)
# print(name)