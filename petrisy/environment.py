class Color(object):
    #         R    G    B
    WHITE = (255, 255, 255)
    GRAY = (185, 185, 185)
    BLACK = (0, 0, 0)
    RED = (155, 0, 0)
    GREEN = (0, 155, 0)
    BLUE = (0, 0, 155)
    YELLOW = (155, 155, 0)

    @staticmethod
    def change_color(color, value):
        def add(c, v):
            return c + v if c + v <= 255 else 255

        def sub(c, v):
            return c + v if c + v >= 0 else 0

        f = add if value >= 0 else sub
        r, g, b = f(color[0], value), f(color[1], value), f(color[2], value)
        return r, g, b


class JapaneseColor(object):
    class REDS(object):
        SUOU = (158, 61, 163)
        ENJI = (185, 64, 71)

    class GREENS(object):
        MACCHA = (197, 197, 106)
        WAKATAKE = (104, 190, 141)

    class BLUES(object):
        RURI = (0, 92, 175)
        CONPEKI = (0, 123, 187)

    class YELLOWS(object):
        HABA = (251, 210, 107)
        KIHADA = (254, 242, 99)
        KANZOU = (248, 184, 98)

    class WHITES(object):
        GEPPAKU = (234, 244, 252)
        SHIRONERI = (243, 243, 242)

    class BLACKS(object):
        SHIKKOKU = (13, 0, 21)
        KARASUBA = (24, 6, 20)


# yapf: disable
class Template(object):
    TEMPLATEWIDTH = 5
    TEMPLATEHEIGHT = 5
    BLANK = '.'
    S_SHAPE_TEMPLATE = [['.....',
                         '.....',
                         '..OO.',
                         '.OO..',
                         '.....'],
                        ['.....',
                         '..O..',
                         '..OO.',
                         '...O.',
                         '.....']]

    Z_SHAPE_TEMPLATE = [['.....',
                         '.....',
                         '.OO..',
                         '..OO.',
                         '.....'],
                        ['.....',
                         '..O..',
                         '.OO..',
                         '.O...',
                         '.....']]

    I_SHAPE_TEMPLATE = [['..O..',
                         '..O..',
                         '..O..',
                         '..O..',
                         '.....'],
                        ['.....',
                         '.....',
                         'OOOO.',
                         '.....',
                         '.....']]

    O_SHAPE_TEMPLATE = [['.....',
                         '.....',
                         '.OO..',
                         '.OO..',
                         '.....']]

    J_SHAPE_TEMPLATE = [['.....',
                         '.O...',
                         '.OOO.',
                         '.....',
                         '.....'],
                        ['.....',
                         '..OO.',
                         '..O..',
                         '..O..',
                         '.....'],
                        ['.....',
                         '.....',
                         '.OOO.',
                         '...O.',
                         '.....'],
                        ['.....',
                         '..O..',
                         '..O..',
                         '.OO..',
                         '.....']]

    L_SHAPE_TEMPLATE = [['.....',
                         '...O.',
                         '.OOO.',
                         '.....',
                         '.....'],
                        ['.....',
                         '..O..',
                         '..O..',
                         '..OO.',
                         '.....'],
                        ['.....',
                         '.....',
                         '.OOO.',
                         '.O...',
                         '.....'],
                        ['.....',
                         '.OO..',
                         '..O..',
                         '..O..',
                         '.....']]

    T_SHAPE_TEMPLATE = [['.....',
                         '..O..',
                         '.OOO.',
                         '.....',
                         '.....'],
                        ['.....',
                         '..O..',
                         '..OO.',
                         '..O..',
                         '.....'],
                        ['.....',
                         '.....',
                         '.OOO.',
                         '..O..',
                         '.....'],
                        ['.....',
                         '..O..',
                         '.OO..',
                         '..O..',
                         '.....']]
    # yapf: enable
    PIECES = {'S': S_SHAPE_TEMPLATE,
              'Z': Z_SHAPE_TEMPLATE,
              'J': J_SHAPE_TEMPLATE,
              'L': L_SHAPE_TEMPLATE,
              'I': I_SHAPE_TEMPLATE,
              'O': O_SHAPE_TEMPLATE,
              'T': T_SHAPE_TEMPLATE}
