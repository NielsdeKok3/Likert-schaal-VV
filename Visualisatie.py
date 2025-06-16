import streamlit as st
import pandas as pd

st.set_page_config(page_title="Villa Vibes Enquête", layout="wide")
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .stRadio > div {
            flex-direction: row;
        }
        h1 {
            color: #0e4d92;
        }
        .question-container {
            background-color: #ffffff;
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

questions = [
    "Ik vond mijn verblijf bij Villa Vibes aangenaam.",
    "Ik ben van plan om in de toekomst opnieuw te verblijven bij Villa Vibes.",
    "Ik zou Villa Vibes aanbevelen aan vrienden en familie.",
    "De villa waarin ik verbleef was schoon en hygiënisch.",
    "Het personeel van Villa Vibes was vriendelijk en behulpzaam.",
    "Het park was goed onderhouden en verzorgd.",
    "De voorzieningen in de villa voldeden aan mijn verwachtingen.",
    "Het in- en uitcheckproces verliep vlot en efficiënt.",
    "Ik voelde me welkom bij aankomst op het park.",
    "Ik voelde me veilig tijdens mijn verblijf in het park.",
    "Het park bood voldoende rust en ontspanning.",
    "De wifi-verbinding was stabiel en betrouwbaar.",
    "De informatie voorafgaand aan het verblijf was duidelijk en volledig.",
    "De locatie van het park was gunstig en goed bereikbaar.",
    "Het horeca-aanbod op het park was gevarieerd en van goede kwaliteit.",
    "Het animatieprogramma was aantrekkelijk en goed georganiseerd.",
    "De prijs van het verblijf was in verhouding met de geboden kwaliteit.",
    "De bedden in de villa waren comfortabel.",
    "Er waren voldoende faciliteiten beschikbaar op het park.",
    "De parkeergelegenheid op het park was goed geregeld.",
    "De villa bood voldoende privacy tijdens het verblijf.",
    "De sfeer op het park was aangenaam en ontspannen.",
    "De activiteiten voor kinderen waren leuk en afwisselend.",
    "De boekingsprocedure was eenvoudig en duidelijk.",
    "Ik zou langer willen verblijven bij een volgend bezoek aan Villa Vibes."
]
scale = ["Helemaal mee oneens", "Oneens", "Neutraal", "Eens", "Helemaal mee eens"]

responses = []
st.title("🏡 Villa Vibes - Gastenbeleving Enquête")
st.markdown("We horen graag jouw mening! Geef aan in hoeverre je het eens bent met de onderstaande stellingen. Jouw feedback helpt ons verbeteren. 💬")

col1, col2 = st.columns(2)
progress = 0

for i, question in enumerate(questions, 1):
    container = col1 if i % 2 != 0 else col2
    with container:
        with st.container():
            st.markdown(f"<div class='question-container'><b>{i}. {question}</b>", unsafe_allow_html=True)
            response = st.radio("", options=scale, key=i)
            st.markdown("</div>", unsafe_allow_html=True)
            responses.append(scale.index(response) + 1)

    progress = int((len(responses) / len(questions)) * 100)
    st.progress(progress)

st.markdown("---")
if st.button("Toon resultaten"):
    df = pd.DataFrame({
        "Vraag": questions,
        "Score": responses
    })
    st.subheader("Samenvatting van jouw antwoorden")
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df["Score"])

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download resultaten als CSV", csv, "villa_vibes_likert.csv", mime="text/csv")

