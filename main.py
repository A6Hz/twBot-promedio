import tweepy
import re 
import datetime
import time
try:
    from credentials import *
except:
    from os import environ

    consumer_key = environ['CONSUMER_KEY']
    consumer_secret = environ['CONSUMER_SECRET']
    access_token = environ['ACCESS_TOKEN']
    access_token_secret = environ['ACCESS_SECRET']

# tweet every 6 hours
INTERVAL = 60 * 60 * 6  
#INTERVAL = 60  # every 60 seconds, for testing
 
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
#tweets = api.user_timeline(screen_name=username) 


def parse_dolartoday(usr):
    print("parse", usr)
    
    string = api.get_user(usr)
    string = string.description

    valor = re.search("cotiza.*?y", string)
    valor = valor.group().replace(" ", "")
    valor = valor.replace("cotizaaBs.", "").replace("y", "")
    print("=>", valor)
    return valor
    

def parse_DolarTrue(usr):
    print("parse", usr)
    specialChar = ["⬇", "⬇", "⬆"]
    tweets = get_last_tweets(usr)
    for tweet in tweets:
        
        # get last tweet whit the current value of $ 
        if(re.search("#DolarTrue", tweet )):
            valor = tweet.replace(" ", "").lower()
            valor = re.search("dolaren.*", valor)
            valor = valor.group().replace("dolarenbss:", "")
            
            for char in specialChar:
                valor = valor.replace(char, "")

            break
    print("=>", valor)
    return valor



def parse_BolivarCucuta(usr):
    print("parse", usr)
    tweets = get_last_tweets(usr)

    for tweet in tweets:
        if(re.search("Indicadores", tweet)):
            valor = tweet.replace("\n", "")
            valor = re.search("DOLAR EN FRONTERA.*?Bs", valor)
            valor = valor.group().replace("DOLAR EN FRONTERA", "").replace(" Bs", "")
            break
    print("=>", valor)
    return valor


def parse_Theairtm(usr):
    print("parse", usr)
    tweets = get_last_tweets(usr)

    for tweet in tweets:
        if(re.search("Tasa #Airtm", tweet)):
            valor = tweet.replace("\n", "")
            valor = re.search("Tasa #Airtm.*? Bs.S", valor).group()
            valor = valor.replace(" ", "").replace("Tasa#Airtm", "").replace("Bs.S", "")
            break
    print("=>", valor)
    return valor

#ERRROR AL OBTENER EL TWEET. NO ASIGANA VALOR A LA VARIABLE VALOR
def parse_Cotizaciones_(usr): 
    print("parse", usr)
    tweets = get_last_tweets(usr)
    
    for tweet in tweets:
        tweet = tweet.lower().replace(" ", "")
        
        if(re.search("1dolarcopportransferencia", tweet)):
            valor = re.search("=.*?#", tweet).group(0)
            valor = valor.replace("=", "").replace("#", "")
            break
    print("=>", valor)
    return valor
        

def get_last_tweets(usr):
    tweets = api.user_timeline(
        screen_name=usr,
        tweet_mode="extended",
        count = 20
    )

    aux = [tweet.full_text for tweet in tweets]
    return aux



def start():



    valor = {
        "DolarToday": "0.0",
        "DolarTrue_": "0.0",
        "BolivarCucuta": "0.0",
        "Theairtm": "0.0",
        "Cotizaciones_": "0.0",
    }

    # dolartoday 
    valor["DolarToday"] = parse_dolartoday("DolarToday")

    # DolarTrue_
    valor["DolarTrue_"] = parse_DolarTrue("DolarTrue_")
    
    # BolivarCucuta
    valor["BolivarCucuta"] = parse_BolivarCucuta("BolivarCucuta")
    
    # Theairtm
    valor["Theairtm"] = parse_Theairtm("Theairtm")

    # Cotizaciones_   
    valor["Cotizaciones_"] = parse_Cotizaciones_("Cotizaciones_")
    
    
    # promediar.. 
    aux = 0
    valorCuentas = ""
    for key, val in valor.items():
        valRem = val.replace(",", ".")
        aux += float(valRem)
        valorCuentas = valorCuentas + "☑️ " + key + " => " + valRem +".\n" 
    
    valorFinal = aux/len(valor)
    
    tweet = """⛔️ Proof of concept only! ⛔️\n🔴 Valor promedio del dolar es de: %s. 🔴\nCuentas:\n%s\n%s""" % (round(valorFinal,2), valorCuentas, datetime.datetime.now())
    
    api.update_status(tweet)
    print(valor)
    



def main():

    while True:
        print("\n","====| Proceso iniciado", "\n")
        start()
        time.sleep(INTERVAL)

main()