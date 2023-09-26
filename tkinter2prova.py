import tkinter as tk
from tkinter import messagebox

# Função para realizar o login
def fazer_login():
    email = entrada_email.get()
    senha = entrada_senha.get()

    if "@" in email and len(senha) > 6:
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Email ou senha inválidos. Tente novamente.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("600x400")

# Rótulo de email
email_label = tk.Label(janela, text="Email:")
email_label.pack()

# Entrada de email
entrada_email = tk.Entry(janela)
entrada_email.pack()

# Rótulo de senha
senha_label = tk.Label(janela, text="Senha:")
senha_label.pack()

# Entrada de senha (configurada para mostrar asteriscos)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()

# Botão de login
botao_login = tk.Button(janela, text="Login", command=fazer_login)
botao_login.pack()

# Iniciar o loop principal
janela.mainloop()
