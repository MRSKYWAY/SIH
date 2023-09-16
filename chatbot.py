import streamlit as st
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import random
import time

model_path = "/Users/maymay/Desktop/BARD API/model"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPTNeoForCausalLM.from_pretrained(model_path)

def chat_with_bot(user_input):
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    response_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
    bot_response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return bot_response


st.title("Chatbot")


st.markdown(
    """
    <style>
    .stTextInput {
        margin-top: 400px; /* Add desired margin or padding here */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Send a message"):
    
    st.chat_message("user").markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"

with st.chat_message("user"):
    st.markdown(prompt)

with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""
    assistant_response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    
    for chunk in assistant_response.split():
        full_response += chunk + " "
        time.sleep(0.05)
        
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)

st.session_state.messages.append({"role": "assistant", "content": full_response})


    
if st.button("Clear Recent Chat"):
    st.session_state.messages.clear()
    st.text("Chatbot: Chat cleared.")
