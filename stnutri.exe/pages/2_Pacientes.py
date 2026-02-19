import streamlit as st

#BLOQUEIO DE ACESSO
if "logado" not in st.session_state or not st.session_state.logado:
    st.warning("Você precisa estar logado para acessar esta página.")
    st.switch_page("app.py")

st.set_page_config(page_title="Pacientes - NutriAI", layout="wide")

#CSS
st.markdown("""
<style>
.stApp {
    background-color: #0f172a;
    color: white;
}

.header {
    background: #14b8a1;
    padding: 20px;
    border-radius: 12px;
    color: white;
}

.table-header {
    font-weight: bold;
    color: #cbd5e1;
    padding-bottom: 6px;
}

.row {
    padding: 6px 0;
}

.divider {
    border-bottom: 1px solid #334155;
    margin: 6px 0;
}

div.stButton > button {
    padding: 4px 6px !important;
    font-size: 14px !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("<div class='header'><h2>Pacientes</h2></div>", unsafe_allow_html=True)
with col2:
    st.button("+ NOVO PLANO")

st.markdown("<br>", unsafe_allow_html=True)

#filtros
f1, f2, f3 = st.columns(3)
with f1:
    st.text_input("Buscar paciente")
with f2:
    st.selectbox("Diagnóstico", ["Todos", "Diabetes I", "Diabetes II", "Câncer"])
with f3:
    st.selectbox("Ordenar por", ["Nome", "Último Plano"])

st.markdown("<br>", unsafe_allow_html=True)

h1, h2, h3, h4 = st.columns([3,2,2,2])
with h1:
    st.markdown("<div class='table-header'>Nome</div>", unsafe_allow_html=True)
with h2:
    st.markdown("<div class='table-header'>Diagnóstico</div>", unsafe_allow_html=True)
with h3:
    st.markdown("<div class='table-header'>Último Plano</div>", unsafe_allow_html=True)
with h4:
    st.markdown("<div class='table-header'>Ações</div>", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

#infos
pacientes = [
    ("Larissa Brandim", "Diabetes II", "20/08/2025"),
    ("Saulo Pietro", "Diabetes II", "20/08/2025"),
    ("Laura Marques", "Câncer", "20/08/2025"),
]

for i, (nome, diag, data) in enumerate(pacientes):

    c1, c2, c3, c4 = st.columns([3,2,2,2])

    with c1:
        st.markdown(f"<div class='row'><b>{nome}</b></div>", unsafe_allow_html=True)

    with c2:
        cor = "#ef4444" if "Diabetes" in diag else "#60a5fa"
        st.markdown(
            f"<div class='row' style='color:{cor}; font-weight:bold'>{diag}</div>",
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(f"<div class='row'>{data}</div>", unsafe_allow_html=True)

    with c4:
        b1, b2, b3 = st.columns(3)

        with b1:
            st.button("📄", key=f"rel_{i}")

        with b2:
            st.button("💬", key=f"chat_{i}")

        with b3:
            st.button("✏️", key=f"edit_{i}")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)