from flask import Flask, render_template
import os
#bibliotecas: urllib - para manipular as requisições e json - para tratar na tela o resultado que eu vou receber na requisição
import urllib.request, json

#carregar a instância do Flask
app = Flask(__name__)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))  
    app.run(host="0.0.0.0", port=port)

""" - - - FUNÇÕES - - - """
"""Função para pegar os episódios de um personagem"""
def get_character_episodes(episode_urls):
    episodes = []
    
    for url in episode_urls:
        response = urllib.request.urlopen(url)
        episode_data = response.read()
        episode_dict = json.loads(episode_data)
        
        episode = {
            "name": episode_dict["name"],
            "id": episode_dict["id"]
        }
        
        episodes.append(episode)
    
    return episodes

"""Função para pegar os personagens"""
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
            "status": character["status"],
            "episodes" : character["episodes"],
            "origin": character["origin"],
            "location": character["location"]
        }

        characters.append(character)
        
    return {"characters": characters}

"""Função para pegar os dados da url do personagem através da url do episódio"""
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

""" - - - ROTAS - - - """

"""Página inicial"""
@app.route("/")  #rota principal/ página inicial
def get_list_character_page():
    
    #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/character" 
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    data = response.read()
    
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])

"""Personagem específico"""
@app.route("/profile/<id>")  #rota para personagem específico
def get_profile(id):
    
    #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/character/" + id
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    data = response.read()
    
    dict = json.loads(data)
    
    episodes = get_character_episodes(dict["episode"])

    return render_template("profile.html", profile = dict, episodes = episodes)

"""Listagem de personagens em Json"""
@app.route("/lista")
def get_list_characters():
    return get_characters()



"""Listagem de episódios"""
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

"""Episódio específico"""
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

"""Listagem de localizações"""
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
    
"""Localização específica"""
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