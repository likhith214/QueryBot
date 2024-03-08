import streamlit as st
from streamlit_chat import message
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain, ConversationChain
from langchain.chains.conversation.memory import (
    ConversationBufferMemory,
    ConversationSummaryMemory,
    ConversationBufferWindowMemory,
)
import re




import string
from googlesearch import search

if 'conversation' not in st.session_state:
    st.session_state['conversation'] = None

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

if 'API_KEY' not in st.session_state:
    st.session_state['API_KEY'] = ''


def remove_unwanted_patterns(response):
    cleaned_response = re.sub(r'<\s*p\W*a\W*d\s*>', '', response, flags=re.IGNORECASE)
    cleaned_response = ' '.join(word for word in cleaned_response.split() if not (word.startswith('<') or word[0] in string.punctuation))
    return cleaned_response.strip()


def get_google_results(query, num_results=3):
    results = []
    for result in search(query, num=5): 
        results.append(result)
        if len(results) == num_results:
            break
    return results



def get_response(user_input, api_key):
    if st.session_state['conversation'] is None:
        llm = HuggingFaceHub(
            repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
            model_kwargs={"temperature": 0.9, "max_length": 64},

            huggingfacehub_api_token=api_key
        )

        st.session_state['conversation'] = ConversationChain(
            llm=llm,
            verbose=True,
            memory=ConversationBufferMemory()
        )

    # Get the raw response from the model
    raw_response = st.session_state['conversation'].predict(input=user_input)

    # Clean the response to remove unwanted patterns
    cleaned_response = remove_unwanted_patterns(raw_response)

    # Get Google search results
    google_results = get_google_results(user_input)

    # Include Google search results in the response
    cleaned_response += "\n\n**Google Search Results:**\n"
    for idx, result in enumerate(google_results, start=1):
        cleaned_response += f"{idx}. [{result}]({result})\n"

    print(st.session_state['conversation'].memory.buffer)

    return cleaned_response

# Setting page title and header 
st.set_page_config(page_title="ImartiChat", page_icon="🤖")
st.markdown("<h1 style='text-align: center;> How Can I assist you? </h1>", unsafe_allow_html=True)

st.sidebar.title("🤖")
st.session_state['API_KEY'] = st.sidebar.text_input("What's your API key?", type="password")





response_container = st.container()

#Container for user input text box
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("Your question goes here:", key="input", height=100)
        submit_button = st.form_submit_button(label="Send")
        if submit_button:
            st.session_state['messages'].append(user_input)
            model_response = get_response(user_input,st.session_state['API_KEY'])
            st.session_state['messages'].append(model_response)

            with response_container:
                for i in range(len(st.session_state['messages'])):
                    if (i % 2) == 0:
                        message(st.session_state['messages'][i], is_user = True, key=str(i) +"_user")
                    else:
                        message(st.session_state['messages'][i], key=str(i) +"_AI")
