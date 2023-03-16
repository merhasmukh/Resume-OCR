import spacy
from spacy.matcher import Matcher

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# initialize matcher with a vocab
matcher_1= Matcher(nlp.vocab)
matcher_2= Matcher(nlp.vocab)


def extract_number(resume_text):
    try:
        nlp_text = nlp(resume_text)

        # First name and Last name are always Proper Nouns
        # pattern = [{'LIKE_NUM': True},
        #    {'IS_DIGIT': True}]
        pattern= [[{'IS_DIGIT': True, 'LENGTH': 10}],[{'IS_DIGIT': True, 'LENGTH': 5},{'SHAPE': '-'},{'IS_DIGIT': True, 'LENGTH': 5}]]
        # pattern= [{'IS_DIGIT': True, 'LENGTH': 10} or {'LIKE_NUM': True,'IS_DIGIT': True} or [{'IS_DIGIT': True, 'LIKE_NUM': True, 'LENGTH': 5},{'SHAPE': '-'},{'IS_DIGIT': True, 'LIKE_NUM': True, 'LENGTH': 5}]]
        
       
        matcher_1.add('Mobile Number:',pattern)

        matches_1= matcher_1(nlp_text)
        print(matcher_1)
        for match_id, start, end in matches_1:
            print(start,end)
            span = nlp_text[start:end]
            if span.text != None:
                print("span1",span)
                return span.text
           

    except Exception as e:
       return str(e),500

# name = extract_name(text)
# print(name)