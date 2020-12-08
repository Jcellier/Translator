from googletrans import Translator

text = input("Enter the text you want to translate in French: ")

translator = Translator()

lang = translator.detect(text)
# print(lang)

res = translator.translate(text, dest="fr")
print(res.text)