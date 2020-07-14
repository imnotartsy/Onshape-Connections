from onshape_client.client import Client
import argparse 
import base64
import hmac
from datetime import datetime, timezone

# Parse Arguements from the cmdline
parser = argparse.ArgumentParser(description='Onshape API')

parser.add_argument('-d', dest="did", help="Specify a document id (did) for your Onshape workspace")
parser.add_argument('-w', dest="wid", help="Specify a workspace id (wid) for your Onshape workspace")
parser.add_argument('-e', dest="eid", help="Specify an element id (eid) for your Onshape workspace")
parser.add_argument('-b', dest="base", help="Specify a base url your Onshape workspace")

parser.add_argument('-p', dest="port", help="Specify a port for your Spike Prime")

args = parser.parse_args()

# Parse Arguements from file
if (not (args.did and args.wid and args.eid)):
    try:
        with open("document-preferences", "r") as f: 
            args.base = f.readline().rstrip()
            args.did  = f.readline().rstrip()
            args.wid  = f.readline().rstrip()
            args.eid  = f.readline().rstrip()
    except:
        print("All parameters not given. Please give did, wid, and eid using the flags -d, -w, and -e")
        exit()

if (not args.base):
    args.base = "https://rogers.onshape.com"
    print(". . . Defaulting to rogers.onshape.com . . .")

# Gets api key and secret key
with open("api-key", "r") as f: 
    accessKey = f.readline().rstrip()
    secretKey = f.readline().rstrip()

# Setting up the client
client = Client(configuration={"base_url": args.base, "access_key": accessKey, "secret_key": secretKey})
headers = {'Accept': 'application/vnd.onshape.v1+json; charset=UTF-8;qs=0.1', 'Content-Type': 'application/json'}

print(client)
# print(client.__dict__)


# creates path
fixed_url = '/api/assemblies/d/did/w/wid/e/eid'
fixed_url = fixed_url.replace('did', args.did)
fixed_url = fixed_url.replace('wid', args.wid)
fixed_url = fixed_url.replace('eid', args.eid)
url = args.base + fixed_url

# variables
method = "GET"
onNonce = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
authDate = datetime.now(timezone.utc).strftime("%Y%m%d")
content_type = "application/json"
path = fixed_url
queryString = ""

# generate hmac string
hmacString = (method + '\n' + onNonce + '\n' + authDate + '\n' +
  content_type + '\n' + path + '\n' + queryString + '\n').lower();

bitsecretkey = bytearray()
bitsecretkey.extend(map(ord,secretKey))

# string = hmac.new(bitsecretkey, hmacString)

# signature = base64.b64encode(string);

# Auth made!
# asign = 'On ' + accessKey + ':HmacSHA256:' + signature;


print("On-Nonce: ", onNonce)
print("Date: ", authDate)
# print("Authorization: ", asign)


