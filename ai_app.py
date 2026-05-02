import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Ljus AI", page_icon="🤖", layout="centered")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}
.block-container {
    max-width: 750px;
    padding-top: 60px;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
}
.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 30px;
}
.answer-box {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🤖 Ljus AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Savolingizni yozing — men yordam beraman</div>', unsafe_allow_html=True)

savol = st.text_area("Savol yoz:", height=120, placeholder="Masalan: biznes g‘oya ber, kod yoz, tarjima qil...")

if st.button("Javob olish 🚀"):
    if savol.strip():
        with st.spinner("AI o‘ylayapti..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Sen foydalanuvchiga sodda, aniq va foydali javob beradigan AI yordamchisan. O‘zbek tilida javob ber."},
                    {"role": "user", "content": savol}
                ]
            )
            javob = response.choices[0].message.content

        st.markdown(f'<div class="answer-box">{javob}</div>', unsafe_allow_html=True)
    else:
        st.warning("Avval savol yozing.")
