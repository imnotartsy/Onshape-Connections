from onshape_client.client import Client

def openApi():
	### Finding a file named api-key within this directory and setting key and secret for setting up the client 
	with open("api-key", "r") as f: 
		key = f.readline().rstrip()
		secret = f.readline().rstrip()

	# MODIFY THIS IF YOU WANT cad.onshape.com, don't forget to modify key and secret as well
	base_url = "https://rogers.onshape.com"

	# Setting up the client
	client = Client(configuration={"base_url": base_url, "access_key": key, "secret_key": secret})
	headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}

	## TODO:
	# hit api and check if did, wid, and eid are valid
