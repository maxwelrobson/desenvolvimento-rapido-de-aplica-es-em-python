import tkinter as tk

def submit():
    #Recupera os dados dos campos de entrada
    nome = nome_entry.get()
    email = email_entry.get()

    #imprime os dados no console
    print("Nome:", nome)
    print("Email:", email)

#Cria janela principal
root = tk.Tk()
root.title("Formulário de Inscrição")

#Cria um frame para conter os widgets
frame = tk.Frame(root)
frame.pack(padx=100, pady=70)

#Campo de entrada para "Nome"
nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1, pady=10)

#Campo de entrada para "Email"
email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

#Botão de submissão
submit_button = tk.Button(frame, text="Submeter", command=submit)
submit_button.grid(row=2, columnspan=2, pady=20)

#Inicializa o loop da GUI
root.mainloop()
