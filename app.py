import streamlit as st
from transformers import pipeline

# Load pre-trained question-answering model (using Huggingface pipeline)
qa_pipeline = pipeline("question-answering")

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

# Placeholder for the user to enter queries
st.write("Ask any question regarding placements, and I will do my best to assist you.")

query = st.text_input("Enter your query:", help="E.g., What is the eligibility criteria for placement?")
context = """
Placement queries can vary, including eligibility criteria, placement process, company requirements, deadlines, and interview preparation. 
We support queries such as:
- What companies are visiting the campus this year?
- What are the eligibility criteria for placements?
- How should I prepare for interviews?
- What is the last date to register for placements?
"""

# If the user inputs a query, use the question-answering model to find the answer
if query:
    # Process query using QA model
    response = qa_pipeline({'question': query, 'context': context})
    answer = response['answer']
    
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
