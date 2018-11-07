import requests

# Thanks to both this post: https://medium.com/crowdbotics/how-to-build-a-custom-amazon-alexa-skill-step-by-step-my-favorite-chess-player-dcc0edae53fb
# and this repo: https://github.com/serverless/examples/tree/master/aws-python-alexa-skill 
# and this post: https://dzone.com/articles/serverless-and-virtualenv-unable-to-import-module for the tools I needed to build this!

def dadjoke(event, context):
    #print(event)
    url = "https://icanhazdadjoke.com/"
    headers = {'Accept': 'text/plain'}
    dadjoke = requests.get(url, headers=headers)

    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': str(dadjoke.text),
            }
        }
    }

    return response
