import requests


def translate(text):
    params = {
        "key": "trnsl.1.1.20200416T214531Z.bdff3bd117c49cd3.1690a9c200aacd144ce086fdc12c96757d5de6c0",
        "text": text,
        "lang": 'en-ru'
    }
    response = requests.get(
        "https://translate.yandex.net/api/v1.5/tr.json/translate",
        params=params
    )
    return ''.join(response.json()["text"])


lines = list()
with open("text_4.txt") as file:
    for line in file:
        original_word = line.split()[0]
        translated_word = line.replace(original_word, translate(original_word))
        lines.append(translated_word)

with open("text_4_new.txt", "w") as file:
    file.writelines(lines)

