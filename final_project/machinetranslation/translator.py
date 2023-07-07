'''Translator functions for E2F and F2E'''
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    '''Translator functions for E2F'''
    french_text = MyMemoryTranslator(source = "en-US", target = "fr-FR").translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    '''Translator functions for F2E'''
    english_text = MyMemoryTranslator(source = "fr-FR", target = "en-US").translate(french_text)
    print(english_text)
    return english_text
