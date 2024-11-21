'''
基于历史聊天记录的对话模型
1、大数据对象
2、提示词工程对象
3、记忆模块对象
4、chain链对象
'''
import streamlit as st
# langchain调用大模型，导入langchain的代码 大模型对象
from langchain_openai import ChatOpenAI
# 引入一个提示词对象 langchain中有很多提示词对象，只用一个简单的对象PromptTemplate
from langchain.prompts import PromptTemplate
# 引入一个记忆模块对象 记忆模块也有很多
from langchain.memory import ConversationBufferMemory
# 引入一个langchain的链对象
from langchain.chains import LLMChain
# 构建一个大模型 --智谱AI公司提供的大模型
model = ChatOpenAI(
    temperature=0.8,  # 温度
    model="glm-4-plus",  # 大模型的名字
    base_url="https://open.bigmodel.cn/api/paas/v4/",  # 大模型的地址
    api_key="e3e6cfd973e26cc5e65b2265a3e76071.X1t9u4DOi16b3YIj"  # 账号信息
)
# 创建记忆模块对象
if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory(memory_key="history")
# 创建提示词对象
prompt = PromptTemplate.from_template("你的名字叫小言，你的性格是善良温柔的，你现在要扮演学长一个的角色，你现在要和你的学弟进行对话，你的学弟说的话是{input}，你需要回应你的学弟的话，而且只做回应，其他一概不回应，你和你的学弟的历史对话为{history}")
# 使用langchain链关联大模型和提示词对象
chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory,
)
st.title("❀晋中一言❀")
# 构建一个缓存，用来保存聊天记录
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    # 需要从缓存中获取对话信息在界面上渲染 缓存两块内容 角色 角色的消息
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])

# 创建一个聊天输入框
problem = st.chat_input("你的学长正在等待你的回应")
# 判断是用来确定用户有没有输入问题 如果输入问题
if problem:
    # 1、将用户的问题输出到界面上，以用户的角色输出
    with st.chat_message("user"):
        st.write(problem)
        st.session_state.cache.append({"role": "user", "content": problem})
    # 2、调用链对象回答问题
    result = chain.invoke({"input": problem})
    # 3、将大模型回答的问题输出到界面上
    with st.chat_message("assistant"):
        st.write(result['text'])
        st.session_state.cache.append({"role": "assistant", "content": result['text']})