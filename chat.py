from test import run_conversation
import streamlit as st
import pandas as pd
from utils import llm_utils
st.title("💬 Vizard")
st.caption("Data Visualization Assistant")
uploaded_file = st.file_uploader("Choose a file", type='csv')
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.dataframe(dataframe)


if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]


for i, msg in enumerate(st.session_state.messages):
    if("content" in msg):
        st.chat_message(msg["role"]).write(msg["content"])
    if("chart" in msg):
        st.chat_message(msg["role"]).image(msg["chart"])


if prompt := st.chat_input():
    system_prompt = llm_utils.create_system_prompt(dataframe)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    res, chart = run_conversation(system_prompt, prompt)
    
    
    st.session_state.messages.append({"role": "assistant", "content": res.choices[0].message.content})

    st.chat_message("assistant").write(res.choices[0].message.content)