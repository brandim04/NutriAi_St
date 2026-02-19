import streamlit as st

st.set_page_config(page_title="Gerar Plano Alimentar", layout="wide")


if "etapa" not in st.session_state:
    st.session_state.etapa = 1

#css

st.markdown("""
<style>

.main {
    background-color: #f5f6fa;
}

.titulo {
    font-size: 26px;
    font-weight: 600;
    text-align: center;
}

.subtitulo {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

.step {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

.step-circle {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background-color: #d1d5db;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    margin-right: 10px;
}

.step-active {
    background-color: #10b981;
    color: white;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


st.markdown('<div class="titulo">GERAR PLANO ALIMENTAR</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Preencha os dados do paciente para gerar um plano alimentar personalizado</div>', unsafe_allow_html=True)


col_steps, col_form = st.columns([1, 3])

#etapas

with col_steps:
    st.markdown("### Etapas")

    etapas = [
        "Identificação",
        "Antropometria",
        "Diagnóstico",
        "Medicamentos e suplementação",
        "Objetivo",
        "Refinação para IA"
    ]

    for i, nome in enumerate(etapas, start=1):
        if st.session_state.etapa == i:
            st.markdown(f"""
            <div class="step">
                <div class="step-circle step-active">{i}</div>
                <div><b>{nome}</b></div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="step">
                <div class="step-circle">{i}</div>
                <div>{nome}</div>
            </div>
            """, unsafe_allow_html=True)

#forms

with col_form:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if st.session_state.etapa == 1:

        st.markdown("### Identificação do Paciente")

        nome = st.text_input("Nome Completo", "Larissa Gabriela dos Santos Brandim")

        col1, col2 = st.columns(2)
        with col1:
            nascimento = st.date_input("Data de Nascimento")
        with col2:
            sexo = st.selectbox("Sexo", ["Feminino", "Masculino"])

        diagnostico = st.text_input("Diagnóstico Principal", "Diabetes II")

    elif st.session_state.etapa == 2:
        st.markdown("### Antropometria")
        peso = st.number_input("Peso (kg)", 0.0, 300.0, 58.0)
        altura = st.number_input("Altura (m)", 0.0, 3.0, 1.65)

    elif st.session_state.etapa == 3:
        st.markdown("### Diagnóstico")
        st.text_area("Detalhes do diagnóstico")

    elif st.session_state.etapa == 4:
        st.markdown("### Medicamentos e Suplementação")
        st.text_area("Medicamentos em uso")

    elif st.session_state.etapa == 5:
        st.markdown("### Objetivo")
        st.selectbox("Objetivo do plano", ["Emagrecimento", "Hipertrofia", "Condicionamento", "Imunidade"])

    elif st.session_state.etapa == 6:
        st.markdown("### Refinação para IA")
        st.text_area("Observações adicionais para personalização")

    st.markdown('</div>', unsafe_allow_html=True)

#botoes

st.write("")
colA, colB, colC = st.columns([1,1,2])

with colA:
    if st.button("💾 Salvar rascunho"):
        st.success("Rascunho salvo!")

with colB:
    if st.button("🗑 Limpar"):
        st.session_state.clear()
        st.rerun()

with colC:
    if st.button("Próxima ➜", use_container_width=True):
        if st.session_state.etapa < 6:
            st.session_state.etapa += 1
        else:
            st.success("Plano finalizado com sucesso!")
        st.rerun()