import requests

def get_random_word():
    url = 'https://api.dicionario-aberto.net/random'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            word_data = response.json()
            return word_data['word']
        else:
            print(f"Erro ao chamar a API: {response.status_code}")
            return None
    except Exception as e:
        print(f"Erro na solicitação: {e}")
        return None



