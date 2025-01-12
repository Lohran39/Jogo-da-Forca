import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Lista de Palavras
PALAVRAS = [
    "Futebol", "Programador", "Desenvolvedor", "Música",
    "Jogo", "Gamer", "Professor", "Militar", "Lutador", 
    "Motorista", "Praia", "New York"
]

class JogoDaForca:
    def __init__(self, root):
        self.root = root 
        self.iniciar_jogo()

    def iniciar_jogo(self):
        # Atributos do Jogo
        self.palavra = random.choice(PALAVRAS).lower()
        self.tentativas_restante = 6
        self.letras_certas = ["_"] * len(self.palavra)
        self.letras_erradas = []
        self.etapas_imagens = [
            "Lh projetos (6).png",
            "Lh projetos.png",
            "Lh projetos (1).png",
            "Lh projetos (2).png",
            "Lh projetos (3).png",
            "Lh projetos (4).png",
            "Lh projetos (5).png"
        ]
        self.etapa_atual = 0

        # Limpar Widgets Existentes
        for widget in self.root.winfo_children():
            widget.destroy()

        # Definir cor de fundo para preto
        self.root.config(bg="black")

        # Criação da Interface
        self.label_titulo = tk.Label(self.root, text="Jogo da Forca", font=("Arial", 16), bg="black", fg="white")
        self.label_titulo.pack(pady=10)

        # Carregar e exibir a imagem inicial
        self.imagem = Image.open(self.etapas_imagens[self.etapa_atual])
        self.imagem_tk = ImageTk.PhotoImage(self.imagem)
        self.label_imagem = tk.Label(self.root, image=self.imagem_tk, bg="black")
        self.label_imagem.pack(pady=10)

        # Exibindo a Palavra
        self.label_palavra = tk.Label(self.root, text=" ".join(self.letras_certas), font=("Arial", 20), bg="black", fg="white")
        self.label_palavra.pack(pady=10)

        # Contador de Tentativas
        self.label_tentativas = tk.Label(self.root, text=f"Tentativas restantes: {self.tentativas_restante}", font=("Arial", 12), bg="black", fg="white")
        self.label_tentativas.pack(pady=10)

        # Letras Erradas
        self.label_erradas = tk.Label(self.root, text="Letras erradas: Nenhuma", font=("Arial", 12), bg="black", fg="white")
        self.label_erradas.pack(pady=10)

        # Mostra as letras incorretas que o jogador já tentou.
        self.entry_letra = tk.Entry(self.root, font=("Arial", 14), width=5)
        self.entry_letra.pack(pady=10)

        # Botão verificar
        self.botao_verificar = tk.Button(self.root, text="Verificar", command=self.verificar_letra, font=("Arial", 12))
        self.botao_verificar.pack(pady=10)

        # Bind Enter key to verificar_letra method
        self.root.bind('<Return>', lambda event: self.verificar_letra())

    # Método verificar letra
    def verificar_letra(self):
        # Obter a Letra do Campo de Entrada
        letra = self.entry_letra.get().lower() # Converte a letra para minúscula.
        self.entry_letra.delete(0, tk.END) # Limpa o campo de entrada.
        
        if not letra.isalpha() or len(letra) != 1: # Verifica se a entrada é uma única letra do alfabeto.
            messagebox.showwarning("Erro", "Digite apenas uma letra válida!")
            return
        
        if letra in self.letras_certas or letra in self.letras_erradas:
            messagebox.showinfo("Atenção", "Você já tentou essa letra!")
            return
        
        # Letra Correta
        if letra in self.palavra:
            for i, l in enumerate(self.palavra):
                if l == letra:
                    self.letras_certas[i] = letra
            self.label_palavra.config(text=" ".join(self.letras_certas))

            if "_" not in self.letras_certas:
                messagebox.showinfo("Vitória", "Parabéns, você venceu!")
                self.iniciar_jogo()
        # Letra Incorreta
        else:
            self.letras_erradas.append(letra)
            self.tentativas_restante -= 1
            self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas_restante}")
            self.label_erradas.config(text=f"Letras erradas: {', '.join(self.letras_erradas)}")

            # Atualizar imagem da forca
            if self.etapa_atual < len(self.etapas_imagens) - 1:
                self.etapa_atual += 1
                self.imagem = Image.open(self.etapas_imagens[self.etapa_atual])
                self.imagem_tk = ImageTk.PhotoImage(self.imagem)
                self.label_imagem.config(image=self.imagem_tk)
                self.label_imagem.image = self.imagem_tk

            if self.tentativas_restante == 0:
                messagebox.showerror("Derrota", f"Você perdeu! A palavra era: {self.palavra}")
                self.iniciar_jogo()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    jogo = JogoDaForca(root)
    root.mainloop()
