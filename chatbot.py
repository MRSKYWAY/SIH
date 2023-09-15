import streamlit as st
from transformers import GPTNeoForCausalLM, GPT2Tokenizer

model_path = "/Users/maymay/Desktop/BARD API/model"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPTNeoForCausalLM.from_pretrained(model_path)

def chat_with_bot(user_input):
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    response_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
    bot_response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return bot_response

# Create a title for your app
st.title("Chatbot")

# # Define a function to simulate the chatbot's response
# def chatbot_response(user_input):
#     # Here, you can replace this logic with a real chatbot, like GPT-3.
#     # For simplicity, we'll just return a random response.
#     responses = [
#         "Hello! How can I assist you today?",
#         "Tell me more...",
#         "I'm not sure I understand. Could you rephrase that?",
#     ]
#     return responses

# Add CSS to create space (padding)
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

# Create a text input box for the user to enter messages
user_input = st.text_input("You:", "")

# Check if the user has entered a message
if user_input:
    # Display the user's message
    st.text("You: " + user_input)

    # Get the chatbot's response
    bot_response = chat_with_bot(user_input)

    # Display the chatbot's response
    st.text("Chatbot: " + bot_response)

    # Add the user's message to the chat history
    # chat_history.append(("User", user_input))

# Display the chat history
# st.subheader("Chat History:")
# for speaker, message in chat_history:
#     st.text(f"{speaker}: {message}")

# Add a button to clear the chat
if st.button("Clear Chat"):
    st.text("Chatbot: Chat cleared.")