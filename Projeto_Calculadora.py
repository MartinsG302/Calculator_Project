from tkinter import *
from tkinter import messagebox

cor0 = "#202020"
cor0_butao = "#323232"
cor1 = "#4a4a4a"

janela = Tk()
janela.geometry('305x500')
janela.title("Calculadora")
janela.configure(bg=cor0)
janela.resizable(width=False, height=False)

txt = Label(janela, width=10, height=2, fg="white", bg=cor0, font=("Ivy 19 "), text="Calculadora")
txt.place(x=-5, y=-10)

Painel = Entry(janela, width=200, fg="white", bg=cor0, borderwidth=0, highlightthickness=-1, font=("", 30))
Painel.place(x=10, y=50)


def adicionar_ao_visor(valor):
    Painel.insert(END, valor)


def calcular_resultado():
    try:
        expressao = Painel.get()
        resultado = eval(expressao)
        Painel.delete(0, END)
        Painel.insert(END, resultado)
    except Exception as e:
        messagebox.showerror("Erro", "Erro!")
        Painel.delete(0, END)


def limpar_visao():
    Painel.delete(0, END)


def apagar_caractere():
    expressao_atual = Painel.get()
    expressao_atualizada = expressao_atual[:-1]
    Painel.delete(0, END)
    Painel.insert(END, expressao_atualizada)
    
def inverter_sinal():
    expressao_atual = Painel.get()
    if expressao_atual and expressao_atual[0] == "-":
        Painel.delete(0)
    else:
        Painel.insert(0, "-")



for i in range(1, 10):
    botao = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text=str(i), borderwidth=0,
                   highlightthickness=-1, command=lambda digit=i: adicionar_ao_visor(digit))
    botao.place(x=10 + (i - 1) % 3 * 65, y=250 - (i - 1) // 3 * 50)

Botao_0 = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text="0", borderwidth=0, highlightthickness=-1,
                 command=lambda: adicionar_ao_visor(0))
Botao_0.place(x=75, y=300)

Botao_virgula = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text=",", borderwidth=0,
                       highlightthickness=-1, command=lambda: adicionar_ao_visor("."))
Botao_virgula.place(x=140, y=300)

adi_operador = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text="+", borderwidth=0,
                      highlightthickness=-1, command=lambda: adicionar_ao_visor("+"))
adi_operador.place(x=230, y=150)

sub_operador = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text="-", borderwidth=0,
                      highlightthickness=-1, command=lambda: adicionar_ao_visor("-"))
sub_operador.place(x=230, y=200)

mult_operador = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text="x", borderwidth=0,
                       highlightthickness=-1, command=lambda: adicionar_ao_visor("*"))
mult_operador.place(x=230, y=250)

div_operador = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text="/", borderwidth=0,
                      highlightthickness=-1, command=lambda: adicionar_ao_visor("/"))
div_operador.place(x=230, y=300)

Botao_mais_e_menos = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text="+/-", borderwidth=0,
                            highlightthickness=-1, command=inverter_sinal)
Botao_mais_e_menos.place(x=10, y=300)

btn_igual = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text="=", borderwidth=0, highlightthickness=-1,
                   command=calcular_resultado)
btn_igual.place(x=140, y=350)

btn_limpar = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text="C", borderwidth=0, highlightthickness=-1,
                    command=limpar_visao)
btn_limpar.place(x=230, y=350)

btn_apagar = Button(janela, width=8, height=2, fg="white", bg=cor0_butao, text="<--", borderwidth=0, highlightthickness=-1,
                    command=apagar_caractere)
btn_apagar.place(x=230, y=100)

janela.mainloop()
