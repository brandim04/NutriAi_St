import streamlit as st

if "logado" not in st.session_state or not st.session_state.logado:
    st.warning("Faça login para acessar esta página.")
    st.switch_page("app.py")

st.title("Área do Paciente")

if "refeicoes_dia" not in st.session_state:
    st.session_state.refeicoes_dia = [
        {
            "nome": "Café da manhã",
            "horario": "07:30",
            "calorias": 350,
            "descricao": "Omelete com 2 ovos, 1 fatia de pão integral e café sem açúcar",
            "receita": "Bata os ovos, prepare a omelete e sirva com pão integral."
        },
        {
            "nome": "Almoço",
            "horario": "12:30",
            "calorias": 650,
            "descricao": "Arroz integral, frango grelhado, feijão e salada verde",
            "receita": "Grelhar o frango, montar o prato com arroz, feijão e salada."
        },
        {
            "nome": "Lanche da tarde",
            "horario": "16:00",
            "calorias": 220,
            "descricao": "Iogurte natural com banana e aveia",
            "receita": "Misture o iogurte com banana picada e aveia."
        },
        {
            "nome": "Jantar",
            "horario": "19:30",
            "calorias": 480,
            "descricao": "Sopa de legumes com carne desfiada",
            "receita": "Cozinhe os legumes e adicione carne desfiada temperada."
        }
    ]

if "agenda" not in st.session_state:
    st.session_state.agenda = [
        {"data": "20/03/2026", "evento": "Consulta de retorno", "horario": "09:00"},
        {"data": "23/03/2026", "evento": "Avaliação corporal", "horario": "15:30"},
    ]

if "alertas_ia" not in st.session_state:
    st.session_state.alertas_ia = [
        "Você está consumindo poucas fibras no período da tarde.",
        "Lembre-se de beber água entre as refeições.",
        "Seu plano alimentar está com boa distribuição calórica."
    ]

total_calorias = sum(ref["calorias"] for ref in st.session_state.refeicoes_dia)

st.subheader("Resumo do dia")

col1, col2 = st.columns(2)

with col1:
    st.metric("Calorias do dia", f"{total_calorias} kcal")

with col2:
    st.metric("Refeições planejadas", len(st.session_state.refeicoes_dia))

st.divider()

st.subheader("Refeições do dia")

for i, ref in enumerate(st.session_state.refeicoes_dia):
    with st.container():
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(f"**{ref['nome']}**")
            st.write(f"Horário: {ref['horario']}")
            st.write(f"Calorias: {ref['calorias']} kcal")
            st.write(ref["descricao"])

        with col2:
            if st.button("Mais detalhes", key=f"detalhe_{i}"):
                st.session_state.refeicao_selecionada = ref
                st.switch_page("pages/3_Plano_Alimentar.py")

        st.divider()

st.subheader("Refeições recentes")

for i, ref in enumerate(st.session_state.refeicoes_dia[:3]):
    with st.expander(f"{ref['nome']} - {ref['horario']}"):
        st.write(f"Descrição: {ref['descricao']}")
        st.write(f"Receita: {ref['receita']}")
        if st.button("Ver plano alimentar", key=f"plano_{i}"):
            st.session_state.refeicao_selecionada = ref
            st.switch_page("pages/3_Plano_Alimentar.py")

st.divider()

st.subheader("Agenda")

for item in st.session_state.agenda:
    st.write(f"**{item['data']}** - {item['evento']} às {item['horario']}")

st.divider()

st.subheader("Alertas IA")

for alerta in st.session_state.alertas_ia:
    st.info(alerta)

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("Abrir Chat"):
        st.switch_page("pages/4_Chat_Paciente.py")

with col2:
    if st.button("Sair"):
        st.session_state.logado = False
        st.switch_page("app.py")