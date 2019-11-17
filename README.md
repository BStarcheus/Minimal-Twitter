# Minimal-Twitter  
Minimal Twitter allows you to stay updated on up to 8 accounts while keeping you off of Twitter itself. Use the program at most once a day. Break the infinite scrolling addiction!

## Requirements  

- python3  
- pip3  
- virtualenv  
- Mac or Linux with bash or zsh shells

## Credentials  

This program uses Twitter API to fetch tweets.  

- [Get a Twitter API Consumer Key, Consumer Secret, Access Token Key, and Access Token Secret](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens)

- Create a file named 'keys.ini' formatted like:  
```
[Default]  
TWITTER_CONSUMER_KEY = YOUR_CONSUMER_KEY
TWITTER_CONSUMER_SECRET = YOUR_CONSUMER_SECRET
TWITTER_ACCESS_TOKEN_KEY = YOUR_ACCESS_TOKEN_KEY
TWITTER_ACCESS_TOKEN_SECRET = YOUR_ACCESS_TOKEN_SECRET
```
and place it in the Minimal-Twitter folder.  

## Configuration and Running  
You can run this program in one of several ways:

1.  Add an alias to your shell profile  
`alias minitw="sh /{ PATH_TO_YOUR_FOLDER }/Minimal-Twitter/bin/minitw"`

2.  Add the bin to your path  
`export PATH="/{ PATH_TO_YOUR_FOLDER }/Minimal-Twitter/bin:${PATH}"`  

In either instance, then simply run the command `minitw` from your command prompt.  

3.  Another alternative is navigating to the project folder each time and running  
`python3 main.py`  
but this will display output from Flask. The first two implementations are more elegant.
