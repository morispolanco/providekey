import streamlit as st
from model import GeneralModel


def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = st.sidebar.text_input("APIkey", type="password")
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip() , api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("Escritor GPT-3")

        # st.write("---")

        s_example = "Escriba un ensayo argumentativo a favor de los vouchers escolares"
        input = st.text_area(
            "Use el ejemplo de abajo o escriba su propio texto en español",
            value=s_example,
            max_chars=1250,
            height=50,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
