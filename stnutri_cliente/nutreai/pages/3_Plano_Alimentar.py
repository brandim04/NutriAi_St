import streamlit as st

if "logado" not in st.session_state or not st.session_state.logado:
    st.warning("Faça login para acessar esta página.")
    st.switch_page("app.py")

st.title("Plano Alimentar")

ref = st.session_state.get("refeicao_selecionada", None)

if not ref:
    st.warning("Nenhuma refeição selecionada.")
    if st.button("Voltar"):
        st.switch_page("pages/2_Inicio_Paciente.py")
else:
    st.subheader(ref["nome"])

    st.write(f"**Horário:** {ref['horario']}")
    st.write(f"**Calorias:** {ref['calorias']} kcal")

    st.write("**Descrição da refeição**")
    st.write(ref["descricao"])

    st.write("**Receita / modo de preparo**")
    st.write(ref["receita"])

    st.write("**Orientações nutricionais**")
    st.write(
        "Consumir esta refeição no horário planejado, mantendo boa hidratação ao longo do dia. "
        "Evitar substituições sem alinhamento com o nutricionista."
    )

    st.write("**Observações**")
    st.write(
        "Plano alimentar individualizado. As quantidades e substituições devem seguir a orientação profissional."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Voltar para início"):
            st.switch_page("pages/2_Inicio_Paciente.py")

    with col2:
        if st.button("Ir para o chat"):
            st.switch_page("pages/4_Chat_Paciente.py")