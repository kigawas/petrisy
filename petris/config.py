from environment import Color, Template

# color config
BORDERCOLOR = Color.BLUE
BGCOLOR = Color.WHITE
TEXTCOLOR = Color.BLACK
TEXTSHADOWCOLOR = Color.GRAY
COLORS = (Color.BLUE, Color.GREEN, Color.RED, Color.YELLOW)
LIGHTCOLORS = (Color.LIGHTBLUE, Color.LIGHTGREEN, Color.LIGHTRED,
               Color.LIGHTYELLOW)

#Keyboard config
MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

# UI config
FPS = 25
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 20
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = '.'

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5
PIECES = {'S': Template.S_SHAPE_TEMPLATE,
          'Z': Template.Z_SHAPE_TEMPLATE,
          'J': Template.J_SHAPE_TEMPLATE,
          'L': Template.L_SHAPE_TEMPLATE,
          'I': Template.I_SHAPE_TEMPLATE,
          'O': Template.O_SHAPE_TEMPLATE,
          'T': Template.T_SHAPE_TEMPLATE}
