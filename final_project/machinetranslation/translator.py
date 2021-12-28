"""
Provide IBM Watson based translation services for English / French
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

TR_VERSION= "2018-05-01"

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=TR_VERSION, authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translate a string from English to French.
    """
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text =translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translate a string from French to English
    """
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text =translation['translations'][0]['translation']
    return english_text
