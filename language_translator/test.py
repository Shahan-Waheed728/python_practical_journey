
from deep_translator import GoogleTranslator

text = "I love learning programming."

for language in ["ur", "hi", "fr"]:
    translated = GoogleTranslator(
        source="en",
        target=language
    ).translate(text)

    print(f"{language}: {translated}")
