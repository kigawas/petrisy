import time

from ui import *
from board import *
import pygame.locals as pglocals


def calculate_level_fallfreq(score):
    # Based on the score, return the level the player is on and
    # how many seconds pass until a falling piece falls one space.
    level = int(score / 10) + 1
    fallFreq = 0.8 - (level * 0.02)
    return level, fallFreq


def run():
    # setup variables for the start of the game
    board = get_blank_board()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingDown = False  # note: there is no movingUp variable
    movingLeft = False
    movingRight = False
    score = 0
    level, fallFreq = calculate_level_fallfreq(score)

    fallingPiece = get_new_piece()
    nextPiece = get_new_piece()

    while True:  # game loop
        if fallingPiece == None:
            # No falling piece in play, so start a new piece at the top
            fallingPiece = nextPiece
            nextPiece = get_new_piece()
            lastFallTime = time.time()  # reset lastFallTime

            if not is_valid_position(board, fallingPiece):
                return  # can't fit a new piece on the board, so game over

        check_quit()
        for event in pygame.event.get():  # event handling loop
            if event.type == pglocals.KEYUP:
                if (event.key == pglocals.K_p):
                    # Pausing the game
                    DISPLAYSURF.fill(BGCOLOR)
                    show_text('Paused')  # pause until a key press
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                elif (event.key == pglocals.K_LEFT or
                      event.key == pglocals.K_a):
                    movingLeft = False
                elif (event.key == pglocals.K_RIGHT or
                      event.key == pglocals.K_d):
                    movingRight = False
                elif (event.key == pglocals.K_DOWN or
                      event.key == pglocals.K_s):
                    movingDown = False

            elif event.type == pglocals.KEYDOWN:
                # moving the piece sideways
                if (event.key == pglocals.K_LEFT or
                        event.key == pglocals.K_a) and is_valid_position(
                            board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()

                elif (event.key == pglocals.K_RIGHT or
                      event.key == pglocals.K_d) and is_valid_position(
                          board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()

                # rotating the piece (if there is room to rotate)
                elif (event.key == pglocals.K_UP or event.key == pglocals.K_w):
                    fallingPiece['rotation'] = (
                        fallingPiece['rotation'] +
                        1) % len(PIECES[fallingPiece['shape']])
                    if not is_valid_position(board, fallingPiece):
                        fallingPiece['rotation'] = (
                            fallingPiece['rotation'] -
                            1) % len(PIECES[fallingPiece['shape']])
                elif (event.key == pglocals.K_q):  # rotate the other direction
                    fallingPiece['rotation'] = (
                        fallingPiece['rotation'] -
                        1) % len(PIECES[fallingPiece['shape']])
                    if not is_valid_position(board, fallingPiece):
                        fallingPiece['rotation'] = (
                            fallingPiece['rotation'] +
                            1) % len(PIECES[fallingPiece['shape']])

                # making the piece fall faster with the down key
                elif (event.key == pglocals.K_DOWN or
                      event.key == pglocals.K_s):
                    movingDown = True
                    if is_valid_position(board, fallingPiece, adjY=1):
                        fallingPiece['y'] += 1
                    lastMoveDownTime = time.time()

                # move the current piece all the way down
                elif event.key == pglocals.K_SPACE:
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not is_valid_position(board, fallingPiece, adjY=i):
                            break
                    fallingPiece['y'] += i - 1

        # handle moving the piece because of user input
        if (movingLeft or movingRight) and time.time(
        ) - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if movingLeft and is_valid_position(board, fallingPiece, adjX=-1):
                fallingPiece['x'] -= 1
            elif movingRight and is_valid_position(
                    board, fallingPiece, adjX=1):
                fallingPiece['x'] += 1
            lastMoveSidewaysTime = time.time()

        if movingDown and time.time(
        ) - lastMoveDownTime > MOVEDOWNFREQ and is_valid_position(
                board, fallingPiece, adjY=1):
            fallingPiece['y'] += 1
            lastMoveDownTime = time.time()

        # let the piece fall if it is time to fall
        if time.time() - lastFallTime > fallFreq:
            # see if the piece has landed
            if not is_valid_position(board, fallingPiece, adjY=1):
                # falling piece has landed, set it on the board
                add_piece(board, fallingPiece)
                score += remove_complete_lines(board)
                level, fallFreq = calculate_level_fallfreq(score)
                fallingPiece = None
            else:
                # piece did not land, just move the piece down
                fallingPiece['y'] += 1
                lastFallTime = time.time()

        # drawing everything on the screen
        DISPLAYSURF.fill(BGCOLOR)

        draw_board(board)
        draw_status(score, level)
        draw_next_piece(nextPiece)
        if fallingPiece is not None:
            draw_piece(fallingPiece)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def main():
    show_text('Petrisy')
    while True:  # game loop
        run()
        show_text('Game Over')

#show_text('AA')
main()
