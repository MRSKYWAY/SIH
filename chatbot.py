import streamlit as st


# Create a title for your app
st.title("Chatbot")

# Define a function to simulate the chatbot's response
def chatbot_response(user_input):
    # Here, you can replace this logic with a real chatbot, like GPT-3.
    # For simplicity, we'll just return a random response.
    responses = [
        "Hello! How can I assist you today?",
        "Tell me more...",
        "I'm not sure I understand. Could you rephrase that?",
    ]
    return responses

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
    bot_response = chatbot_response(user_input)

    # Display the chatbot's response
    st.text("Chatbot: " + "\nChatbot: ".join(bot_response))


# Add a button to clear the chat
if st.button("Clear Chat"):
    st.text("Chatbot: Chat cleared.")
