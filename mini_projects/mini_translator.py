from translate import Translator

translator = Translator(to_lang="es")

with open("C:/Users/Tony/Desktop/Random.txt") as file:
    text = file.read()

translation = translator.translate(text)

print(translation)