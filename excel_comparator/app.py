import streamlit as st
import pandas as pd
from io import BytesIO

def clean_and_combine(df, cols):
    """Limpa e combina colunas para comparação."""
    return (
        df[cols]
        .fillna('')  # Substitui NaN por string vazia
        .astype(str)  # Garante que tudo é string
        .apply(lambda x: x.str.strip().str.lower())  # Padroniza
        .agg('|'.join, axis=1)  # Combina colunas
    )

def get_sheet_names(file):
    """Obtém os nomes das abas do arquivo Excel."""
    try:
        return pd.ExcelFile(file).sheet_names
    except Exception as e:
        st.error(f"Erro ao ler abas do arquivo: {str(e)}")
        return []

def compare_excel_files(df1, df2, cols1, cols2):
    """Comparação robusta entre DataFrames."""
    try:
        df1['Combinação'] = clean_and_combine(df1, cols1)
        df2['Combinação'] = clean_and_combine(df2, cols2)
        
        mask = df1['Combinação'].isin(df2['Combinação'])
        return df1[mask].drop(columns=['Combinação']), df1[~mask].drop(columns=['Combinação'])
    except Exception as e:
        st.error(f"Erro na comparação: {str(e)}")
        return pd.DataFrame(), pd.DataFrame()

def main():
    st.set_page_config(
        page_title="Excel Comparator Pro",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📊 Comparador Avançado de Planilhas")
    
    # Upload de arquivos
    col1, col2 = st.columns(2)
    with col1:
        file1 = st.file_uploader("Planilha 1", type=["xlsx", "xls"])
        sheet1 = None
        if file1:
            sheet_names1 = get_sheet_names(file1)
            sheet1 = st.selectbox("Selecione a aba da Planilha 1", sheet_names1)
    
    with col2:
        file2 = st.file_uploader("Planilha 2", type=["xlsx", "xls"])
        sheet2 = None
        if file2:
            sheet_names2 = get_sheet_names(file2)
            sheet2 = st.selectbox("Selecione a aba da Planilha 2", sheet_names2)

    if file1 and file2 and sheet1 and sheet2:
        df1 = pd.read_excel(file1, sheet_name=sheet1)
        df2 = pd.read_excel(file2, sheet_name=sheet2)
        
        # Seleção de colunas
        st.subheader("🔍 Seleção de Colunas")
        col1, col2 = st.columns(2)
        with col1:
            cols1 = st.multiselect("Colunas da Planilha 1", df1.columns)
        with col2:
            cols2 = st.multiselect("Colunas da Planilha 2", df2.columns)

        if st.button("Comparar Planilhas", type="primary") and cols1 and cols2:
            with st.spinner("Processando..."):
                encontrados, faltantes = compare_excel_files(df1, df2, cols1, cols2)
            
            # Resultados
            st.subheader("📋 Resultados")
            tab1, tab2 = st.tabs(["✅ Encontrados", "❌ Faltantes"])
            
            with tab1:
                st.dataframe(encontrados)
                st.metric("Registros Encontrados", len(encontrados))
            
            with tab2:
                st.dataframe(faltantes)
                st.metric("Registros Faltantes", len(faltantes))
            
            # Exportação
            if not encontrados.empty or not faltantes.empty:
                output = BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    if not encontrados.empty:
                        encontrados.to_excel(writer, sheet_name="Encontrados", index=False)
                    if not faltantes.empty:
                        faltantes.to_excel(writer, sheet_name="Faltantes", index=False)
                
                st.download_button(
                    "⬇️ Exportar Resultados",
                    output.getvalue(),
                    "resultado_comparacao.xlsx",
                    "application/vnd.ms-excel"
                )

if __name__ == "__main__":
    main()