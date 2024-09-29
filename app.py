import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Set the title and header of the web application
st.set_page_config(page_title="Placement Query Bot", layout="wide")
st.title("Placement Query Resolution Bot")
st.subheader("Your Personal Assistant for Placement-Related Queries")

# Business-themed banner
st.markdown(
    """
    <div style='text-align: center; padding: 10px; background-color: #00274d;'>
    <h2 style='color: white;'>Welcome to the Placement Query Assistant</h2>
    <p style='color: lightgrey;'>Get quick answers to your placement-related queries to make informed decisions</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Function to interact with OpenAI GPT
def get_openai_response(query):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use GPT-4 if it's available
        prompt=query,
        max_tokens=200,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Placeholder for the user to enter queries
st.write("Ask any question regarding placements, and I will do my best to assist you.")

query = st.text_input("Enter your query:", help="E.g., What is the eligibility criteria for placement?")

# If the user inputs a query, use the OpenAI API to get a real-time answer
if query:
    with st.spinner("Processing your query..."):
        answer = get_openai_response(query)
    
    # Display the answer
    st.markdown(f"**Query**: {query}")
    st.markdown(f"**Answer**: {answer}")

# Footer with contact information
st.markdown(
    """
    <hr>
    <div style='text-align: center;'>
    <p style='font-size: 12px;'>If you need further assistance, please contact us at <a href='mailto:support@placementbot.com'>support@placementbot.com</a>.</p>
    </div>
    """,
    unsafe_allow_html=True
)
