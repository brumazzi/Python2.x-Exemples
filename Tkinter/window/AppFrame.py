#!/usr/bin/env python3
# *-* coding: utf-8 *-*

try:
    import tkinter as tk
except:
    import Tkinter as tk

class MainFrame(tk.Tk):
    __slots__ = ["components"]

    def __enter__(self):
        self.title("My Tk Window")
        self.components = []
        self.__instance__(self.components)
        self.__config__(self.components)

        return self

    def __exit__(self, type, val, cback):
        return True

    def __instance__(self, comp):
        comp.append(tk.Button(self, text="Close", command=self.destroy))
        comp[len(comp)-1].loc = tk.BOTTOM
        comp.append(tk.Label(self, text="Click in Button to Close"))

    def __config__(self, comp):
        for c in comp:
            try:
                c.pack(side=c.loc)
            except:
                c.pack()

    def show(self):
        with self as mf:
            mf.mainloop()
