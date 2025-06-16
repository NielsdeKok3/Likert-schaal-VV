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
st.title("Villa Vibes Enquête")
st.write("Beantwoord de volgende stellingen:")

for i, question in enumerate(questions, 1):
    response = st.radio(f"{i}. {question}", options=scale, key=i)
    responses.append(scale.index(response) + 1)

if st.button("Toon resultaten"):
    df = pd.DataFrame({
        "Vraag": questions,
        "Score": responses
    })
    st.dataframe(df)
    st.bar_chart(df["Score"])

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download resultaten als CSV", csv, "villa_vibes_likert.csv")
