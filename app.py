import httpsig

from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()

@app.route('/actor')
def actor(request):
	actor_json = {
			"@context": [
				"https://www.w3.org/ns/activitystreams",
				"https://w3id.org/security/v1"
				],

			"id": "https://astraea.systems/activitypub/actor",
			"type": "Person",
			"preferredUsername": "alice",
			"inbox": "https://astraea.systems/activitypub/inbox",

			"publicKey": {
				"id": "https://astraea.systems/activitypub/actor#main-key",
				"owner": "https://astraea.systems/activitypub/actor",
				"publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArxzK7Z7ga5oL/KVLbUK6\nHY9ocvSD0Gr9bb+a3WaRSuS8ULr59Ppktk2l0BHw4pl5vmVoXwv0WeR2/YzYYalZ\nUMv4oV9+akh105UQJcQB52MrRBIgmHxRWI5VtdNRDoL8uMJ6wpAv8Nyu5gRhHfEl\nxMYZ7VxIGXJ2WH1ceOEe8VgOzniWDZxrfCkv7QO4goNy8mzYVMAPqgB2NXfsVRAx\nn+Io3QL5Ndnjq3MXpvgKS7pQKTrW8v8ZLIuw149+nIZcE57g637rR+0JAM61j4qr\nBitOaRjC7vGpXWdOrX/EuyOpwUx4jFI93pRssIJVi3Bs7TyM8A+A0MdbWfxc/LcX\nswIDAQAB\n-----END PUBLIC KEY-----"
				}
			} 

	return JSONResponse(actor_json)

@app.route('/inbox')
def inbox(request):
	return JSONResponse('in inbox')

@app.route('/create-hello-world')
def create_hello_world(request):
  message_json = {
    '@context': 'https://www.w3.org/ns/activitystreams',
    'id': 'https://astraea.systems/create-hello-world'
  }

  secret = open('activitypub/private.pem', 'rb').read()
  print(secret)

  return JSONResponse(message_json)

