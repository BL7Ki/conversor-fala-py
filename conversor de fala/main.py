from tkinter import * # tkinter para interfaces graficas, das mais simples as mais complexas
from gtts import * # import google text to speech
from playsound import playsound # import funcao playsound
import os # biblioteca para interagir com o sistema operacional(obter info do sistema, criar diretórios)

# error 259 command, arquivo mp3 n funcionando ver depois, talvez seja versao do playsound 

# variáveis para customizar a interface
root = Tk() # Cria a janela principal da interface gráfica
root.title = ('Texto em fala') # Define o título da janela (o correto seria root.title('Texto em fala'))
root.geometry('500x420') # Define o tamanho inicial da janela
root.maxsize(500, 420) # Define o tamanho máximo da janela
root.minsize(500, 420) # Define o tamanho mínimo da janela
root.configure(bg='#1d1d1d') # Define a cor de fundo da janela

def margem(altura):
    """
    Adiciona um espaçamento vertical usando um Canvas.
    :param altura: Altura do espaçamento.
    """
    tela = Canvas(root, width=500, height=altura, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
    tela.pack()

def botao(texto, comando, padx):
    """
    Cria um botão com os parâmetros fornecidos e o adiciona à interface.
    :param texto: Texto a ser exibido no botão.
    :param comando: Função a ser chamada ao clicar no botão.
    :param padx: Espaçamento horizontal interno do botão.
    """
    botao = Button(root,
            text=texto,
            padx=padx,
            pady=20,
            command=comando,
            fg='#FFFFFF',
            activebackground='#C69749',
            activeforeground='#FFFFFF',
            bg='#C69749',
            relief=FLAT,
            font=('Montserrat', 12, 'bold'))
    botao.pack()

def resetar():
    """
    Limpa o texto inserido e remove o arquivo de áudio gerado.
    """
    e.delete(0, 'end') # Limpa o campo de entrada de texto
    os.remove('arquivo_fala.mp3') # Remove o arquivo de áudio se existir

def texto_em_fala():
    """
    Converte o texto inserido em fala e reproduz o áudio.
    """
    texto_inserido = e.get() # Obtém o texto inserido pelo usuário
    fala = gTTS(text=texto_inserido, lang='pt', slow=False, tld='com.br') # Cria o objeto de fala com o texto
    arquivo_fala = 'arquivo_fala.mp3' # Nome do arquivo de áudio
    fala.save(arquivo_fala) # Salva o áudio no arquivo
    playsound(arquivo_fala) # Reproduz o áudio

margem(20) # Adiciona um espaçamento inicial
titulo = Label(root, bg='#1d1d1d', fg='#FFFFFF', font=('Montserrat', 18, 'bold'), text='Conversor texto em fala')
titulo.pack() # Adiciona o título à interface
margem(30) # Adiciona um espaçamento
insere_texto = Label(root, bg='#1d1d1d', fg='#FFFFFF', font=('Montserrat', 16, 'bold'), text='Insira o texto:')
insere_texto.pack() # Adiciona o rótulo para a entrada de texto
margem(30) # Adiciona um espaçamento
e = Entry(root, width=25, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#000000', font=('Montserrat', 21, 'bold'), justify=CENTER)
e.pack() # Adiciona o campo de entrada de texto
margem(20) # Adiciona um espaçamento
play = botao('INICIAR', texto_em_fala, 37) # Cria o botão de iniciar e o adiciona à interface
margem(10) # Adiciona um espaçamento
reset = botao('RESETAR', resetar, 30) # Cria o botão de resetar e o adiciona à interface
root.mainloop() # Inicia o loop principal da interface gráfica
