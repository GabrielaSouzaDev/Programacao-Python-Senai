import customtkinter as ctk
from pytubefix import YouTube
import threading

# configurações visuais
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# criação da janela
janela = ctk.CTk()
janela.geometry('600x500')
janela.title('Downloader Youtube')

# icone da janela
janela.iconbitmap('icone.ico')

# função para barra de progresso
def progresso(stream, chunk, bytes_remaining):
    tamanho_total = stream.filesize
    bytes_baixados = tamanho_total - bytes_remaining
    porcentagem = bytes_baixados / tamanho_total

    barra_progresso.set(porcentagem) # atualiza a barra
    status.configure(text=f'Baixando... {int(porcentagem * 100)}%')
    janela.update_idletasks() # força a interface a atualizar


#função para fazer o download rodar em segundo plano
def thread_download(url):
    try:
        yt = YouTube(url, on_progress_callback=progresso) # essa variavel abre toda a biblioteca e atrela todas as configurações de um video dentro do video desse link
        stream = yt.streams.get_highest_resolution() # melhor qualidade

        # mostra a barra e o status agora que começou
        barra_progresso.pack(pady=20)
        status.pack(pady=20)
        status.configure(text='Iniciando download...',
                     text_color='white')

        stream.download()
        status.configure(text='Download concluído!',
                         text_color='green')
    except Exception as e:
        status.configure(text=f'Erro: {e}',
                         text_color='red')

# função para baixar
def baixar():
    # captura o link digitado dentro do input
    url = link.get()
    
    if not url:
        status.pack(pady=20)
        status.configure(text='Cole um link válido!',
                         text_color='orange')
        return
    
    # reset da interface
    barra_progresso.pack_forget() # esconde a barra até que o download seja iniciado
    status.pack_forget()

    barra_progresso.set(0) #mantem a barra zerada até que o download comece
    
    threading.Thread(target=thread_download, args=(url,), daemon=True).start() # inicia um fluxo de download sem travar a tela



# elementos da tela
# label titulo
titulo = ctk.CTkLabel(janela, 
                      text='Downloader Youtube',
                      font=('Arial', 30),
                      text_color='red'
                      )
titulo.pack(pady=40)

# entrada do link
link = ctk.CTkEntry(janela, 
                    placeholder_text='Cole seu link aqui...',
                    width=260,
                    height=36,
                    font=('Arial', 15))
link.pack(pady=20)

# botão 
donwload = ctk.CTkButton(janela, 
                         text='Download',
                         command= baixar,
                         corner_radius= 15,
                         hover_color=('red'),
                         font=('Arial', 15))
donwload.pack(pady=20)

# barra de progresso
barra_progresso = ctk.CTkProgressBar(janela,
                                     orientation='horizontal')
barra_progresso.set(0)
# barra_progresso.pack(pady=20)

# status do download
status = ctk.CTkLabel(janela, 
                      text='',
                      font=('Arial', 15))
# status.pack(pady=20)


# para gerar a janela
janela.mainloop()