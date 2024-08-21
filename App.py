import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyB3p-msB4w6fo5-tDmw-O-FkfOk9LiaYyw")

# Streamlit app title
st.title("Unity: Your Personal Assistant")

# Streamlit input widget with a friendly prompt
text = st.text_input("How can I assist you today?")

# Process the input if provided
if text:
    # Create the GenerativeModel object
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    
    # Send the message and get the response
    response = chat.send_message(text)
    
    # Display the response with some styling
    st.subheader("Response:")
    st.write(response.text)
