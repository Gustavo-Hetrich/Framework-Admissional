import re
import fitz  # PyMuPDF
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import os
import keyboard

def ler_pdf_para_texto(caminho_pdf):
    # Abre o PDF
    documento = fitz.open(caminho_pdf)
    texto = ""

    # Itera por todas as páginas
    for pagina in documento:
        texto += pagina.get_text()

    documento.close()
    return texto

def extrair_informacoes(texto):
    informacoes = {}

    # Definindo expressões regulares para capturar as informações
    informacoes["Nome"] = re.search(r"Nome:\s*(.*)", texto, re.IGNORECASE)
    informacoes["Nome Social"] = re.search(r"Nome Social:\s*(.*?)(?=\s*Estado Civil:)", texto, re.IGNORECASE)
    informacoes["Estado_Civil"] = re.search(r"Estado Civil:\s*\(x\s*\)\s*(.*?)\s*\(.*?\)\s*\(.*?\)\s*\(.*?\)\s*\(.*?\)",texto, re.IGNORECASE)
    informacoes["Raça/Etnia"] = re.search(r"Raça/Etnia:\s*\([^)]+\)\s*(\w+)", texto, re.IGNORECASE)        
    informacoes["Cidade de Nascimento"] = re.search(r"Cidade de Nascimento:\s*(.*)", texto, re.IGNORECASE)
    informacoes["Estado"] = re.search(r"Estado:\s*(Paraná|.*?)(?:\n|$)", texto, re.IGNORECASE)
    informacoes["Data de Nascimento"] = re.search(r"Data de Nascimento:\s*([\d/]+)", texto, re.IGNORECASE)
    informacoes["Nome da Mãe"] = re.search(r"Nome da mãe:\s*(.*)", texto, re.IGNORECASE)
    informacoes["Nome do Pai"] = re.search(r"Nome do pai:\s*(.*)", texto, re.IGNORECASE)
    informacoes["E-mail pessoal"] = re.search(r"E-mail pessoal:\s*(.*)", texto, re.IGNORECASE)
    informacoes["Telefone"] = re.search(r"Telefone:\s*(.*)", texto, re.IGNORECASE)
    informacoes["Celular"] = re.search(r"Celular:\s*(.*)", texto, re.IGNORECASE)
    informacoes["CPF"] = re.search(r"CPF:\s*([\d\.\/-]+)", texto, re.IGNORECASE)
    informacoes["RG"] = re.search(r"RG:\s*(\d{2,})", texto, re.IGNORECASE)
    informacoes["Emissor"] = re.search(r"Emissor:\s*(\w+)", texto, re.IGNORECASE)
    informacoes["Data de Emissão RG"] = re.search(r"Data de Emissão:\s*([\d/]+)", texto, re.IGNORECASE)
    informacoes["CPTS"] = re.search(r"CPTS:\s*(\d+)", texto, re.IGNORECASE)
    informacoes["Cartão Nacional de Saúde"] = re.search(r"Cartão Nacional de Saúde \(SUS\):\s*(\d+)", texto, re.IGNORECASE)
    informacoes["PIS"] = re.search(r"PIS:\s*([\d.]+)", texto, re.IGNORECASE)
    informacoes["Rua"] = re.search(r"Rua\s*(?:\(Av\))?:\s*(.*)", texto, re.IGNORECASE)
    informacoes["Nº"] = re.search(r"Nº\s*\D*(\d+)", texto, re.IGNORECASE)
    informacoes["Complemento"] = re.search(r"Complemento:\s*(.*)", texto, re.IGNORECASE)
    informacoes["Bairro"] = re.search(r"Bairro:\s*(.*)", texto, re.IGNORECASE)
    informacoes["Cidade"] = re.search(r"Cidade:\s*(.*)", texto, re.IGNORECASE)
    informacoes["CEP"] = re.search(r"CEP:\s*(\d+-\d+)", texto, re.IGNORECASE)
    informacoes["Banco"] = re.search(r"Banco:\s*(\w+)", texto, re.IGNORECASE)
    informacoes["Nº Conta Corrente"] = re.search(r"N° Conta Corrente:\s*(.*)", texto, re.IGNORECASE)
    informacoes["Data de Emissão PIS"] = re.search(r"PIS:\s*[\d.-]+\s*Data\s*[dD]e\s*[eE]missão:\s*([\d/]+)", texto, re.IGNORECASE)
    informacoes["Data de Emissão CPTS"] = re.search(r"CPTS:\s*\d+\s*Data\s*[dD]e\s*[eE]missão:\s*([\d/]+)", texto, re.IGNORECASE)
    informacoes["Série CPTS"] = re.search(r"Série:\s*(\d+)", texto, re.IGNORECASE)


    # Limpeza dos resultados extraídos
    informacoes = {chave: valor.group(1).strip() if valor else "Não encontrado" for chave, valor in informacoes.items()}
    
    return informacoes

def mostrar_informacoes_na_tela(informacoes):
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Informações Extraídas")
    janela.geometry("600x600")

    # Cria uma área de texto rolável
    area_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=70, height=30, font=("arial", 12))
    area_texto.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Configura a tag para texto vermelho
    area_texto.tag_configure("vermelho", foreground="red")

    # Insere as informações na área de texto
    for campo, valor in informacoes.items():
        if valor == "Não encontrado":
            area_texto.insert(tk.END, f"{campo}: {valor}\n", "vermelho")  # Insere o texto com a tag "vermelho"
        else:
            area_texto.insert(tk.END, f"{campo}: {valor}\n")

    # Torna a área de texto editável
    area_texto.config(state=tk.NORMAL)

    # Função a ser chamada quando o botão "Prosseguir" é clicado
    def ao_prosseguir():
        # Extrai o texto da área de texto do tkinter
        area_texto_extraido = area_texto.get("1.0", tk.END).strip()
        print(area_texto_extraido)
        
        # Inicializa o dicionário para armazenar as informações editadas
        informacoes_editadas = {}

        # Definindo expressões regulares para capturar as informações
        informacoes_editadas["Nome"] = re.search(r"Nome:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["CPF"] = re.search(r"CPF:\s*([\d\.\/-]+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Nome Social"] = re.search(r"Nome Social:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Estado Civil"] = re.search(r"Estado Civil:\s*\(.*?x.*?\)\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Data de Nascimento"] = re.search(r"Data de Nascimento:\s*([\d/]+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Cidade de Nascimento"] = re.search(r"Cidade de Nascimento:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Raça/Etnia"] = re.search(r"Raça/Etnia:\s*(\w+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Cartão Nacional de Saúde"] = re.search(r"Cartão Nacional de Saúde:\s*(\d{15})", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Nome da Mãe"] = re.search(r"Nome da mãe:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Nome do Pai"] = re.search(r"Nome do pai:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["CEP"] = re.search(r"CEP:\s*(\d+-\d+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Rua"] = re.search(r"Rua\s*(?:\(Av\))?:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Nº"] = re.search(r"Nº\s*\D*(\d+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Complemento"] = re.search(r"Complemento:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Bairro"] = re.search(r"Bairro:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Cidade"] = re.search(r"Cidade:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Estado"] = re.search(r"Estado:\s*(Paraná|.*?)(?:\n|$)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Telefone"] = re.search(r"Telefone:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["E-mail pessoal"] = re.search(r"E-mail pessoal:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Celular"] = re.search(r"Celular:\s*(.*)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["RG"] = re.search(r"RG:\s*(\d{2,})", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Emissor"] = re.search(r"Emissor:\s*(\w+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Data de Emissão RG"] = re.search(r"Data de Emissão RG:\s*([\d/]+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["PIS"] = re.search(r"PIS:\s*([\d.]+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Data de Emissão PIS"] = re.search(r"Data de Emissão PIS:\s*([\d/]+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["CPTS"] = re.search(r"CPTS:\s*(\d+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Série CPTS"] = re.search(r"Série CPTS:\s*(\d+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Data de Emissão CPTS"] = re.search(r"Data de Emissão CPTS:\s*([\d/]+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Banco"] = re.search(r"Banco:\s*(\w+)", area_texto_extraido, re.IGNORECASE)
        informacoes_editadas["Nº Conta Corrente"] = re.search(r"Nº\s*Conta\s*Corrente:\s*([\d\-\.\/]+)", area_texto_extraido, re.IGNORECASE)



        # Limpeza dos resultados extraídos
        informacoes_editadas = {chave: valor.group(1).strip() if valor else "Não encontrado" for chave, valor in informacoes_editadas.items()}

        # Exibe o dicionário resultante
        print("Informações editadas:", informacoes_editadas)

        

        area_texto.pack_forget()
        botao_prosseguir.pack_forget()
        messagebox.showinfo("Informações", "Informações revisadas.")
        janela.geometry("300x80")
        janela.attributes("-topmost", True)
        # Cria as variáveis necessárias para navegação
        keys = list(informacoes_editadas.keys())
        index = 0

        # Atualiza o conteúdo da label com o valor do dicionário atual
        def atualizar_conteudo():
            conteudo.config(text=f"{keys[index]}: {informacoes_editadas[keys[index]]}")

        # Funções para navegação
        def proximo():
            nonlocal index
            if index < len(keys) - 1:
                index += 1
                atualizar_conteudo()

        def anterior():
            nonlocal index
            if index > 0:
                index -= 1
                atualizar_conteudo()


        # Bind das teclas F7 e F5
        keyboard.add_hotkey('right', proximo)
        keyboard.add_hotkey('left', anterior)
        
        def colar():
            current_content = informacoes_editadas[keys[index]]
            keyboard.write(current_content)
            proximo()
        
        keyboard.add_hotkey('alt+v', colar)
        
        # Botões e label para navegação
        botao_proximo = tk.Button(janela, text=">", command=proximo)
        botao_proximo.pack(side=tk.RIGHT, anchor="e", padx=10, pady=10)
        botao_anterior = tk.Button(janela, text="<", command=anterior)
        botao_anterior.pack(side=tk.LEFT, anchor="e", padx=10, pady=10)
        conteudo = tk.Label(janela, text="", font=('arial', 10))
        conteudo.pack(anchor="center", padx=10, pady=30)

        # Atualiza a label pela primeira vez
        atualizar_conteudo()

        # Exibindo o dicionário de informações após fechar a janela
        print("\nDicionário de Informações Extraídas:")
        for campo, valor in informacoes.items():
            print(f"{campo}: {valor}")
        
        # Cria uma janela para exibir os dados extraídos
        
       

    # Adiciona um botão "Prosseguir"
    botao_prosseguir = tk.Button(janela, text="Prosseguir", command=ao_prosseguir, font=("Helvetica", 10))
    botao_prosseguir.pack(pady=10)

    # Inicia o loop da interface gráfica
    janela.mainloop()

def main():

    # Procura por arquivos PDF na pasta atual
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))  # Adjust file types as needed
    )
    if file_path:
        print(f"Arquivo selecionado: {file_path}")

        # Lê o PDF e extrai o texto
        conteudo_pdf = ler_pdf_para_texto(file_path)

        # Extrai as informações do texto e armazena no dicionário
        informacoes_extraidas = extrair_informacoes(conteudo_pdf)

        # Exibe as informações na tela
        mostrar_informacoes_na_tela(informacoes_extraidas)
        
    else:
        print("Nenhum arquivo PDF encontrado na pasta.")

    


if __name__ == "__main__":
    main()
