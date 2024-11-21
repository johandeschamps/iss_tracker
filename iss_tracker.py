import urllib.request
import json
from datetime import datetime, timezone
import requests

req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
response = urllib.request.urlopen(req)

obj = json.loads(response.read())

# Convertir le timestamp en format lisible avec timezone-aware objects
timestamp = obj['timestamp']
readable_time = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

# Affichage formaté
print(f"L'heure actuelle est : {readable_time}")
print(f"La latitude de l'ISS est : {obj['iss_position']['latitude']}")
print(f"La longitude de l'ISS est : {obj['iss_position']['longitude']}")

# Récupérer les données des occupants de la station
response = requests.get("http://api.open-notify.org/astros.json")
if response.status_code == 200:
    data = response.json()
    num_people = data["number"]
    people = data["people"]

    # Afficher le nombre d'occupants
    print(f"Il y a actuellement {num_people} personnes à bord de la Station Spatiale Internationale :")

    # Afficher les noms des occupants
    for person in people:
        print(f"- {person['name']} ({person['craft']})")
else:
    print("Échec de la récupération des données.")