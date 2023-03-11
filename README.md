# Embedded-Lua

1. Use Lua for main program logic.
	- Init.
	- Main Loop.
	- Reset Game.


2. For web, use HTML, javascript, canvas.
	- Use fengari (https://fengari.io/) (fengari-web.js) connect between javascript and Lua.
	- Use timer (setInterval) to control refresh speed.
	- Use file.lua.js to avoid extra settings on web server.

	- Use wasmoon (https://github.com/ceifa/wasmoon) (wasmoon.js) (glue.wasm)


3. For desktop, use Python, lupa, pygame.
	- Use lupa (https://pypi.org/project/lupa/) connect between python and lua.
	- Use pygame.time.Clock()	to control refresh speed.


4. js / python will provide function and global variables.
	- clear screen.
	- drawImage / blit image.
	- draw text.
	- load images.
