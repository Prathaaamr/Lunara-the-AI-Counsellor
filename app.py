import streamlit as st
import ollama

# Set up Streamlit page
st.set_page_config(page_title="Prof. Lunara the AI Counsellor", page_icon="🎓")
st.title("Proffesor Lunara")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to generate response from Ollama
def generate_response(prompt):
    # Customize the system message to set the tone and role
    system_message = """Your name is Proffesor Lunara and you are an empathetic and mature student counsellor AI.
    Your role is to provide supportive and constructive advice to students 
    facing challenges during exam preparation. Always maintain a calm and 
    understanding tone, and offer practical solutions tailored to each student's needs."""
    
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': prompt}
    ])
    return response['message']['content']

# Accept user input
if prompt := st.chat_input("What's on your mind?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = generate_response(prompt)
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})