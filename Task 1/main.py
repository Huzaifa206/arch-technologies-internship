import streamlit as st
import ollama

# Set up the page configuration
st.set_page_config(page_title="Local Ollama Chat", page_icon="🦙", layout="centered")
st.title("🦙 Chat with Local LLM Model(qwen 2.5) using Ollama")

# --- SIDEBAR ---
with st.sidebar:
    st.header("Project Info")
    st.markdown("**Developer:** Huzaifa")
    st.markdown("**Intern ID:** ARCH-2603-1066")
    
    st.markdown("---")
    
    st.header("Settings")
    
    # You can type the name of the model you pulled in Ollama (e.g., llama3, mistral, phi3)
    model_name = "qwen2.5:3b"
    # Display the current model name as plain text
    st.markdown(f"**Active Model:** `{model_name}`")
    
    st.markdown("---")
    
    # Reset Conversation Button
    if st.button("Clear Conversation", type="primary"):
        st.session_state.messages = []
        st.rerun()


# --- INITIALIZE SESSION STATE ---
# This keeps track of the chat history across reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- DISPLAY CHAT HISTORY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CHAT INPUT & LLM CALL ---
if prompt := st.chat_input("Ask me anything..."):
    
    # 1. Add user's prompt to session state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Generate and display the assistant's response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            # Stream the response directly from the local Ollama instance
            stream = ollama.chat(
                model=model_name,
                messages=st.session_state.messages,
                stream=True
            )
            
            # Update the placeholder text as chunks arrive
            for chunk in stream:
                full_response += chunk['message']['content']
                response_placeholder.markdown(full_response + "▌")
            
            # Remove the blinking cursor once streaming is done
            response_placeholder.markdown(full_response)
            
            # 3. Add the final response to the conversation history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Failed to connect to Ollama. Ensure it is running locally. Error: {e}")