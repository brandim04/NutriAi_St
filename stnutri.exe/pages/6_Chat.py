import streamlit as st

st.title("Chat com Paciente")

if "chat" not in st.session_state:
    st.session_state.chat=[]

msg = st.text_input("Digite mensagem")

if st.button("Enviar"):

    st.session_state.chat.append(("Nutricionista",msg))
    st.session_state.chat.append(("Paciente","Ok, vou seguir o plano."))

for autor,texto in st.session_state.chat:

    if autor=="Nutricionista":
        st.write(f"🧑‍⚕️ {texto}")
    else:
        st.write(f"👤 {texto}")