#impots
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader

#user definitions
def user_query_response(query):
    response = "I am learning yet"
    return response

#define vector store
def get_vector_store(url):
    loader = WebBaseLoader(url)
    print(loader)
    documents = loader.load()
    return documents

#app config
st.set_page_config(page_title='Chat with website', page_icon = "bot")
st.title("Ask me anything about the website")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [AIMessage(content='Hey, how can I help you?')]

#sidebar config
with st.sidebar:
    st.header('Add your website link')
    website_url = st.text_input('Website URL')

if website_url is None or website_url =="":
    st.info("Please enter website URL")
else:
    doc = get_vector_store(website_url)
    with st.sidebar:
        st.write(doc)
    #user input
    user_query = st.chat_input("Ask your questions here ...")
    if user_query is not None and user_query != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=user_query_response(user_query)))


    #conversation
    for message in st.session_state.chat_history:
        if isinstance(message,AIMessage):
            with st.chat_message('AI'):
                st.write(message.content)
        elif isinstance(message,HumanMessage):
            with st.chat_message('User'):
                st.write(message.content)