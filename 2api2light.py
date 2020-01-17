import logging
import os
import json
import time

textForDataRetriving = 'curl --header "Access-Token: o.UJdMvQny9onevleSQ9Kj0wZ7b9L1I73s" --data-urlencode active="true" --data-urlencode modified_after="1.4e+09" --get https://api.pushbullet.com/v2/pushes'
textForDataDeleting = 'curl --header "Access-Token: o.UJdMvQny9onevleSQ9Kj0wZ7b9L1I73s" --request DELETE https://api.pushbullet.com/v2/pushes'
run = True

def hesten():
    prejson = os.popen(textForDataRetriving);
    line = prejson.readline()

    notificationJson = json.loads(line)
    messagesFromFlic = notificationJson["pushes"]
    numbersOfMessages = len(messagesFromFlic)
    for x in range(numbersOfMessages):
        #print(messagesFromFlic[x])
        melding = messagesFromFlic[x]
        presstype = melding["body"]
        if(presstype == "My Flic was triggered with a hold action!"):
            reset()


    if (numbersOfMessages < 2):
        # lys gronn
        print("gronn", numbersOfMessages)

    if (numbersOfMessages >= 2 and numbersOfMessages <= 5):
        # lys gul
        print("gul", numbersOfMessages)

    if (numbersOfMessages > 5):
        # lys red and blink
        print("rod", numbersOfMessages)

    time.sleep(2)


def reset():
    os.system(textForDataDeleting)

def main():
    reset()
    while run:
        hesten()





if __name__ == '_main_':
    main()