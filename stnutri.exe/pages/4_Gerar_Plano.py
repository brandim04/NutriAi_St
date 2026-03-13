import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gerar Plano Alimentar", layout="wide")

if "etapa" not in st.session_state:
    st.session_state.etapa = 1

if "medicamentos" not in st.session_state:
    st.session_state.medicamentos = []

if "suplementos" not in st.session_state:
    st.session_state.suplementos = []

# CSS
st.markdown("""
<style>
.main { background-color: #f5f6fa; }

.titulo { font-size: 26px; font-weight: 600; text-align: center; }

.subtitulo { text-align: center; color: gray; margin-bottom: 30px; }

.card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

.step { display: flex; align-items: center; margin-bottom: 20px; }

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

col_steps, col_form = st.columns([1, 3])


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


with col_form:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    # ETAPA 1
    if st.session_state.etapa == 1:

        st.markdown("### Identificação do Paciente")

        nome = st.text_input("Nome Completo")

        col1, col2 = st.columns(2)

        with col1:
            nascimento = st.date_input("Data de Nascimento")

        with col2:
            sexo = st.selectbox("Sexo", ["Feminino", "Masculino"])

        diagnostico = st.text_input("Diagnóstico Principal")

        st.session_state.paciente = nome

    # ETAPA 2
    elif st.session_state.etapa == 2:

        st.markdown("### Antropometria")

        col1, col2 = st.columns(2)

        with col1:
            altura = st.number_input("Altura (cm)", 0.0)
            peso = st.number_input("Peso atual (kg)", 0.0)
            variacao = st.number_input("Variação de peso (%)")

        with col2:
            peso_3m = st.number_input("Peso há 3 meses (kg)", 0.0)

        # IMC automático
        if altura > 0 and peso > 0:
            altura_m = altura / 100
            imc = peso / (altura_m ** 2)
            st.metric("IMC calculado", round(imc, 2))
        else:
            imc = 0

        triagem = st.selectbox(
            "Triagem Nutricional",
            ["Selecione", "MUST", "NRS-2002", "PG-SGA"]
        )

    # ETAPA 3
    elif st.session_state.etapa == 3:

        st.markdown("### Diagnóstico")

        tempo_diag = st.number_input("Tempo de diagnóstico (anos)", 0)
        hba1c = st.number_input("HbA1c (%)", 0.0)

        st.markdown("### Monitorização Glicêmica")

        col1, col2 = st.columns(2)

        with col1:
            cgm = st.checkbox("CGM")

        with col2:
            smbg = st.checkbox("SMBG")

        hipo = st.checkbox("Histórico de Hipoglicemia")

        col3, col4 = st.columns(2)

        with col3:
            glic_jejum = st.number_input("Glicemia de jejum (mg/dL)", 0)

        with col4:
            glic_pos = st.number_input("Glicemia pós-prandial (mg/dL)", 0)

    # ETAPA 4
    elif st.session_state.etapa == 4:

        st.markdown("### Medicamentos")

        nome_med = st.text_input("Nome do medicamento")
        dose_med = st.text_input("Dose")
        freq_med = st.text_input("Frequência")
        horario_med = st.text_input("Horário")

        if st.button("➕ Adicionar Medicamento"):
            st.session_state.medicamentos.append({
                "Nome": nome_med,
                "Dose": dose_med,
                "Frequência": freq_med,
                "Horário": horario_med
            })

        if st.session_state.medicamentos:
            df_med = pd.DataFrame(st.session_state.medicamentos)
            st.dataframe(df_med, use_container_width=True)

        st.markdown("---")
        st.markdown("### Suplementação")

        nome_sup = st.text_input("Nome do suplemento")
        dose_sup = st.text_input("Dose suplemento")
        freq_sup = st.text_input("Frequência suplemento")
        horario_sup = st.text_input("Horário suplemento")

        if st.button("➕ Adicionar Suplemento"):
            st.session_state.suplementos.append({
                "Nome": nome_sup,
                "Dose": dose_sup,
                "Frequência": freq_sup,
                "Horário": horario_sup
            })

        if st.session_state.suplementos:
            df_sup = pd.DataFrame(st.session_state.suplementos)
            st.dataframe(df_sup, use_container_width=True)

    # ETAPA 5
    elif st.session_state.etapa == 5:

        st.markdown("### Objetivos")

        manter = st.checkbox("Manter peso")
        perder = st.checkbox("Perder peso")
        ganhar = st.checkbox("Ganhar peso")

        peso_alvo = st.number_input("Peso alvo (kg)", 0.0)
        prazo = st.number_input("Prazo estimado (meses)", 0)

        st.markdown("### Metas Nutricionais")

        calorias = st.number_input("Calorias diárias (kcal)", 1500)
        carb = st.number_input("Carboidratos (g/dia)", 180)
        prot = st.number_input("Proteínas (g/dia)", 80)
        gordura = st.number_input("Gordura (g/dia)", 60)

    # ETAPA 6
    elif st.session_state.etapa == 6:

        st.markdown("### Refinação para IA")

        observacoes = st.text_area("Observações adicionais para personalização")

    st.markdown('</div>', unsafe_allow_html=True)


st.write("")

col1, col2, col3, col4 = st.columns([1,1,1,2])

with col1:
    if st.session_state.etapa > 1:
        if st.button("⬅ Voltar"):
            st.session_state.etapa -= 1
            st.rerun()

with col2:
    if st.button("💾 Salvar rascunho"):
        st.success("Rascunho salvo!")

with col3:
    if st.button("🗑 Limpar"):
        st.session_state.clear()
        st.rerun()

with col4:

    if st.button("Próxima ➜", use_container_width=True):

        if st.session_state.etapa < 6:

            st.session_state.etapa += 1

        else:

            # salva plano
            st.session_state.plano = {
                "calorias": calorias,
                "carbo": carb,
                "proteina": prot,
                "gordura": gordura,
                "imc": imc
            }

            st.switch_page("pages/3_Plano_Detalhado.py")

        st.rerun()