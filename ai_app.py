import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("ljus 🤖")

savol = st.text_input("har qanday muomma hal qilamiz:")

if savol:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": savol}
        ]
    )

    javob = response.choices[0].message.content
    st.write("🤖:", javob)
