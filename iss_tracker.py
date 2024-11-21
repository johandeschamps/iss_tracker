import urllib.request
import json
from datetime import datetime, timezone

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