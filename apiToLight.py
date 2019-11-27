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
        print(messagesFromFlic[x])

    if (numbersOfMessages < 2):
        # lys gronn
        print("gronn")

    if (numbersOfMessages >= 2 and numbersOfMessages <= 5):
        # lys gul
        print("gul")

    if (numbersOfMessages > 5):
        # lys red and blink
        print("rod")

    time.sleep(2)


def reset():
    os.system(textForDataDeleting)

def main():
    while run:
        hesten()





if __name__ == '__main__':
    main()
