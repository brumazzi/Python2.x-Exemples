def InitApp(argv):
	argc = len(argv)
	if argv[argc-1] == "__init__":
		import frame
		import sys
		from frame import GLWindow
		win = GLWindow()
		win.setSize(800,600)
		win.setTitle("PyGame")
		win.setPosition(100,30)
		win.show()
	else:
		print("Parametro incorreto!")
