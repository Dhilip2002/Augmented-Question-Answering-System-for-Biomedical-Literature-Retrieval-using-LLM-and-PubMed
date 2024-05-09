import streamlit as st
import pyrebase
from typing import List
from haystack import Document
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack import Pipeline
from haystack.components.generators import HuggingFaceTGIGenerator
from haystack import component
from pymed import PubMed
from dotenv import load_dotenv
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import subprocess

# Insert the line to save the Hugging Face API token
subprocess.run(["python", "-c", "from huggingface_hub.hf_api import HfFolder; HfFolder.save_token('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')"], check=True)

# Set Streamlit page config
st.set_page_config(page_title="Biomedical Q&A with LLM", page_icon="🧬", layout="wide")

load_dotenv()

# Load the model and tokenizer with BitsAndBytesConfig for 4-bit quantization
base_model_id = "mistralai/Mistral-7B-Instruct-v0.1"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

model = AutoModelForCausalLM.from_pretrained(base_model_id, quantization_config=bnb_config)
tokenizer = AutoTokenizer.from_pretrained(base_model_id, use_fast=True)

def documentize(article):
    return Document(content=article.abstract, meta={'title': article.title, 'keywords': article.keywords})

@component
class PubMedFetcher():

    @component.output_types(articles=List[Document])
    def run(self, queries: list[str]):
        cleaned_queries = queries[0].strip().split('\n')

        articles = []
        try:
            for query in cleaned_queries:
                response = pubmed.query(query, max_results=1)
                documents = [documentize(article) for article in response]
                articles.extend(documents)
        except Exception as e:
            st.error(f"Couldn't fetch articles for queries: {queries}")
            st.error(e)
        return {'articles': articles}

pubmed = PubMed(tool="Haystack2.0Prototype", email="dummyemail@gmail.com")


def ask(question):
    # Fetch articles related to the question
    fetcher = PubMedFetcher()
    articles = fetcher.run([question])['articles']
    
    # Prepare the input for the LLM
    input_text = ""
    for article in articles:
        input_text += f"Title: {article.meta['title']}\n\nAbstract: {article.content}\n\nKeywords: {', '.join(article.meta['keywords'])}\n\n"
    
    # Tokenize the input
    inputs = tokenizer.encode(input_text, return_tensors="pt")
    
    # Generate the output
    outputs = model.generate(input_ids=inputs, max_length=750, num_return_sequences=1)
    
    # Decode the output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract and format the response
    response_parts = response.split('\n')
    formatted_response = ""
    for part in response_parts:
        if part.startswith("Title:") or part.startswith("Abstract:") or part.startswith("Keywords:"):
            formatted_response += part + "\n\n"
    
    return formatted_response.strip()


# Firebase configuration
firebase_config = {
"apiKey": "AIzaSyBFHP15ZoE7U7SkOzV0xNatIRoF0cV_VcA",
"authDomain": "project-test-7aeba.firebaseapp.com",
"databaseURL": "https://project-test-7aeba-default-rtdb.asia-southeast1.firebasedatabase.app",
"projectId": "project-test-7aeba",
"storageBucket": "project-test-7aeba.appspot.com",
"messagingSenderId": "422774618569",
"appId": "1:422774618569:web:b87f6b929f17e79d011018"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth() # Get authentication
db = firebase.database()

# Streamlit App
st.title("Augmented Question-Answering System For Biomedical Literature Retrieval Using Language Models And PubMed Integration")
st.markdown("Ask a question about BioMedical and get an answer from a friendly AI assistant.")

question = st.text_input("Ask your question here:")
if st.button("Submit"):
    if question:
        response = ask(question)
        # Store response in Firebase
        db.child("responses").push({"question": question, "response": response})
        st.markdown(response, unsafe_allow_html=True)

# Display examples in bold
st.markdown("**Examples:**")
examples=[["How are mRNA vaccines being used for cancer treatment?"],["Suggest me some Case Studies related to Pneumonia."],["Tell me about HIV AIDS."],["Suggest some case studies related to Auto Immune Disorders."],["How to treat a COVID infected Patient?"]]
for example in examples:
    st.markdown(f"- **{example[0]}**")

# Launch Streamlit app
if __name__ == "__main__":
    st.write("")
