from datetime import datetime, timedelta


def setupAppData():
    '''Get new users to follow and initialize the file'''
    print("Welcome to Minimal Twitter!")
    print("You can stay updated with up to 8 users.")
    print("For @TwitterUser, the username is 'TwitterUser'.")
    print("Enter a username below, or enter '#' to quit.")

    i = 0
    inp = input("Enter username: ")
    f = open('appdata', 'w')

    twodaysago = str(datetime.utcnow() - timedelta(days=2))
    f.write(twodaysago + '\n')

    while i < 8 and inp != '#':
        f.write(inp + '\n')
        inp = input("Enter another username: ")
        i += 1

    f.close()

if __name__ == "__main__":
    setupAppData()
