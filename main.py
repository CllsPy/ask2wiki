import spacy
import wikipedia
#import en_core_web_sm
import streamlit as st

with st.sidebar:
	st.markdown("## ASK2WIKI")
	st.markdown("""
 			An app that uses spaCy to answer questions 
			    by extracting relevant information from Wikipedia articles for quick, 
			    accurate responses.""")

	st.markdown("---")
	st.markdown("made by [CLL](https://github.com/)")
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

st.button("ASK", type="primary")
if st.button:
	answer = ask2wiki(doc)
	st.markdown(f'*{answer}*')
