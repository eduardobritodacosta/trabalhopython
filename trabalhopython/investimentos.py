#Nome:EDUARDO BRITO DA COSTA, MATRICULA: 2314290127
#NOME:PEDRO SANTOS LEMOS PAIM KAISER, MATRICULA: 2314290138
import tkinter as tk
from tkinter import ttk


taxa_anual = 0.1415
taxa_diaria = (1 + taxa_anual) ** (1 / 365) - 1


COR_PRINCIPAL = "#005CA9"    
COR_SECUNDARIA = "#E5F1FB"   
COR_TEXTO = "white"

def obter_aliquota_iof(dias):
    tabela_iof = [
        1.00, 0.96, 0.93, 0.90, 0.86, 0.83, 0.80, 0.76, 0.73, 0.70,
        0.66, 0.63, 0.60, 0.56, 0.53, 0.50, 0.46, 0.43, 0.40, 0.36,
        0.33, 0.30, 0.26, 0.23, 0.20, 0.16, 0.13, 0.10, 0.06, 0.03
    ]
    return tabela_iof[dias - 1] if 0 < dias <= 30 else 0.0

def obter_aliquota_ir(dias):
    if dias <= 180:
        return 0.225
    elif dias <= 360:
        return 0.20
    elif dias <= 720:
        return 0.175
    else:
        return 0.15

def calcular():
    try:
        valor_inicial = float(entry_valor.get())
        dias = int(entry_dias.get())

        rendimento_bruto = valor_inicial * ((1 + taxa_diaria) ** dias - 1)
        valor_total = valor_inicial + rendimento_bruto

        aliquota_iof = obter_aliquota_iof(dias)
        iof = rendimento_bruto * aliquota_iof

        rendimento_liquido_iof = rendimento_bruto - iof
        aliquota_ir = obter_aliquota_ir(dias)
        ir = rendimento_liquido_iof * aliquota_ir

        valor_liquido = valor_inicial + rendimento_bruto - iof - ir

        resultado_texto = (
            f"Valor Inicial: R$ {valor_inicial:,.2f}\n"
            f"Rendimento Bruto: R$ {rendimento_bruto:,.2f}\n"
            f"Desconto IOF: R$ {iof:,.2f} (Alíquota: {aliquota_iof*100:.1f}%)\n"
            f"Desconto IR: R$ {ir:,.2f} (Alíquota: {aliquota_ir*100:.1f}%)\n"
            f"Valor Final Líquido: R$ {valor_liquido:,.2f}"
        )
        resultado_label.config(text=resultado_texto)
    except ValueError:
        resultado_label.config(text="Digite valores válidos para valor e dias.")

root = tk.Tk()
root.title("Caixinha Super Cofrinho")
root.geometry("480x400")
root.configure(bg=COR_SECUNDARIA)


frame = ttk.Frame(root, padding="30 25 30 25", style="Card.TFrame")
frame.place(relx=0.5, rely=0.35, anchor="center")

style = ttk.Style()
style.theme_use("clam")
style.configure("Card.TFrame", background=COR_SECUNDARIA)
style.configure("TLabel", background=COR_SECUNDARIA, font=('Segoe UI', 10))
style.configure("TEntry", padding=5)
style.configure("TButton", font=('Segoe UI', 10, 'bold'))


ttk.Label(frame, text="Valor Inicial (R$):").grid(column=0, row=0, sticky='W', padx=5, pady=5)
entry_valor = ttk.Entry(frame, width=28)
entry_valor.grid(column=1, row=0, pady=5)

ttk.Label(frame, text="Tempo de Investimento (Dias):").grid(column=0, row=1, sticky='W', padx=5, pady=5)
entry_dias = ttk.Entry(frame, width=28)
entry_dias.grid(column=1, row=1, pady=5)

botao = tk.Button(
    frame, text="Calcular", command=calcular,
    bg=COR_PRINCIPAL, fg=COR_TEXTO, font=("Segoe UI", 10, "bold"),
    relief='flat', padx=10, pady=6, width=20
)
botao.grid(column=0, row=2, columnspan=2, pady=15)

resultado_label = ttk.Label(root, text="", font=("Segoe UI", 10), justify="left", background=COR_SECUNDARIA)
resultado_label.place(relx=0.5, rely=0.75, anchor="center")

root.mainloop()
