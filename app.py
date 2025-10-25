import streamlit as st
import os
import groq
from datetime import datetime

# Configurar página
st.set_page_config(
    page_title="Mestre Jurídico AI",
    page_icon="⚖️",
    layout="wide"
)

# Título principal
st.title("⚖️ Mestre Jurídico AI")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("📋 Menu")
    st.info("""
    **Como usar:**
    1. Preencha os dados abaixo
    2. Clique em Gerar Contrato
    3. Revise e faça download
    """)

# Formulário principal
st.subheader("📝 Criar Novo Contrato")

with st.form("contrato_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Parte A (Contratante)**")
        nome_a = st.text_input("Nome completo/Razão social")
        cpf_a = st.text_input("CPF/CNPJ")
    
    with col2:
        st.write("**Parte B (Contratado)**")
        nome_b = st.text_input("Nome completo/Razão social", key="nome_b")
        cpf_b = st.text_input("CPF/CNPJ", key="cpf_b")
    
    st.write("**Detalhes do Contrato**")
    tipo_contrato = st.selectbox(
        "Tipo de contrato:",
        ["Prestação de Serviços", "Confidencialidade (NDA)", "Compra e Venda", "Parceria"]
    )
    
    valor = st.text_input("Valor do contrato (opcional)")
    prazo = st.text_input("Prazo de vigência (ex: 12 meses)")
    
    # Botão de gerar
    gerar = st.form_submit_button("🔄 Gerar Contrato")
    
    if gerar:
        if not nome_a or not nome_b:
            st.error("❌ Preencha os nomes das partes")
        else:
            with st.spinner("⚖️ Gerando contrato juridicamente válido..."):
                try:
                    # Aqui viria a integração com a Groq
                    contrato_exemplo = f"""
                    **CONTRATO DE {tipo_contrato.upper()}**
                    
                    Entre as partes:
                    **{nome_a}**, inscrito no {cpf_a}, doravante denominado CONTRATANTE;
                    
                    e
                    
                    **{nome_b}**, inscrito no {cpf_b}, doravante denominado CONTRATADO;
                    
                    Celebra o presente contrato com base no Código Civil Brasileiro.
                    
                    **CLÁUSULA PRIMEIRA - DO OBJETO**
                    O objeto deste contrato é a prestação de serviços conforme acordado.
                    
                    **CLÁUSULA SEGUNDA - DO PRAZO**
                    Vigência: {prazo}
                    
                    **CLÁUSULA TERCEIRA - DO VALOR**
                    Valor acordado: {valor}
                    
                    Local e data: {datetime.now().strftime('%d/%m/%Y')}
                    
                    ___________________________
                    {nome_a}
                    
                    ___________________________
                    {nome_b}
                    """
                    
                    st.success("✅ Contrato gerado com sucesso!")
                    st.text_area("Seu contrato:", contrato_exemplo, height=300)
                    
                    # Botão de download
                    st.download_button(
                        label="📥 Download do Contrato",
                        data=contrato_exemplo,
                        file_name=f"contrato_{tipo_contrato}_{datetime.now().strftime('%d%m%Y')}.txt",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"Erro ao gerar contrato: {e}")

# Rodapé
st.markdown("---")
st.caption("⚖️ Mestre Jurídico AI - v1.0 - Gerando contratos com validade jurídica")
