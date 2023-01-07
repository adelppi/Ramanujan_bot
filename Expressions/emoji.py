from janome.tokenizer import Tokenizer
from translate import Translator

def emojiReact(cmdInput):
    tokenizer = Tokenizer()
    translator = Translator(from_lang = "ja", to_lang = "en")
    text = cmdInput
    result = []
    for term in tokenizer.tokenize(text):
        if "名詞" in term.part_of_speech:
            result.append(translator.translate(term.surface))
    return result

if __name__ == "__main__":
    print(emojiReact("風呂"))