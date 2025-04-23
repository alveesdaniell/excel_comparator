# 📊 Excel Comparator

**Excel Comparator** é uma aplicação web desenvolvida em **Python + Streamlit** que permite comparar duas planilhas Excel com diferentes critérios e retornar os registros que coincidem e os que estão faltando.

> 🔗 Teste agora: [excelcomparator.streamlit.app](https://excelcomparator.streamlit.app)

---

## 🚀 Funcionalidades

- Upload de duas planilhas Excel (`.xlsx` ou `.xls`)
- Seleção de abas e colunas específicas para realizar a comparação
- Identificação de:
  - ✅ Registros encontrados
  - ❌ Registros faltantes
- Exportação dos resultados em um único arquivo `.xlsx`
- Interface responsiva com Streamlit

---

## 🛠️ Como usar

### 1. Suba suas planilhas  
Faça o upload de duas planilhas no formato Excel.

### 2. Escolha as abas  
Selecione as abas de cada planilha que deseja comparar.

### 3. Selecione as colunas  
Escolha as colunas de cada aba que serão utilizadas para a comparação. Elas podem ser diferentes, mas devem representar os mesmos dados em contexto.

### 4. Execute a comparação  
Clique em **"Comparar Planilhas"**. O app mostrará os resultados em duas abas: encontrados e faltantes.

### 5. Exporte os resultados  
Clique no botão de download para salvar o arquivo final com os dois relatórios.

---

## 🧠 Como funciona

A comparação é feita a partir de uma coluna “Combinada”, formada pela junção padronizada dos valores das colunas selecionadas. O sistema trata automaticamente:

- Valores nulos ou vazios
- Strings com letras maiúsculas/minúsculas

---

## 🧪 Teste agora

Acesse a versão ao vivo da aplicação:

👉 [https://excelcomparator.streamlit.app](https://excelcomparator.streamlit.app)

---

## 💻 Executar localmente

### Pré-requisitos

- Python 3.9+
- `pip`

### Instalação

```bash
git clone https://github.com/alveesdaniell/excel_comparator
cd excel_comparator
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Estrutura do Projeto

```
excel_comparator/
├── app.py              # Código principal do Streamlit
├── requirements.txt    # Dependências
└── README.md           # Documentação do projeto
```

---

## 📌 Tecnologias utilizadas

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [XlsxWriter](https://xlsxwriter.readthedocs.io/)
- [PyArrow](https://arrow.apache.org/docs/python/)

---

## 🧑‍💻 Autor

Feito com dedicação por [Daniel Alves](https://github.com/alveesdaniell) 🤘  
Se curtiu o projeto, deixe uma ⭐ no repositório!