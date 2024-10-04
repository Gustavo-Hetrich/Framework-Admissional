# Framework Admissional - README

## Descrição do Projeto

O **Framework Admissional** é uma ferramenta desenvolvida para auxiliar o departamento de Recursos Humanos (RH) da **Credibrf** no preenchimento de cadastros admissionais. Ele automatiza a extração de informações de arquivos PDF, como documentos pessoais e dados de contato, facilitando o preenchimento rápido e eficiente dos formulários de admissão.

## Funcionalidades

- **Leitura de PDF**: O sistema permite que o usuário selecione um arquivo PDF contendo os dados de cadastro, que será automaticamente processado.
- **Extração de Informações**: Utiliza expressões regulares (regex) para identificar e extrair campos relevantes, como nome, CPF, RG, data de nascimento, endereço, entre outros.
- **Interface Gráfica (GUI)**: A extração das informações é exibida em uma interface gráfica amigável, construída com **Tkinter**. O usuário pode revisar e editar as informações extraídas.
- **Navegação e Edição**: A interface permite a navegação pelos dados extraídos, possibilitando que o usuário veja e altere cada campo individualmente, utilizando botões e atalhos de teclado.
- **Suporte para Atalhos**: O sistema aceita navegação entre os dados utilizando as teclas de seta e um atalho para colar as informações diretamente no sistema.

## Como Usar

### 1. Seleção de Arquivo PDF
- Ao iniciar o programa, será solicitado ao usuário que selecione um arquivo PDF contendo as informações de cadastro.

### 2. Extração e Exibição de Dados
- O conteúdo do PDF é lido e processado, e as informações são extraídas automaticamente e exibidas em uma área de texto rolável.
- Campos não encontrados no documento original serão destacados em vermelho, para facilitar a identificação de possíveis dados faltantes.

### 3. Revisão e Edição
- O usuário pode revisar os dados diretamente na interface. Caso os dados estejam corretos, pode clicar no botão "Prosseguir".
- Na próxima tela, o usuário pode navegar pelos campos individualmente, utilizando os botões de navegação ou os atalhos de teclado.

### 4. Atalhos Disponíveis
- **Seta para Direita**: Próximo campo.
- **Seta para Esquerda**: Campo anterior.
- **Alt + V**: Cola a informação atual diretamente no campo de entrada, avançando para o próximo campo.

## Requisitos

- Python 3.x
- Bibliotecas necessárias: 
  - `fitz` (PyMuPDF)
  - `tkinter`
  - `re` (expressões regulares)
  - `keyboard`

Para instalar o PyMuPDF, use o comando:
```bash
pip install pymupdf
```

Para instalar a biblioteca `keyboard`, use:
```bash
pip install keyboard
```

## Executando o Programa

1. Certifique-se de ter todas as dependências instaladas.
2. Execute o script principal:
   ```bash
   python framework_admissional.py
   ```
3. Selecione o arquivo PDF quando solicitado e siga as instruções da interface.

## Licença

Este projeto foi criado para uso interno no setor de RH da **Credibrf**.
