#!/ust/bin/env python
# *-* coding:utf-8 *-*

import abc

"""
    Em "Shape" tem um metodo abstrato "abstract".
    raise irá forçar o erro caso chame o método
    sem instancia-lo.
"""
class Shape:
    def abstract(self):
        raise NotImplementedError("Method \"abstract\" not implemented!")
        return

"""
    Em "ShapeABC" se usa a biblioteca abc para
    definir um método abstrato, assim n~ao permite
    instanciar a classe diretamente.
"""
class ShapeABC:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def abstract(self):
        return

try:
    s = Shape()
    print "Shape instancied!"
except:
    print "Shape not instancied!"

try:
    s = ShapeABC()
    print "ShapeABC instancied!"
except:
    print "ShapeABC not instancied!"

