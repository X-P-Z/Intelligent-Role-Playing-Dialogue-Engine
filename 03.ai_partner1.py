import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="AI 智能伴侣",
    page_icon="🐧",
    #整个网页的布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI 智能伴侣")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])


#logo
st.logo("💬")

#创建的与ai大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

system_prompt = "你是一个代码老手，能够帮助我解决各种编程语言的代码问题。"


#输入框
prompt = st.chat_input("请输入您的问题：")
if prompt: #字符串会自动的转换成布尔值，如果存在就是True，如果不存在就是False
    st.chat_message("☺️").write(prompt)
    print("-------------------------这是用户输入的内容-------------------------", prompt)
    st.session_state.messages.append({"role":"☺️","content":prompt})


    # 与ai大模型进行交互
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果
    print("-------------------------这是大模型返回的内容-------------------------", response.choices[0].message.content)
    st.chat_message("AI").write(response.choices[0].message.content)
    st.session_state.messages.append({"role": "AI", "content": response.choices[0].message.content})
