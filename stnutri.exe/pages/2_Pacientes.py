import streamlit as st

st.set_page_config(page_title="Pacientes", layout="wide")

st.title("Pacientes Cadastrados")


pacientes = [
    {"nome": "Larissa Gabriela", "idade": 28, "peso": 58, "altura": 1.65, "diagnostico": "Diabetes II"},
    {"nome": "Saulo Pietro", "idade": 20, "peso": 82, "altura": 1.75, "diagnostico": "Hipertensão"},
    {"nome": "Maria Souza", "idade": 34, "peso": 90, "altura": 1.68, "diagnostico": "Obesidade"}
]

st.write("Clique no nome do paciente para visualizar os detalhes:")

st.divider()

for paciente in pacientes:
    col1, col2 = st.columns([3,2])

    with col1:
        if st.button(paciente["nome"], key=paciente["nome"], use_container_width=True):
            st.session_state.paciente_selecionado = paciente
            st.switch_page("pages/3_Paciente_Detalhe.py")

    with col2:
        st.write(paciente["diagnostico"])

    st.divider()
