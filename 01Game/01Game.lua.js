-- for js (web)
if js ~= nil then
    local js = require "js";
    window = js.global;
    -- document = window.document;
else 
    -- for python or others
    if window == nil then
        window = {};
    end
end

--notify js / python this script is loaded.
window.lua_load = true;

local p1 = true;  -- player1 == human
local p2 = false; -- player2 == computer
local step = 0;
local winner = 0;
local board = {
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    };

window.gameMode = 'Main Menu';
window.keyCode = 0;
window.keyName = '';

function resetBoard()
    step = 0;
    winner = 0;
    board = { 
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
    };
end

function drawChips()
    local dx, dy, ch, pos;
    local c = { 255, 0, 0 }; --RGB

    pos = 1;
    for y = 1, 3 do
        for x = 1, 3 do
            ch = board[ (y-1)*3 + x ];
            if( ch == 1 ) then
                window.drawCircle( x, y );
            end

            if( ch == 2 ) then
                window.drawX( x, y );
            end

            if( ch == 0 ) then
                -- window.drawText( x * 72, y * 72, pos, c );
            end
            pos = pos + 1;
        end --x
    end --y
end -- drawChips()

function checkWin()
    local wintable = { {1,2,3}, {4,5,6}, {7,8,9}, {1,4,7}, {2,5,8}, {3,6,9}, {1,5,9}, {3,5,7} };

    for t = 1, #wintable do
        local p1, p2, p3;
        p1 = wintable[t][1];
        p2 = wintable[t][2];
        p3 = wintable[t][3];

        if( board[p1] ~= 0 ) then
            if( board[p1]==board[p2] and board[p2]==board[p3] ) then
                winner = board[p1];
            end
        end
    end
end

function GameStart()
    window.clearScreen( true );
    local player = (step%2) + 1; -- 1 or 2
    local c1 = { 0, 0, 0 }; --RGB
    local c2 = { 255, 0, 0 }; --RGB

    window.drawBoard();
    --print( 'window.keyName', window.keyName);

    if( winner == 0 ) then
        if( player == 1 ) then
            window.drawText( 100, 10, 'Player1', 0, 0, 0 );
        else
            window.drawText( 100, 10, 'Player2', 0, 0, 0 );
        end
    else
        window.drawText( 100, 10, 'Player' .. winner .. ' WIN !', 255, 0, 0 );
        drawChips();
        return
    end

    if( window.keyName >= '1' and window.keyName <= '9' ) then
        local n = window.keyName + 0;
        -- print( 'found key', n );
        if( board[n] == 0 ) then
            board[n] = player;
            step = step + 1; -- next player
        end
    end
    drawChips();
    checkWin();

    -- window.keyCode 49 / 97 == 1
    -- 50 / 98 == 2
    -- 51 / 99 == 3
    -- 52 / 100 == 4
    -- 53 / 101 == 5
    -- 54 / 102 == 6
    --testDraw()
end --GameStart

function MainMenu()
    --print( 'lua : this is Main Menu', window.keyCode );
    local c = { 0, 0, 255 }; --RGB

    window.clearScreen( true );
    window.drawText( 80, 10, 'Main Menu', 0, 0, 255 ); -- 'Main Menu' width 150px
    window.drawText( 80, 60, 'F1 - P v P', 0, 0, 255 );
    window.drawText( 80, 110, 'ESC = Stop', 0, 0, 255 );
    -- F1 
    if( window.keyCode == 112 ) then
        resetBoard();
        p1 = true; -- player1 == human
        p2 = true; -- player2 == human
        window.gameMode = 'Start';
    end
end --MainMenu

function ginit()
    print( 'ginit - lua init' );
    window.keyName = '';
    window.drawBoard();
end

function gloop()
    if window.gameMode == 'Start' then
        GameStart();
    end

    if( window.keyEsc ) then
        window.gameMode = 'Main Menu';
        -- window:clearScreen( true );
        -- window.quit = true;
    end

    if window.gameMode == 'Main Menu' then
        MainMenu();
    end
end

function testDraw()
    window.drawCircle( 1, 1 );
    window.drawCircle( 1, 2 );
    window.drawCircle( 1, 3 );
    window.drawCircle( 2, 1 );
    window.drawCircle( 2, 2 );
    window.drawCircle( 2, 3 );
    window.drawCircle( 3, 1 );
    window.drawCircle( 3, 2 );
    window.drawCircle( 3, 3 );

    window.drawX( 1, 1 );
    window.drawX( 1, 2 );
    window.drawX( 1, 3 );
    window.drawX( 2, 1 );
    window.drawX( 2, 2 );
    window.drawX( 2, 3 );
    window.drawX( 3, 1 );
    window.drawX( 3, 2 );
    window.drawX( 3, 3 );
end --testDraw()
