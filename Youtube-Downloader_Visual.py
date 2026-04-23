import customtkinter as ctk
from pytubefix import YouTube

# configurações visuais
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# criação da janela
janela = ctk.CTk()
janela.geometry('900x700')
janela.title('Downloader Youtube')

# para gerar a janela
janela.mainloop()