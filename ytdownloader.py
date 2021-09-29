#x=list(map(int,input().split()))
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa=list(string.ascii_lowercase) lsit do alfa
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))
from tkinter import *
from tkinter import filedialog,messagebox
import tkinter
from tkinter.font import BOLD
from PIL import Image, ImageTk
import pytube

cor = "#404040"#pretoclaro
 
root = Tk()
root.title("YouYube Downloader")
root.resizable(False, False)

root.geometry("660x150")
root.config(bg=cor)

stringURL = StringVar()
stringDiretorio =StringVar()
url = str()
caminho = str()
 
def savevid():
    global caminho
    caminho = filedialog.askdirectory()
    stringDiretorio.set(caminho)
 
def downvid():
    global url
    try:
        url = stringURL.get()   
        youtube = pytube.YouTube(url)   
        video = youtube.streams.get_highest_resolution()    
        video.download(caminho, youtube.title)
        msg = f'''
Titulo: {youtube.title}
Duração: {youtube.length} segundos
Canal: {youtube.author}
Sucesso. Salvo em: {caminho}
'''
    except:
        msg="URL Inválida"
    messagebox.showinfo("YouYube Downloader",msg)
 
img = ImageTk.PhotoImage(Image.open("YouTube.ico"))
 
lb1 = Label(root, image=img, bg=cor).pack(anchor=NW)
lb2 = Label(root, text="URL", bg=cor,font=BOLD).place(x=130, y=5)
lb3 = Label(root, text="Diretório", bg=cor,font=BOLD).place(x=130, y=35)

et1 = Entry(root, textvariable=stringURL, width=53).place(x=210, y=5)
et2 = Entry(root, textvariable=stringDiretorio, width=53).place(x=210, y=35)

bt1 = Button(root, text="Onde salvar", width=20, command=savevid).place(x=210, y=65)
bt2 = Button(root, text="Baixar vídeo", width=20, command=downvid).place(x=380, y=65)
 
root.mainloop()


caramba='''def janelaip():
    def buscaip():
        try:
            textip.configure(font=("Times New Roman", 12, "bold"),state='normal')
            textip.delete('1.0',tkinter.END)
        except:
            pass
        global result
        result = input.get()
        try:
            api=requests.get('http://ipwhois.app/json/'+result).json()
        except:
            msg="IP Inválido"
        try:
            msg=f"IP: {api['ip']}\nTIPO: {api['type']}\nCONTINENTE: {api['continent']}\nCÓDIGO DO CONTINENTE: {api['continent_code']}\nPAÍS: {api['country']}\nCAPITAL DO PAIS: {api['country_capital']}\nCÓDIGO TELEFÕNICO DO PAÍS: {api['country_phone']}\nREGIÃO: {api['region']}\nCIDADE: {api['city']}\nLATITUDE: {api['latitude']}\nLONGITUDE: {api['longitude']}\nORG: {api['org']}\nISP: {api['isp']}\nHORÁRIO PADRÃO: {api['timezone']}\nNOME DO HORÁRIO PADRÃO: {api['timezone_name']}\nGMT: {api['timezone_gmt']}\nMOEDA: {api['currency']}\nCODIGO DA MOEDA: {api['currency_code']}"
        except:
            msg="IP Inválido"
        textip.insert('1.0',msg)
        textip.configure(font=("Times New Roman", 12, "bold"),fg='black',state=DISABLED)
        if len(msg)==11:textip.configure(fg='red')
    frameip = Frame(root)
    inputip = Entry(frameip, width = 50)
    inputip.pack()
    textip = Text(root, font = ('ariel',20))

    buttonip = Button(frameip, text = 'CONSULTAR', command = buscaip)                                                 
    buttonip.pack(side = RIGHT)
    frameip.pack(side = TOP)
    textip.pack()'''
