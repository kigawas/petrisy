import sys

import pygame
from pygame.locals import QUIT, KEYUP, KEYDOWN, K_ESCAPE


def check_quit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)  # put the other KEYUP event objects back


def check_key_press():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    check_quit()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None


def terminate():
    pygame.quit()
    sys.exit()
