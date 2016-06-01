#!/usr/bin/env python
# *-* coding:utf-8 *-*

#########################################################
# Manual de passagem de parametros e keywords em python #
# As vezes na programação, é dificil quando se depara c #
# -om metodos limitados de parametros (Em casos que se  #
# necessita a passagem de "n" parametros), assim como e #
# -sse exemplo, muitos outros estarão sendo escritos e  #
# enviados para ajudar a suprir as duvidas da linguagem #
# e instruis suas funcionalidades as pessoas.           #
#                                                       #
# Autor: Daniel Borges Brumazzi                         #
# Empresa: None                                         #
# Data: 25/11/2015                                      #
# #######################################################

class Param(object):
    __slots__ = ["args","kwds"] # Variaveis da classe

    # *args são os parametros passados na instancia do objeto
    # **kwds são as keywords devinidas no parametro
    # os args são tuplas com lista de valores
    # as kwds são partes de uma struct
    def __init__(self, *args, **kwds): 
        # Guandando parametros nas variaveis da classe
        self.args = args
        self.kwds = kwds

    # Escreve tudo que está dentro de "self.args"
    def list_args(self):
        print "ARGS:"
        for x in self.args:
            print " ",x
        print ''

    # Escreve tudo que está dentro de "self.kwds"
    def list_kwds(self):
        print "KWDS:"
        for x in self.kwds:
            print " ",x,":",self.kwds[x]
        print ''

# Instancia do objeto passando os parametros
p = Param(
        "args_1",
        "args_2",
        "args_3",
        "args_4",
         kwds_1 = "kwds_P",
         kwds_2 = "kwds_S",
         kwds_3 = "kwds_T",
         kwds_4 = "kwds_Q",
        )

# Chamada das funções de listagem
p.list_args()
p.list_kwds()
