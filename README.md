# twBot-promedio 

![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)


**Proof of concept** using tweepy to obtain the average value of the dollar as published in several twitter accounts. The accounts from which the information is obtained are: 

> @DolarToday
> @DolarTrue_
> @BolivarCucuta
> @Theairtm
> @Cotizaciones_

## Testing locally 



    git clone https://github.com/Alex143/twBot-promedio.git
    cd twBot-promedio 
    
Now create a credentials.py file whit your consumer_key, access_token, etc. in this folder. 

	consumer_key 		= "xxxxxxxxx"
	consumer_secret 	= "xxxxxxxxx"
	access_token 		= "xxxxxxxxx"
	access_token_secret = "xxxxxxxxx"
 
Then you should be able to run locally. 

    pip3 install -r requirements.txt
    python3 main.py 


Actual bot is running at [@DaemonPurosesu](https://twitter.com/DaemonPurosesu)
