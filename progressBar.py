import time
import threading
import getSize
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog



class Progress:
    def __init__(self):
        self.root = Tk()
        self.root.title('Progress Bar')
        self.progress = ttk.Progressbar(self.root, orient='horizontal', length=150, mode='determinate')
        self.progress.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.lblPercent = Label(self.root)
        self.btn = Button(self.root, text='INICIAR PROGRESSO', command=self.carrega)
        self.btn.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.root.mainloop()

    def pb(self, max):             
        self.progress['max']=max
        self.progress['value']=0
        self.percent = 0
        self.lblPercent.place(relx=0.5, rely=0.45, anchor=CENTER)      
                
        while self.percent < 100: #self.progress['value'] < self.progress['max']:            
            self.copiado = getSize.calcula(destino)
            self.progress['value']=self.copiado - (destinoAtual) #- destinoAppdata)
            self.percent = self.progress['value']/self.progress['max']*100
            self.lblPercent['text']='{:.2f} / {:.2f}\n{:.0f}%'.format(self.progress['value'], self.progress['max'], self.percent)


    def copia(self):
        folders = ['Contacts', 'Desktop', 'Documents', 'Downloads', 'Favorites', 'Pictures', 'Music', 'Videos', 'AppData/Local/Google/Chrome']
        #Corrigir 20/07/2020
        for c in range(len(folders)):
            if os.path.exists(os.path.join(origem, folders[c])):
                os.system(f'robocopy.exe {os.path.join(origem, folders[c])} {os.path.join(destino, folders[c])} /s /e /MT[:8] > c:/temp/copy{c}.txt')
            else:
                os.system(f'robocopy.exe {origem} {destino} /s /e /MT[:8] > c:/temp/copy.txt')
                break

    def carrega(self):
        self.t1=threading.Thread(target=self.pb, args=(size,))
        self.t1.start()       

        self.t2=threading.Thread(target=self.copia)
        self.t2.start()


origem = filedialog.askdirectory(title = 'Selecionar local de origem')

size = getSize.calcula(origem)
print(size)
print(size/1024)

destino = filedialog.askdirectory(title = 'Selecionar local de destino')

destinoAtual =  getSize.calcula(destino)
#destinoAppdata = getSize.calcula(os.path.join(destino, "appdata"))

root = Progress()