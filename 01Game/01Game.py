import pygame
import datetime
import math
import lupa
from lupa import LuaRuntime
lua = LuaRuntime(unpack_returned_tuples=True)

# lua_func = lua.eval('loadfile( "./01Game.lua.js") ')
# lua_func();
#same
lua.execute('t = loadfile( "01Game.lua.js") ');
lua.eval('t()');

#global variables
SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;

# global variables for keypress
    # var keyCode = 0;      #lupa direct assign variable.
    # var keyName = '';     #lupa direct assign variable.
    # var keyEsc = false; // 27 #lupa direct assign variable.
gameQuit = False; #quite game

# variables for fps
timeFrame1 = datetime.datetime.now();
frames = 0;
fps = 0;

timeStart = datetime.datetime.now(); #time game start.

#initialise screen.
pygame.init();
pygame.display.set_caption('測試');
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) );
screen.fill( (128, 128, 128) );
clock = pygame.time.Clock();

# you have to call this at the start.
pygame.font.init();
FONT = pygame.font.Font(pygame.font.get_default_font(), 30);
FONT_SIZE = 30;

# variables for draw "#" board
xw = 50;        #//cell width
x1 = 80;        #//left edge
x2 = xw + x1;   #//vertical bar left
x3 = xw + x2;   #//vertical bar right
x4 = xw + x3;   #//right edge

yh = 50         #//cell height
y1 = 100;       #//top edge
y2 = yh + y1;   #//horizontal bar 1
y3 = yh + y2;   #//horizontal bar 2
y4 = yh + y3;   #//bottom edge

# X pos
crossWidth = 30;
crossHeight = 30;
crossX1 = x1 + 10;
crossY1 = y1 + 10;
crossX2 = x2 + 10;
crossY2 = y2 + 10;
crossX3 = x3 + 10;
crossY3 = y3 + 10;

# // O pos
circleRadius = 15;
circleX1 = x1 + xw / 2;
circleX2 = x2 + xw / 2;
circleX3 = x3 + xw / 2;
circleY1 = y1 + yh / 2;
circleY2 = y2 + yh / 2;
circleY3 = y3 + yh / 2;



def testLine():
    # line(surface, color, start_pos, end_pos, width=1) -> Rect
    # if width == 0, (default) fill the circle
    # if width > 0, used for line thickness
    # if width < 0, nothing will be drawn
    pygame.draw.line(screen, (255, 0, 0), (60, 80), (130, 100), 5);
    pygame.draw.circle(screen, "blue", [60, 250], 40, 3);

def testText():
    print( 'default font', pygame.font.get_default_font() );
    # text_surface = FONT.render('text', True, pygame.Color('dodgerblue1'))
    text_surface = FONT.render( 'test', False, (255,0,0) );
    text_rect = text_surface.get_rect();
    text_rect.topleft = [50, 50];
    screen.blit(text_surface, text_rect);

    text_surface2 = FONT.render( 'test', True, (255,0,0) );
    text_rect = text_surface2.get_rect();
    text_rect.topleft = [150, 50];
    screen.blit(text_surface2, text_rect);


# to test how pygame draw.
# testLine();
# testText();
# pygame.display.update();
# input('');
# exit();



def pyClearScreen( clear ) :
    if( clear ):
        screen.fill( (255,255,255) );
    else:
        screen.fill( (0,255,255) );



def pyDrawBoard() :
    pos1x = (x2 - x1) / 2 + x1;
    pos1y = (y2 - y1) / 2 + y1;

    lineWidth = 5;

    # 0 = black
    pygame.draw.line(screen, 0, (x1, y2), (x4, y2), lineWidth);
    pygame.draw.line(screen, (0,0,0), (x1, y3), (x4, y3), lineWidth);

    pygame.draw.line(screen, (0,0,0), (x2, y1), (x2, y4), lineWidth);
    pygame.draw.line(screen, (0,0,0), (x3, y1), (x3, y4), lineWidth);



def pyDrawX( boardX, boardY ) :
    if( boardX == 1 ):
        x1 = crossX1;
    if( boardX == 2 ):
        x1 = crossX2;
    if( boardX == 3 ):
        x1 = crossX3;

    if( boardY == 1 ):
        y1 = crossY1;
    if( boardY == 2 ):
        y1 = crossY2;
    if( boardY == 3 ):
        y1 = crossY3;

    x2 = x1 + crossWidth;
    y2 = y1 + crossHeight;

    pygame.draw.line(screen, (0, 0, 255), (x1, y1), (x2, y2), 5);
    pygame.draw.line(screen, (0, 0, 255), (x2, y1), (x1, y2), 5);



def pyDrawCircle( boardX, boardY ) :
    if( boardX == 1 ):
        x1 = circleX1;
    if( boardX == 2 ):
        x1 = circleX2;
    if( boardX == 3 ):
        x1 = circleX3;

    if( boardY == 1 ):
        y1 = circleY1;
    if( boardY == 2 ):
        y1 = circleY2;
    if( boardY == 3 ):
        y1 = circleY3;

    pygame.draw.circle(screen, "red", [x1, y1], circleRadius, 5)



def pyDrawText( x, y, txt, r, g, b ) :
    # render(text, antialias, color, background=None) -> Surface

    # LUA table start from "1", Python start from "0"

    colour = (r, g, b);

    tmp_text = FONT.render( str(txt), True, colour);
    text_rect = tmp_text.get_rect();
    text_rect.topleft = [x, y];
    screen.blit(tmp_text, text_rect);



def testDraw() :
    pyClearScreen( True );
    pyDrawBoard();

    pyDrawText( 10, 10, 'pyDrawText', 128, 128, 128 );

    pyDrawCircle( 1, 1 );
    pyDrawCircle( 1, 2 );
    pyDrawCircle( 1, 3 );
    pyDrawCircle( 2, 1 );
    pyDrawCircle( 2, 2 );
    pyDrawCircle( 2, 3 );
    pyDrawCircle( 3, 1 );
    pyDrawCircle( 3, 2 );
    pyDrawCircle( 3, 3 );

    pyDrawX( 1, 1 );
    pyDrawX( 1, 2 );
    pyDrawX( 1, 3 );
    pyDrawX( 2, 1 );
    pyDrawX( 2, 2 );
    pyDrawX( 2, 3 );
    pyDrawX( 3, 1 );
    pyDrawX( 3, 2 );
    pyDrawX( 3, 3 );



# map pyfunc to lua
# lua.execute( 'window = {};');
lua_map1 = lua.eval('''
function(f1, f2, f3, f4, f5) 
    window.lua_ginit = ginit;
    window.lua_gloop = gloop;

    window.clearScreen = f1
    window.drawBoard = f2
    window.drawX = f3
    window.drawCircle = f4
    window.drawText = f5;
end
''');
lua_map1( pyClearScreen, pyDrawBoard, pyDrawX, pyDrawCircle, pyDrawText );

def testLuaMap():
    lua.eval( 'window.drawBoard()' );
    lua.eval( 'window.drawCircle(0, 0)' );
    lua.eval( 'window.drawX(0, 0)' );
    pygame.display.update()



# testLuaMap();
# input();
# exit();


# print( 'gameMode', lua.eval( 'window.gameMode' ) );
# lua.execute( 'MainMenu()' );
#
# lua.eval( 'window.lua_ginit()' ); #same
# lua.execute( 'ginit()' ); #same
#
# input();
# exit();


# testDraw()
# pygame.display.update()
# input('');
# exit();



def checkKey():
    global gameQuit;
    keys = pygame.key.get_pressed();

    if keys[pygame.K_F1]:
        lua.execute( 'window.keyCode = 112; window.keyName = ""; ' );
    if keys[pygame.K_1]:
        lua.execute( 'window.keyCode = 0; window.keyName = "1"; ' );
    if keys[pygame.K_2]:
        lua.execute( 'window.keyCode = 0; window.keyName = "2"; ' );
    if keys[pygame.K_3]:
        lua.execute( 'window.keyCode = 0; window.keyName = "3"; ' );
    if keys[pygame.K_4]:
        lua.execute( 'window.keyCode = 0; window.keyName = "4"; ' );
    if keys[pygame.K_5]:
        lua.execute( 'window.keyCode = 0; window.keyName = "5"; ' );
    if keys[pygame.K_6]:
        lua.execute( 'window.keyCode = 0; window.keyName = "6"; ' );
    if keys[pygame.K_7]:
        lua.execute( 'window.keyCode = 0; window.keyName = "7"; ' );
    if keys[pygame.K_8]:
        lua.execute( 'window.keyCode = 0; window.keyName = "8"; ' );
    if keys[pygame.K_9]:
        lua.execute( 'window.keyCode = 0; window.keyName = "9"; ' );

    if keys[pygame.K_ESCAPE]:
        gameQuit = True;
        pygame.QUIT;

    for event in pygame.event.get():
        # print( event );

        if event.type == pygame.KEYDOWN:
            # print( event, event.key, event.scancode );
            pass
        if event.type == pygame.QUIT:
            #user close window
            gameQuit = True;
    #for event
# def checkKey():



# lua.eval( 'window.lua_ginit()' ); #same
# lua.eval( 'ginit()' ); #same
lua.execute( 'ginit()' ); #same

while not gameQuit:
    checkKey();

    if gameQuit :
        pygame.quit();
        exit();

    lua.execute( 'gloop()' );

    frames = frames +1;
    x = datetime.datetime.now() - timeFrame1;
    x = x / 1000;
    if ( x.microseconds >= 1000 ) :
        fps = frames / x.microseconds * 1000;
        timeFrame1 = datetime.datetime.now();
        print( 'fps', f'{fps:0.2f}', 'frames', frames, timeFrame1, x );
        # print( 'window.gameMode', gameMode );
        frames = 0;

    clock.tick(60);
    pygame.display.update();
# while not quit:
