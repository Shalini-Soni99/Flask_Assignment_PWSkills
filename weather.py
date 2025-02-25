apikey = "47ceca7e65dbc701369208928ba003d6"
url = "https://api.openweathermap.org/data/2.5/weather"

params = { 'q': "delhi",
          'appid': apikey,
          'units': "metric"}

import requests
data = requests.get(url, params = params)

print(data.json())

#Build the app in local
#Push it in git
#Deploy on the cloud
#Test it

