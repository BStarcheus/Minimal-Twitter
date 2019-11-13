import twitter
from flask import Flask, request
import configparser
from threading import Timer
import requests
import webbrowser


VIEW_TIME = 600

# Get the Twitter API keys from keys.ini
config = configparser.ConfigParser()
config.read('keys.ini')

if len(config['Default']) != 4:
    print("Invalid keys.ini file. Must contain all 4 keys and secrets.")
    exit()

api = twitter.Api(consumer_key=config['Default']['TWITTER_CONSUMER_KEY'],
              consumer_secret=config['Default']['TWITTER_CONSUMER_SECRET'],
              access_token_key=config['Default']['TWITTER_ACCESS_TOKEN_KEY'],
              access_token_secret=config['Default']['TWITTER_ACCESS_TOKEN_SECRET'])

app = Flask(__name__)

@app.route('/')
def generateTweets():
    return "Hello There"

@app.route('/shutdown', methods=['POST'])
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Shutting down."

def shutdown():
    requests.post("http://localhost:5000/shutdown")

def displayPage():
    webbrowser.open("http://localhost:5000")


if __name__ == "__main__":
    Timer(VIEW_TIME, shutdown).start()
    Timer(1, displayPage).start()
    app.run(debug=True)
