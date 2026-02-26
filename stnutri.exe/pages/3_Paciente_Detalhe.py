import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Detalhes do Paciente", layout="wide")

if "paciente_selecionado" not in st.session_state:
    st.warning("Nenhum paciente selecionado.")
    st.stop()

paciente = st.session_state.paciente_selecionado


st.title(f" {paciente['nome']}")

st.write(f"**Idade:** {paciente['idade']} anos")
st.write(f"**Peso:** {paciente['peso']} kg")
st.write(f"**Altura:** {paciente['altura']} m")
st.write(f"**Diagnóstico:** {paciente['diagnostico']}")

st.divider()


col1, col2 = st.columns(2)

with col1:
    st.subheader("Evolução do Peso")

    semanas = [1, 2, 3, 4]
    pesos = [
        paciente["peso"],
        paciente["peso"] - 0.5,
        paciente["peso"] - 1,
        paciente["peso"] - 1.5
    ]

    fig1 = plt.figure(figsize=(4,2.5))
    plt.plot(semanas, pesos)
    plt.xlabel("Semanas")
    plt.ylabel("Peso (kg)")
    st.pyplot(fig1)

with col2:
    st.subheader("Ingestão Calórica")

    calorias = [1800, 1700, 1650, 1600]
    semanas = [1, 2, 3, 4]

    fig2 = plt.figure(figsize=(4,2.5))
    plt.bar(semanas, calorias)
    plt.xlabel("Semanas")
    plt.ylabel("Kcal")
    st.pyplot(fig2)

st.divider()


colA, colB = st.columns(2)

with colA:
    if st.button("➕ Novo Plano", use_container_width=True):
        st.switch_page("pages/4_Gerar_Plano.py")

with colB:
    if st.button("⬅ Voltar para Pacientes", use_container_width=True):
        st.switch_page("pages/2_Pacientes.py")
