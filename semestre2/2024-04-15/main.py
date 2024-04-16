import requests
import json

def mostra_dicionario(dicionario):
  for key in dicionario.keys():
    if type(dicionario[key]) is dict:
      mostra_dicionario(dicionario[key])
    else:
      print(f"{key}: {dicionario[key]}")
  return

# Twitter API
# url = "https://twitter154.p.rapidapi.com/user/details"

# querystring = {"username":"omarmhaimdat","user_id":"96479162"}

# headers = {
# 	"X-RapidAPI-Key": "515c51b2c6msh9bc958e12541e18p16938ajsnb8bb11a8a05b",
# 	"X-RapidAPI-Host": "twitter154.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)
# response = response.json()

# mostra_dicionario(response)



# Instagram API
# url = "https://instagram120.p.rapidapi.com/api/instagram/get"

# headers = {
# 	"X-RapidAPI-Key": "515c51b2c6msh9bc958e12541e18p16938ajsnb8bb11a8a05b",
# 	"X-RapidAPI-Host": "instagram120.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)
# response = response.json()

# mostra_dicionario(response)
