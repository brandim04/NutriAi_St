import streamlit as st

if "logado" not in st.session_state or not st.session_state.logado:
    st.warning("Faça login para acessar esta página.")
    st.switch_page("app.py")

st.title("Chat com Nutricionista")

if "chat" not in st.session_state:
    st.session_state.chat = []

msg = st.text_input("Digite sua mensagem")

if st.button("Enviar"):
    if msg:
        st.session_state.chat.append(("Paciente", msg))
        st.session_state.chat.append(("Nutricionista", "Mensagem recebida! Vou analisar e te orientar."))

for autor, texto in st.session_state.chat:
    if autor == "Nutricionista":
        st.write(f"🧑‍⚕️ {texto}")
    else:
        st.write(f"👤 {texto}")

st.divider()

if st.button("Voltar para início"):
    st.switch_page("pages/2_Inicio_Paciente.py")