import streamlit as st
import os
from openai import OpenAI
from datetime import  datetime
import json

#整个页面的布局
st.set_page_config(
    page_title="AI 智能伴侣",
    page_icon="🐧",
    # 整个网页的布局
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

#生成文件的名字，用时间来命名
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

#存储文件，把文件放在文件夹里面。
def save_session():
    if st.session_state.current_session:
        data = {
            "name" : st.session_state.name,
            "nature" : st.session_state.nature,
            "current_session" : st.session_state.current_session,
            "messages" : st.session_state.messages
        }

        if not os.path.exists("sessions"):
            os.mkdir("sessions")
        with open(f"sessions/{st.session_state.current_session}.json","w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=2)

#加载所有会话信息
def load_sessions():
    session_list = []
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True)
    return session_list

#加载指定的会话信息
def load_session(session_name):
    if os.path.exists(f"sessions/{session_name}.json"):
        with open(f"sessions/{session_name}.json","r",encoding="utf-8") as f:
            session_data = json.load(f)
            try:
                st.session_state.current_session = session_name
                st.session_state.messages = session_data["messages"]
                st.session_state.name = session_data["name"]
                st.session_state.nature = session_data["nature"]
            except Exception:
                st.error("加载会话失败！")

#删除指定的会话信息
def delete_session(session_name):
    if os.path.exists(f"sessions/{session_name}.json"):
        try:
            os.remove(f"sessions/{session_name}.json")
            if st.session_state.current_session == session_name:
                st.session_state.current_session = generate_session_name()
                st.session_state.messages = []
        except Exception:
            st.error("删除会话失败！")


# 大标题
st.title("AI 智能伴侣")


# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []
#初始化名字
if "name" not in st.session_state:
    st.session_state.name = "落叶"
#初始化性格
if "nature" not in st.session_state:
    st.session_state.nature = "是一个看见代码问题可以一针见血的找出问题所在，并给出解决方案最后输出，最后把正确代码输出来"
#初始化会话名字
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

st.text("-------------------------------------")
# 左侧的侧边栏
with st.sidebar:
    st.title("AI控制面板")
    if st.button("新建会话",width="stretch",icon="🦖"):
        # 保存当前会话
        save_session()

        # 创建一个新会话
        if st.session_state.messages:       #如果消息为空这里是False，如果有消息则是True
            st.session_state.current_session = generate_session_name()
            st.session_state.messages = []
            save_session()
            st.rerun()

    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1,col2 = st.columns([4,1])
        with col1:  #三目运算符 值1 if 条件 值2，先进行if判断。，如果是True则返回值1，如果是False，返回值2
            if st.button(session,width="stretch",icon="📄",key=f"load_{session}",type="primary" if st.session_state.current_session == session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            if st.button("",width="stretch",icon="💤",key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    st.divider()

    st.subheader("智能伴侣的信息")
    name = st.text_input("请输入伴侣的名称：",placeholder="请输入伴侣的名称",value=st.session_state.name,key="partner_name")
    nature = st.text_area("请输入伴侣的性格：",placeholder="请输入伴侣的性格",value=st.session_state.nature,key="partner_nature")

# 同步用户修改到 session_state（必须在读取 widget 之后立即执行）
st.session_state.name = name
st.session_state.nature = nature


st.text(f"当前会话: {st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# logo
st.logo("💬")

# 创建的与ai大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

system_prompt = f""""

        你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：

        规则：

            1.每次只回1条消息

            2.禁止任何场景或状态描述性文字

            3.匹配用户的语言

            4.有需要的话可以用emoji表情

            5.用符合伴侣性格的方式对话

            6.回复的内容，要充分体现伴侣的性格特征

        伴侣性格：

            -%s

        你必须严格遵守上述规则来回复用户。
    """

# 输入框
prompt = st.chat_input("请输入您的问题：")
if prompt:  # 字符串会自动的转换成布尔值，如果存在就是True，如果不存在就是False
    st.chat_message("☺️").write(prompt)
    print("-------------------------这是用户输入的内容-------------------------", prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与ai大模型进行交互
    print([
        {"role": "system", "content": system_prompt},
        *st.session_state.messages
    ])
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.name, st.session_state.nature)},
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

    # 保存大模型返回的结果

    response_message = st.empty()

    full_messages = ""

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_messages += content
            response_message.chat_message("assistant").write(full_messages)

    st.session_state.messages.append({"role": "assistant", "content": full_messages})
    save_session()
