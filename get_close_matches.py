from difflib import get_close_matches

user_input = input('Topic ')
Weather:list[str] =['weather','Weather','WEATHER']


Btc:dict[str:str] = {
    'btc':('BTC','Btc','Bitcoin','BITCOIN','bitcoin')
    }

btc_matches:list[str] = [v for v in Btc['btc']]
Topics:list[str] = get_close_matches(user_input, btc_matches, n=5, cutoff=0.6)
if Topics:
    print(Topics[0])

