import pandas as pd
import requests
# from geopy.distance import geodesic
import re # regex
import json


with open('config.json') as json_file:
    data = json.load(json_file)

key = data['googleKey']

googleUrl = 'https://maps.googleapis.com/maps/api/geocode/json?address='


def queryAddress(addr):
    response = requests.get(googleUrl + addr + '&key=' + key)
    resp_json_payload = response.json()
    try:
        address     = resp_json_payload['results'][0]['formatted_address']
        cep         = re.findall(r"\d+\-\d+", address)
        latitude    = resp_json_payload['results'][0]['geometry']['location']['lat']
        longitude   = resp_json_payload['results'][0]['geometry']['location']['lng']

        if cep == []:
            cep = ['00000-000']
        # end if

        return (cep[0], latitude, longitude)
        
    except IOError as io:
        return ('IO Error', io)
    except ValueError as ve:
        return ("Value Error", ve)
    except ImportError as ie:
        return ("Import Error", ie)
    except EOFError as eof:
        return ("EOF Error", eof)

    except KeyboardInterrupt as ki:
        return ("Keyboard Interrupt", ki)
    except :
        return ('error')
        
    # end try


