# Embedded-Lua
嵌入式-Lua

1. 主要程序使用Lua。
	- 初始化。
	- 主循環。
	- 重置遊戲。

2. 網頁版本，使用 HTML、CSS、canvas。
	- 使用 fengari (https://fengari.io/) 连接 javascript 和 Lua。
	- 使用定时器 timer (setInterval) 控制刷新速度。

3. 桌面版本，使用 Python、lupa、pygame。
	- 使用 lupa (https://pypi.org/project/lupa/) 连接 python 和 lua。
	- 使用 pygame.time.Clock() 来控制刷新速度。

4. js/python 提供函数和全局变量。
	- 清除屏幕。
	- 貼圖 (drawImage / blit) 。
	- 绘制文字。
	- 加载图像（素材）。
