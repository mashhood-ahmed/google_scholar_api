
from scholarly import scholarly
import json
import jsonpickle
from scholarly import ProxyGenerator

# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)

def fetchPublication(title):
	try:
	    search_query = scholarly.search_pubs(title)
	    data = next(search_query)
	    pubJSON = jsonpickle.encode(data)
	    return pubJSON
	except Exception:
		return jsonpickle.encode({'message': 'No Record Found'})

# publicationJSONData = json.dumps(pubJSON, indent=4)

#print(pubJSON)