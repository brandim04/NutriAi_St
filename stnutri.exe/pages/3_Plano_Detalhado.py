import streamlit as st

st.set_page_config(layout="wide")

paciente = st.session_state.get("paciente", "Paciente")
plano = st.session_state.get("plano", {})

st.title("Plano Alimentar do Paciente")

col1, col2 = st.columns([1,4])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)

with col2:
    st.subheader(paciente)
    st.caption("28 anos • Diabetes Tipo II")

st.divider()

col_resumo, col_plano, col_receita = st.columns([1.2,2.5,2])


with col_resumo:

    st.subheader("Resumo Nutricional")

    calorias = plano.get("calorias",1500)
    proteina = plano.get("proteina",80)
    carbo = plano.get("carbo",180)
    gordura = plano.get("gordura",70)
    imc = plano.get("imc",22)

    st.write("Calorias")
    st.progress(1100/calorias)
    st.caption(f"1100 / {calorias} kcal")

    st.write("Proteínas")
    st.progress(60/proteina)
    st.caption(f"60 / {proteina} g")

    st.write("Carboidratos")
    st.progress(130/carbo)
    st.caption(f"130 / {carbo} g")

    st.write("Gorduras")
    st.progress(40/gordura)
    st.caption(f"40 / {gordura} g")

    st.divider()

    st.subheader("Marcadores Clínicos")

    if imc < 18.5:
        st.warning("IMC abaixo do peso")

    elif imc < 25:
        st.success("IMC adequado")

    elif imc < 30:
        st.warning("Sobrepeso")

    else:
        st.error("Obesidade")


with col_plano:

    st.subheader("Plano Alimentar")

    if st.button("🥣 Café da manhã - Iogurte com frutas"):
        st.session_state.receita = "cafe"

    if st.button("🍎 Lanche da manhã - Castanhas + maçã"):
        st.session_state.receita = "lanche"

    if st.button("🍗 Almoço - Frango grelhado + arroz integral"):
        st.session_state.receita = "almoco"

    if st.button("🥑 Lanche da tarde - Iogurte proteico"):
        st.session_state.receita = "lanche_tarde"

    if st.button("🍳 Jantar - Omelete com legumes"):
        st.session_state.receita = "jantar"


with col_receita:

    st.subheader("Receita")

    if "receita" not in st.session_state:
        st.info("Clique em uma refeição para ver a receita")

    elif st.session_state.receita == "cafe":

        st.image("https://images.unsplash.com/photo-1559561853-08451507cbe7")

        st.subheader("Iogurte de coco com chia")

        st.write("Ingredientes")

        st.write("""
        • 1 pote de iogurte de coco  
        • 2 colheres de chia  
        • 1/2 xícara de frutas vermelhas
        """)

        st.write("Modo de preparo")

        st.write("""
        Misture o iogurte com a chia.

        Deixe descansar por 15 minutos.

        Adicione as frutas e sirva.
        """)

    elif st.session_state.receita == "lanche":

        st.image("https://images.unsplash.com/photo-1567306226416-28f0efdc88ce")

        st.subheader("Maçã com castanhas")

        st.write("Ingredientes")

        st.write("""
        • 1 maçã  
        • 30g castanhas
        """)

        st.write("Modo de preparo")

        st.write("""
        Corte a maçã em fatias.

        Consuma com as castanhas.
        """)

    elif st.session_state.receita == "almoco":

        st.image("https://images.unsplash.com/photo-1604908176997-125f25cc6f3d")

        st.subheader("Frango grelhado com arroz integral")

        st.write("Ingredientes")

        st.write("""
        • 120g frango grelhado  
        • 100g arroz integral  
        • salada verde
        """)

        st.write("Modo de preparo")

        st.write("""
        Tempere o frango com sal e ervas.

        Grelhe por 10 minutos.

        Sirva com arroz integral e salada.
        """)

    elif st.session_state.receita == "lanche_tarde":

        st.image("https://images.unsplash.com/photo-1604908176997-125f25cc6f3d")

        st.subheader("Iogurte proteico")

        st.write("Ingredientes")

        st.write("""
        • 1 iogurte proteico  
        • 1 colher de chia
        """)

        st.write("Modo de preparo")

        st.write("""
        Misture os ingredientes e consuma gelado.
        """)

    elif st.session_state.receita == "jantar":

        st.image("https://images.unsplash.com/photo-1604908176997-125f25cc6f3d")

        st.subheader("Omelete com legumes")

        st.write("Ingredientes")

        st.write("""
        • 2 ovos  
        • tomate  
        • espinafre
        """)

        st.write("Modo de preparo")

        st.write("""
        Bata os ovos.

        Adicione os legumes.

        Cozinhe em frigideira antiaderente.
        """)