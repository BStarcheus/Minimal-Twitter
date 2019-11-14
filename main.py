import twitter
from flask import Flask, request, render_template
import configparser
from threading import Timer
from datetime import datetime
import requests
import webbrowser


def getScreenNames():
    '''Return the list of screen names the user wants to fetch tweets for
    '''
    f = open('appdata', 'r')
    f.readline()
    text = f.readline()
    names = []
    while text and text != '\n':
        names.append(text[:-1])
        text = f.readline()
    return names

def getTweets(user):
    '''Return a list of tweets created since the last run of this program
    limited to 40 tweets per user'''

    results = api.GetUserTimeline(screen_name=user, count=40)
    tweets = []
    lastdate = ""
    # Get the last date this program was run
    with open('appdata', 'r') as f:
        lastdate = str(datetime.strptime(f.readline()[:-1], "%Y-%m-%d %H:%M:%S.%f"))
        f.close()

    # Filter out tweets from before the last run
    for r in results:
        date = str(datetime.strptime(r.created_at, "%a %b %d %H:%M:%S %z %Y"))
        if date < lastdate:
            break
        tweets.append(r)

    # Return the tweets in chronological order
    tweets.reverse()
    return tweets



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
              access_token_secret=config['Default']['TWITTER_ACCESS_TOKEN_SECRET'],
              tweet_mode="extended")


screenNames = getScreenNames()





app = Flask(__name__)

@app.route('/')
def createPage():
    users = {}
    for name in screenNames:
        users[name] = getTweets(name)

    with open('appdata', 'r+') as f:
        f.write(str(datetime.utcnow()))
        f.close()

    return render_template('tweetsummary.html', users=users)

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
    Timer(1, displayPage).start()
    Timer(VIEW_TIME, shutdown).start()
    app.run(debug=True, use_reloader=False)
