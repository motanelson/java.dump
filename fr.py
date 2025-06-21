import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.font as tkfont
import os

print("\033c\033[43;30m\n")


class starts:
    def __init__(self):
        print("give me a word to traslate english <> france ? " )
        self.word0=input().strip()
        self.fromm=self.load_keywords("dic")
        
        n=""
        for n in self.fromm:
            nn=n.strip().split("=")
            if nn[0].strip()==self.word0 or nn[1].strip()==self.word0:
                print(n)

   
    def load_keywords(self,names):
        try:
            with open(names+".csv", "r") as f:
                data = f.read()
                keywords =  data.split(",") 
                #print(keywords)
                return keywords
        except FileNotFoundError:
            messagebox.showerror("Erro", "Ficheiro " + names + ".csv não encontrado!")
            return []

    



starts()
