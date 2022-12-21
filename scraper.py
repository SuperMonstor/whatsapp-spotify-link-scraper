import re

users = {}
messages = 0
linkfile = open("spotifylinks.txt", "w+")

with open("_chat.txt", encoding="utf8") as file:
    for line in file:
        if line[0] == '[':
            messages += 1
            first_char = line.index(']')
            user = line[first_char+2: first_char+4]

            if user in users:
                users[user] += 1
            else: 
                users[user] = 1
        urls = re.findall(
            r"[\bhttps://open.\b]*spotify[\b.com\b]*[/:]*track[/:]*[A-Za-z0-9?=]+", line
        )
        if len(urls) > 0:
            songurl = urls[0]
            print(songurl)
            startIndex = len(songurl) - songurl[::-1].index('/')
            if('?' in songurl):
                endIndex = songurl.index('?')
                songId = songurl[startIndex: endIndex]
            else: 
                songId = songurl[startIndex: ]
            linkfile.write("spotify:track:" +songId + "\n")

print('total messages: ' +str(messages))
print(users)
linkfile.close()
