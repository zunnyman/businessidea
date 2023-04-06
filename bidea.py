import openai
import streamlit as st
import os

# Set OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set Streamlit page config
st.set_page_config(page_title="Business Idea Generator", page_icon=":bulb:")

# Set Streamlit app title and description
st.title("Business Idea Generator")
st.markdown("Enter a topic and get 10 new business ideas.")

# Get user input
user_input = st.text_input("Enter a topic:")

if user_input:
    # Generate business ideas using OpenAI API
    prompt = f"Generate 10 new business ideas related to {user_input}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.6,
    )

    # Extract and format the business ideas from API response
    ideas = [
        "- " + idea.capitalize().strip() + "." for idea in response.choices[0].text.split("\n") if idea != ""
    ][:10]

    # Display the business ideas
    st.write("Here are 10 new business ideas based on your input:\n")
    for i, idea in enumerate(ideas):
        if i == 0:
            st.write(f"🔥 {idea}")
        elif i % 2 == 0:
            st.write(f"🌟 {idea}")
        else:
            st.write(f"✨ {idea}")
        st.write("")








