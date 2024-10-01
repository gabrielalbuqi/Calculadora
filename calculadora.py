import tkinter as tk

class Calculadora:
    def __init__(self):

        self.janela = tk.Tk()
        self.janela.title("Calculadora")

        self.entry = tk.Entry(self.janela, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.botao_7 = tk.Button(self.janela, text="7", padx=40, pady=20, command=lambda: self.apertar_botao(7))
        self.botao_8 = tk.Button(self.janela, text="8", padx=40, pady=20, command=lambda: self.apertar_botao(8))
        self.botao_9 = tk.Button(self.janela, text="9", padx=40, pady=20, command=lambda: self.apertar_botao(9))
        self.botao_div = tk.Button(self.janela, text="/", padx=40, pady=20, command=lambda: self.apertar_botao("/"))

        self.botao_4 = tk.Button(self.janela, text="4", padx=40, pady=20, command=lambda: self.apertar_botao(4))
        self.botao_5 = tk.Button(self.janela, text="5", padx=40, pady=20, command=lambda: self.apertar_botao(5))
        self.botao_6 = tk.Button(self.janela, text="6", padx=40, pady=20, command=lambda: self.apertar_botao(6))
        self.botao_mult = tk.Button(self.janela, text="x", padx=40, pady=20, command=lambda: self.apertar_botao("*"))

        self.botao_1 = tk.Button(self.janela, text="1", padx=40, pady=20, command=lambda: self.apertar_botao(1))
        self.botao_2 = tk.Button(self.janela, text="2", padx=40, pady=20, command=lambda: self.apertar_botao(2))
        self.botao_3 = tk.Button(self.janela, text="3", padx=40, pady=20, command=lambda: self.apertar_botao(3))
        self.botao_sub = tk.Button(self.janela, text="-", padx=40, pady=20, command=lambda: self.apertar_botao("-"))

        self.botao_0 = tk.Button(self.janela, text="0", padx=40, pady=20, command=lambda: self.apertar_botao(0))
        self.botao_ponto = tk.Button(self.janela, text=".", padx=40, pady=20, command=lambda: self.apertar_botao("."))
        self.botao_igual = tk.Button(self.janela, text="=", padx=40, pady=20, command=self.calcular)
        self.botao_soma = tk.Button(self.janela, text="+", padx=40, pady=20, command=lambda: self.apertar_botao("+"))

        self.botao_limpar = tk.Button(self.janela, text="Limpar", padx=29, pady=20, command=self.limpar)

        self.botao_7.grid(row=1, column=0)
        self.botao_8.grid(row=1, column=1)
        self.botao_9.grid(row=1, column=2)
        self.botao_div.grid(row=1, column=3)

        self.botao_4.grid(row=2, column=0)
        self.botao_5.grid(row=2, column=1)
        self.botao_6.grid(row=2, column=2)
        self.botao_mult.grid(row=2, column=3)

        self.botao_1.grid(row=3, column=0)
        self.botao_2.grid(row=3, column=1)
        self.botao_3.grid(row=3, column=2)
        self.botao_sub.grid(row=3, column=3)

        self.botao_0.grid(row=4, column=0)
        self.botao_ponto.grid(row=4, column=1)
        self.botao_igual.grid(row=4, column=2)
        self.botao_soma.grid(row=4, column=3)

        self.botao_limpar.grid(row=5, column=0, columnspan=4)

    def apertar_botao(self, valor):
        self.entry.insert(tk.END, str(valor))

    def calcular(self):
        try:
            resultado = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(resultado))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Erro")

    def limpar(self):
        self.entry.delete(0, tk.END)

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()