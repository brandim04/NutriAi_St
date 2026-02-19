import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Paciente - NutriAi", layout="wide")

#css

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}

.titulo {
    font-size: 28px;
    font-weight: 600;
    color: white;
}

.subinfo {
    color: #c9d1d9;
    font-size: 15px;
}

.section-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 10px;
    color: white;
}

.status-ativo {
    color: #00c853;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


st.markdown('<div class="titulo">Larissa Gabriela</div>', unsafe_allow_html=True)
st.markdown('<div class="subinfo">28 anos | Peso: 58kg | Altura: 1.65 | IMC: 21.3</div>', unsafe_allow_html=True)

st.divider()

#infos#

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Informações Clínicas</div>', unsafe_allow_html=True)
    st.write("**Objetivo:** Condicionamento + imunidade")
    st.write("**Condições:** Câncer de estômago")
    st.write("**Status do Plano:**")
    st.markdown('<span class="status-ativo">● Ativo</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Plano Atual</div>', unsafe_allow_html=True)
    st.write("**Fase:** 2")
    st.write("**Início:** 01/10")
    st.write("**Fim:** 31/10")
    st.write("**Calorias:** 1900 kcal")
    st.write("**Distribuição de Macros:**")
    st.write("- Proteína: 30%")
    st.write("- Carboidrato: 45%")
    st.write("- Gordura: 25%")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

#graficoss

col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Evolução do Peso</div>', unsafe_allow_html=True)

    peso = [58, 57.5, 57, 56.5]
    semanas = [1, 2, 3, 4]

    fig1 = plt.figure(figsize=(4,2.5))
    plt.plot(semanas, peso)
    plt.xlabel("Semanas")
    plt.ylabel("Peso (kg)")
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Ingestão Calórica</div>', unsafe_allow_html=True)

    calorias = [1500, 1700, 1600, 1800]
    semanas = [1, 2, 3, 4]

    fig2 = plt.figure(figsize=(4,2.5))
    plt.bar(semanas, calorias)
    plt.xlabel("Semanas")
    plt.ylabel("Kcal")
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

#botao

col5, col6 = st.columns(2)

with col5:
    st.button("➕ Novo Plano", use_container_width=True)

with col6:
    st.button("📄 Gerar Relatório", use_container_width=True)