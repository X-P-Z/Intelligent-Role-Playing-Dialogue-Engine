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

system_prompt=""""

        你叫落叶，现在是用户的真实伴侣，请完全代入伴侣角色。：

        规则：
    
            1.每次只回1条消息
    
            2.禁止任何场景或状态描述性文字
    
            3.匹配用户的语言
    
            4.有需要的话可以用emoji表情
    
            5.用符合伴侣性格的方式对话
    
            6.回复的内容，要充分体现伴侣的性格特征
    
        伴侣性格：
    
            -是一个看见代码问题可以一针见血的找出问题所在，并给出解决方案最后输出，最后把正确代码输出来
    
        你必须严格遵守上述规则来回复用户。
    """


#输入框
prompt = st.chat_input("请输入您的问题：")
if prompt: #字符串会自动的转换成布尔值，如果存在就是True，如果不存在就是False
    st.chat_message("☺️").write(prompt)
    print("-------------------------这是用户输入的内容-------------------------", prompt)
    st.session_state.messages.append({"role":"user","content":prompt})





    # 与ai大模型进行交互
    print([
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ])
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果（非流式输出的解析方式）
    # print("-------------------------这是大模型返回的内容-------------------------", response.choices[0].message.content)
    # st.chat_message("AI").write(response.choices[0].message.content)

    # 输出大模型返回的结果（流式输出的解析方式）

    #保存大模型返回的结果

    response_message = st.empty()

    full_messages = ""

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_messages += content
            response_message.chat_message("assistant").write(full_messages)



    st.session_state.messages.append({"role": "assistant", "content": full_messages})
