import customtkinter as ctk
import requests

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('600x800')
app.title('Consulta CNPJ')
app.iconbitmap('lupa.ico')


def consultar():
    cnpj = entrada_cnpj.get().strip()
    url = f'https://api.opencnpj.org/{cnpj}'

    if not cnpj:
        dados_gerados.configure(text='Digite um CNPJ válido!', text_color='#FF0000')

    try:
        resposta = requests.get(url)
        dados = resposta.json()
        

        informacoes = (
        f'CNPJ: {dados["cnpj"]}\n'
        f'Razão Social: {dados["razao_social"]}\n'
        f'Situação Cadastral: {dados["situacao_cadastral"]}\n'
        f'Início das Atividades: {dados["data_inicio_atividade"]}\n'
        f'Estado: {dados["uf"]} \nMunicípio: {dados["municipio"]}'
        )
        status.configure(text='CNPJ consultado com sucesso!', text_color='#008000')
        dados_gerados.configure(text=informacoes)
    except:
        dados_gerados.configure(text='Erro ao consultar!', text_color='#FF0000')


titulo = ctk.CTkLabel(app,
                      text='Consulta CNPJ',
                      text_color='#F0F0F0',
                      font=('Arial', 30))
titulo.pack(pady=50)

entrada_cnpj = ctk.CTkEntry(app,
                            placeholder_text='Digite um CNPJ...',
                            width=260,
                            height=36,
                            font=('Arial', 15))
entrada_cnpj.pack(pady=20)

botao = ctk.CTkButton(app,
                      text='Consultar',
                      command=consultar,
                      corner_radius=15,
                      fg_color=('#008000'),
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
