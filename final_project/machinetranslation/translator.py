from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(eng_fr_txt):
    if eng_fr_txt == "" or eng_fr_txt is None:
        return "Please enter some text to translate..."
    translation = language_translator.translate(
        text=eng_fr_txt, model_id="en-fr"
    ).get_results
    frenchText = translation["translations"][0]["translation"]
    return frenchText


def french_to_english(fr_eng_txt):
    if fr_eng_txt == "" or fr_eng_txt is None:
        return "Please enter some text to translate..."
    translation = language_translator.translate(
        text=fr_eng_txt, model_id="fr-en"
    ).get_results()
    englishText = translation["translations"][0]["translation"]
    return englishText
