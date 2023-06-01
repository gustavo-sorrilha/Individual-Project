import requests

def tradutorApi(texto):

    url = "https://translate.argosopentech.com/translate"
    
    response = requests.post(url, data={
        "q": texto,
        "source": "en",
        "target": "pt",
    })
    response.raise_for_status()
    return response.json()["translatedText"]

def conselhoApi():
    url = "https://api.adviceslip.com/advice"

    response = requests.get(url)

    if response.status_code == 200:
        conselho = response.json()["slip"]["advice"]
        return conselho
    else:
        return "ERRO"

