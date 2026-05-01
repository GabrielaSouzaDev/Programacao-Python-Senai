import customtkinter as ctk
import requests

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('500x600')
app.title('Consulta CPF')
app.iconbitmap('lupa.ico')

def consultar():
    cpf = entrada_cpf.get()
    url = f'https://api.cpfhub.io/cpf/{cpf}'
    headers = {
        'x-api-key': '8511d07fd288539bf2d9698900818bbcb1a1a9eb3343662eccbfeb0152a6d66b',
        'Accept': 'application/json'
    }

    resposta = requests.get(url, headers=headers)
    dados = resposta.json()
    informacoes = (
        f'CPF: {dados["data"]["cpf"]}\n'
        f'Nome: {dados["data"]["name"]}\n'
        f'Sexo: {dados["data"]["gender"]}\n'
        f'Nascimento: {dados["data"]["birthDate"]}'
    )

    status.configure(text='CPF consultado com sucesso!', text_color='green')
    dados_gerados.configure(text=informacoes)


titulo = ctk.CTkLabel(app,
                      text='Consulta CPF',
                      font=('Arial', 30),
                      text_color='#F0F0F0')
titulo.pack(pady=40)

entrada_cpf = ctk.CTkEntry(app,
                   placeholder_text='Digite um CPF...',
                   width=260,
                   height=36,
                   font=('Arial', 15))
entrada_cpf.pack(pady=20)

botao = ctk.CTkButton(app,
                      text='Consultar',
                      command=consultar,
                      corner_radius=15,
                      fg_color=("#008000"),
                      hover_color=('#FF0000'),
                      font=('Arial', 15))
botao.pack(pady=20)

status = ctk.CTkLabel(app,
                      text='',
                      font=('Arial', 15))
status.pack(pady=20)

dados_gerados = ctk.CTkLabel(app,
                             text='',
                             font=('Arial', 15))
dados_gerados.pack(pady=20)

app.mainloop()