from flask import Flask, render_template
#bibliotecas: urllib - para manipular as requisições e json - para tratar na tela o resultado que eu vou receber na requisição
import urllib.request, json

#carregar a instância do Flask
app = Flask(__name__)

@app.route("/")  #rota principal/ página inicial
def get_list_character_page():
    
    #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/character" 
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    data = response.read()
    
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])


@app.route("/profile/<id>")  #rota para personagem específico
def get_profile(id):
    
    #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/character/" + id
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    data = response.read()
    
    dict = json.loads(data)

    return render_template("profile.html", profile = dict)

#criar uma rota com a utliização do decorador route, quais urls serão acionadas, que estão disponíveis dentro da aplicação
@app.route("/lista") #rota principal/ página inicial
def get_list_characters():
    
    return get_characters()


def get_characters():
        #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/character" 
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    #criar uma variável para fazer a leitura do resultado
    characters = response.read()
    
    #criar uma variável que vai formatar para um formato json
    dict = json.loads(characters)
    
    characters = []
    
    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        }

        characters.append(character)
        
    return {"characters": characters}

def get_character_urls(character_urls):
    characters = []
    
    for url in character_urls:
        response = urllib.request.urlopen(url)
        character_data = response.read()
        character_dict = json.loads(character_data)
        
        character = {
            "name": character_dict["name"],
            "image": character_dict["image"],
            "id": character_dict["id"]
        }
        
        characters.append(character)
    
    return characters


@app.route("/episodes")  #listagem dos episódios
def get_list_episodes():
    
    #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/episode" 
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    #criar uma variável para fazer a leitura do resultado
    episodes = response.read()
    
    #criar uma variável que vai formatar para um formato json
    dict = json.loads(episodes)
    
    episodes = []
    
    for episode in dict["results"]:
        episode = {
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode" : episode["episode"],
            "url": episode["url"]
        }

        episodes.append(episode)
        
    return render_template("episodes.html", episodes=dict["results"])

@app.route("/episode/<id>")  #rota para episódio específico
def get_episode(id):
    
    #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/episode/" + id
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    data = response.read()
    
    dict = json.loads(data)
    
    characters = get_character_urls(dict["characters"])

    return render_template("episode.html", episode=dict, characters = characters)

@app.route("/locations")  #listagem dos episódios
def get_list_locations():
    
    #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/location" 
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    #criar uma variável para fazer a leitura do resultado
    locations = response.read()
    
    #criar uma variável que vai formatar para um formato json
    dict = json.loads(locations)
    
    locations = []
    
    for location in dict["results"]:
        location = {
            "name": location["name"],
            "type": location["type"],
            "dimension" : location["dimension"]
        }

        locations.append(location)
        
    return render_template("locations.html", locations=dict["results"])
    
    

@app.route("/location/<id>")  #rota para uma localização específica
def get_location(id):
    
    #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/location/" + id
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    data = response.read()
    
    dict = json.loads(data)
    
    residents = get_character_urls(dict["residents"])
        
    return render_template("location.html", location=dict, residents=residents)

#Comando para levantar o servidor local:  flask --app app run