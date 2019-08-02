import requests

apikey = "AIzaSyBmlR7SUTV9tStVasjd3JhfT6rJ5gg2YCY"

#address = "chase banks near 800 east 180th street"

def sepAddressIntoQuery(address):
    splitString = address.split(' ')
    queryString = ""
    for element in splitString:
        queryString = queryString + element + "+"
    queryString = queryString[0:len(queryString)-1]
    return queryString


def returnBankAddress(theirAddress, bankName):
    address = bankName + " banks near " + theirAddress
    locationQuery = sepAddressIntoQuery(address)
    
    theirQuery = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={locationQuery}&key={apikey}"
    
    #print(requests.get(theirQuery).json())
    theRequest = requests.get(theirQuery).json()
    print(theRequest['results'][0]['formatted_address'])
    return (theRequest['results'][0]['formatted_address']))
 