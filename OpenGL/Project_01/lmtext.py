import loadmodel
from loadmodel import *
import paths as p

m = PyModel()

m.load(p._model+"cube")
#try:
m.drawQuads()
#except:
#	print("Nao foi possivel desenhar o modelo.")
