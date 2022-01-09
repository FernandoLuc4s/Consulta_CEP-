import requests
import json
cep="06770200"
consulCep = requests.get("https://cep.awesomeapi.com.br/json/"+cep)
consulCep = consulCep.json()

print(consulCep)


