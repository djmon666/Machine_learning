import requests
import sys


# checks that a custom API key has been provided
def checkApiKey(key):
  if key == "CHANGE THIS TO YOUR PROJECT API KEY":
    print ("Has de posar la teva calu personal API")
    print("Canvia la linia de codi 6 amb la teva APIkey.")
    sys.exit()



#
# This function will train a new ML model using the current 
# training examples in your project
#
#  key - API key - the secret code for your ML project 
#
def trainModel(key):
  checkApiKey(key)
  
  url = ("https://machinelearningforkids.co.uk/api/scratch/" + 
         key + 
         "/models")

  response = requests.post(url)

  if response.ok == False:
    # if something went wrong, display the error
    print (response.json())
    


#
# This function will check the training status of the 
# machine learning model for your project
#
#  key - API key - the secret code for your ML project 
#
def checkModel(key):
  checkApiKey(key)
  
  url = ("https://machinelearningforkids.co.uk/api/scratch/" + 
         key + 
         "/status")

  response = requests.get(url)

  if response.ok:
    responseData = response.json()

    status = {
      2 : "Preparat",
      1 : "L'entrenament està en procés",
      0 : "Problema"
    }

    return { 
      "Estat" : status[responseData["status"]], 
      "Missatge" : responseData["msg"] 
    }
  else:
    # if something went wrong, display the error
    print (response.json())
