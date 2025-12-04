import streamlit as st
from ai_chef import get_smart_advice
from search_engine import search_food

st.set_page_config(page_title="福田 AI 饮食顾问")

# 侧边栏 - 用户档案表单
st.sidebar.header("👤 个人档案")
weight = st.sidebar.number_input("体重 (kg)", min_value=30.0, max_value=200.0, value=65.0, step=0.5)
goal = st.sidebar.selectbox("健身目标", options=["减脂", "增肌", "维持"])
status = st.sidebar.radio("当前状态", options=["刚练完", "休息日"])

# 聊天窗口
st.title("🥗 福田 AI 饮食顾问")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("有什么饮食需求？", "")
    submitted = st.form_submit_button("发送")

if submitted and user_input.strip():
    # 拼接档案信息与用户输入
    profile_info = f"用户体重：{weight}kg；健身目标：{goal}；当前状态：{status}。"
    full_query = f"{profile_info} 用户需求：{user_input}"
    # 获取AI推荐回复
    ai_reply = get_smart_advice(full_query)
    # 搜索 raw 推荐数据
    recommend_data = search_food(user_input, top_k=5)
    # 存入对话记录
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("ai", ai_reply))
    st.session_state.chat_history.append(("data", recommend_data))

# 聊天记录显示
for entry in st.session_state.get("chat_history", []):
    if entry[0] == "user":
        st.markdown(f"🧑‍💻 <b>你：</b> {entry[1]}", unsafe_allow_html=True)
    elif entry[0] == "ai":
        st.markdown(f"🤖 <b>AI：</b> {entry[1]}", unsafe_allow_html=True)
    elif entry[0] == "data":
        if entry[1]:  # entry[1]是list of dict
            import pandas as pd
            df = pd.DataFrame(entry[1])
            st.markdown("推荐的餐厅列表：")
            st.dataframe(df)
            if "price" in df.columns:
                st.markdown("价格分布：")
                st.scatter_chart(df, x="name", y="price")
        else:
            st.info("未检索到餐厅数据。")

