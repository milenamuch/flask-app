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

    return render_template("profile.html", profile=dict)

#criar uma rota com a utliização do decorador route, quais urls serão acionadas, que estão disponíveis dentro da aplicação
@app.route("/lista") #rota principal/ página inicial
def get_list_characters():
    
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
            "episode" : episode["episode"]
        }

        episodes.append(episode)
        
    return render_template("episodes.html", episodes=dict["results"])



#Comando para levantar o servidor local:  flask --app app run