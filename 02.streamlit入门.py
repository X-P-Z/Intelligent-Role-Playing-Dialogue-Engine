from asyncore import write

import streamlit as st

#配置整个页面


st.set_page_config(
    page_title="小企鹅（streamlit入门）",
    page_icon="🧊",
    #整个网页的布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': "https://www.baidu.com",
        'About': "这是一个streamlit的入门程序"
    }
)






#标题
st.title("streamlit 入门演示")
st.header("streamlit 一级标题")
st.subheader("streamlit 二级标题")

#段落文字
st.write("窗外的梧桐叶被风翻动，阳光从叶隙间筛落，在书页上跳跃成细碎的金斑。")
st.write("时光在这一刻变得缓慢而柔软——远处传来隐约的市声，近处有茶烟袅袅升起。")
st.write("我们总在奔赴远方的山海，却常常忘记了，生活的诗意就藏在这样寻常的午后：一杯温热的茶，一本未读完的书，和一个愿意停下来感受此刻的自己。")
st.write("万物皆有裂缝，那是光照进来的地方；而所有的等待，终将在某个不经意的瞬间，化作不期而遇的温暖。")


#图片
st.image("第三章/resources/企鹅.jpg")

#音频
st.audio("第三章/resources/news.mp3")

#视频
st.video("第三章/resources/news.mp4")

#logo
st.logo("第三章/resources/企鹅.jpg")

#表格
student_data = {
    "姓名":["张三","李四","王五","薛佩卓"],
    "学号":["s001","s002","s003","s004"],
    "语文成绩":[96,85,75,99],
    "数学成绩":[85,64,59,99],
    "英语成绩":[87,98,83,99],
}
st.table(student_data)

#输入框
#普通输入框
name = st.text_input("请输入您的姓名：")
st.write(f"您输入的姓名是：{name}")

#密码输入框
password = st.text_input("请输入您的密码：",type="password")
st.write(f"您输入的密码是：{password}")

#单选按钮
gender = st.radio("您的性别为：",["男","女","未知"],index=2)
st.write(f"您的性别是：{gender}")