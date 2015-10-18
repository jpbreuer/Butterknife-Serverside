from flask import json
import requests
import urllib
from microsofttranslator import Translator

__author__ = 'Laura'

##'client_id' : 'butterknife'
##'client_secret' : '8DWdIRK0yOdWalb3nLuOreETN0Eekpdo0VMITD3snJU='

API_BINGTRANSLATOR_BASE = 'http://api.microsofttranslator.com/v2/Http.svc/Translate?text='

def translate(text, to_language):
     translator = Translator('butterknife', '8DWdIRK0yOdWalb3nLuOreETN0Eekpdo0VMITD3snJU=')
     from_language = translator.detect_language(text)
     output_text = translator.translate(text, to_language)

     return json.jsonify(original=text, translated=output_text)

