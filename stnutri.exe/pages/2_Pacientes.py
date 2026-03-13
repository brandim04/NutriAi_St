import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pacientes", layout="wide")

st.title("👩‍⚕️ Pacientes")


dados = {
    "Nome": ["Larissa Gabriela", "João Silva", "Maria Santos", "Carlos Oliveira"],
    "Idade": [28, 45, 34, 52],
    "Diagnóstico": ["Diabetes II", "Obesidade", "SOP", "Diabetes I"]
}

df = pd.DataFrame(dados)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Pacientes cadastrados", len(df))

with col2:
    diabetes = df[df["Diagnóstico"].str.contains("Diabetes")]
    st.metric("Pacientes com Diabetes", len(diabetes))

with col3:
    st.metric("Planos ativos", len(df))

st.divider()


busca = st.text_input("🔎 Buscar paciente")

if busca:
    df = df[df["Nome"].str.contains(busca, case=False)]


st.subheader("Lista de Pacientes")

for i, row in df.iterrows():

    with st.container():

        col1, col2, col3 = st.columns([5,1,1])

        with col1:

            st.markdown(f"""
            **{row["Nome"]}**

            {row["Idade"]} anos  
            Diagnóstico: **{row["Diagnóstico"]}**
            """)

        with col2:

            if st.button("📄 Ver plano", key=f"ver{i}"):

                st.session_state.paciente = row["Nome"]
                st.switch_page("pages/3_Plano_Detalhado.py")

        with col3:

            if st.button("➕ Gerar plano", key=f"gerar{i}"):

                st.session_state.paciente = row["Nome"]
                st.switch_page("pages/4_Gerar_Plano.py")

        st.divider()