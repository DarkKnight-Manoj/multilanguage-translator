import streamlit as st
import numpy as np

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator

api_key='LW18BCIhSE9qjLbPtI1gpVf7e1EYJM5jMVO2c1IbJ7Hw'
url='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/ad732d23-0810-45ed-a137-4a7d37a2f0cd'

authenticator = IAMAuthenticator(apikey=api_key)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

st.title("Language-Translator")

option = st.selectbox('Which language would you choose to type',('English', 'Arabic', 'Hindi', 'German', 'Spanish', 'korean', 'Bengali', 'Dutch', 'French', 'Japanese', 'Urdu'))
if option == 'English':
    option1 = st.selectbox('Which language would you like to translate to',('English', 'Arabic', 'Hindi', 'German', 'Spanish', 'korean', 'Bengali', 'Dutch', 'French', 'Japanese', 'Urdu'))
else:
    option1 = st.selectbox('Only available language to translate ', ['English',])
sent = "Enter the text in "+option+" language in the text-area provided below"

#setting up the dictionary of language to their keywords

language_lib = {'English': 'en', 'Arabic': 'ar', 'Hindi': 'hi', 'Spanish': 'es', 'German': 'de', 'Korean': 'ko', 'Bengali': 'bn', 'Dutch': 'nl', 'French': 'fr', 'Japanese': 'ja', 'Urdu': 'ur'}

sentence = st.text_area(sent, height=250)

if st.button("Translate"):
    try:
        if option == option1:
            st.write("Please Select different language for translation")
        else:
            translate_code = language_lib[option]+'-'+language_lib[option1]

            translation =language_translator.translate(text=sentence, model_id=translate_code)

            ans = translation.get_result()['translations'][0]['translation']

            sent1 = 'Translated text in '+option1+' language is shown below'

            st.markdown(sent1)
            st.write(ans)

    except:
        st.write('Please do cross check if text-area is filled with sentence or not')