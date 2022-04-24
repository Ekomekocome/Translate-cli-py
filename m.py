from kakaotrans import Translator
translator = Translator()
asw = translator.translate(input("masukan text: "), src=input("from: "), tgt=input("target: "))
print(asw)