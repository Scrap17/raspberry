import pygame

def init():
    pygame.init()


def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = str(pygame.key.get_pressed())
    myKey = getattr(pygame, 'K_{}', format(keyName))
    if keyInput [myKey]:
        ans = True

    return ans

def main():
    if getKey('a'):
        print('Key a was pressed')
    if getKey('b'):
        print('Key b was pressed')

if __name__ == "__main__":
    init()
    while True:
        main()
