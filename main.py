import spacy
import wikipedia
#import en_core_web_sm
import streamlit as st


nlp = spacy.load("en_core_web_sm")

doc_input = st.text_input("Question", placeholder="O que você sabe sobre...")
base = 'What do you know about '
final = base + doc_input
doc = nlp(final)

def ask2wiki(doc):
	for t in doc:
		if t.dep_ == 'pobj' and (t.pos_=='NOUN' or t.pos_=='PROPN'):
			phrase = (''.join([child.text for child in t.lefts]) + '' + t.text).lstrip()

			wiki_resp = wikipedia.page(phrase)
			return ((wikipedia.summary(phrase, sentences=4)))


answer = ask2wiki(doc)
st.write(answer)