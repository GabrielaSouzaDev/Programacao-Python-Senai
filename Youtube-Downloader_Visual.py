import customtkinter as ctk
from pytubefix import YouTube

# configurações visuais
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# criação da janela
janela = ctk.CTk()
janela.geometry('600x500')
janela.title('Downloader Youtube')

# icone da janela
janela.iconbitmap('icone.ico')

#função para barra de progresso
# def progresso(stream, chunk, bytes_remaining):




# função para baixar
def baixar():
    # captura o link digitado dentro do input
    url = link.get()
    # essa variavel abre toda a biblioteca e atrela todas as configurações de um video dentro do video desse link
    yt = YouTube(url)
    # baixar resolução padrão
    yt.streams.first().download()
    status.configure(text='Download concluído')



# elementos da tela
# label titulo
titulo = ctk.CTkLabel(janela, 
                      text='Downloader Youtube',
                      font=('Arial', 30),
                      text_color='red'
                      )
titulo.pack(pady=80)

# entrada do link
link = ctk.CTkEntry(janela, 
                    placeholder_text='Cole seu link aqui...',
                    width=260,
                    height=36,
                    font=('Arial', 15))
link.pack(pady=30)

# botão 
donwload = ctk.CTkButton(janela, 
                         text='Download',
                         command= baixar,
                         corner_radius= 15,
                         hover_color=('red'),
                         font=('Arial', 15))
donwload.pack(pady=30)

# barra de progresso
barra_progresso = ctk.CTkProgressBar(janela,
                                     orientation='horizontal')
barra_progresso.pack(pady=30)

# status do download
status = ctk.CTkLabel(janela, 
                      text='',
                      font=('Arial', 15))
status.pack(pady=30)


# para gerar a janela
janela.mainloop()