# Generative AI Internship Projects

This repository contains two projects completed as part of my **Generative AI Internship**.  
The projects focus on working with **Large Language Models (LLMs)**, building user interfaces for local models, and performing **efficient fine-tuning using QLoRA with Unsloth**.

---

# 📌 Project 1: Streamlit Interface for a Local LLM (Ollama)

## Overview
This project builds an **interactive Streamlit web interface** that connects to a **locally installed Large Language Model (LLM)** running through **Ollama**.

The application allows users to input prompts and receive responses from the local LLM in real time.

---

## Features

- Simple and clean **Streamlit UI**
- **Text input box** for user queries
- **Response display area**
- **Conversation history panel**
- **Reset conversation button**
- Connection to a **local LLM using Ollama API**

---

## Tech Stack

- Python
- Streamlit
- Ollama
- Local LLM (e.g., Llama 3, Mistral, etc.)

---

## Project Structure

```
streamlit-ollama-llm/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Huzaifa206/arch-technologies-internship
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Download from:

https://ollama.com

Then run a model:

```bash
ollama run llama3
```

---

## Run the Streamlit App

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## How It Works

1. The user enters a query in the Streamlit interface.
2. The query is sent to the **Ollama API endpoint**.
3. Ollama processes the prompt using the local LLM.
4. The response is returned and displayed in the UI.
5. The conversation history is stored in the session state.

---

# 📌 Project 2: Medical Fine-Tuning Using QLoRA with Unsloth

## Overview

This project demonstrates **efficient fine-tuning of a medical language model** using **QLoRA (Quantized Low Rank Adaptation)** with **Unsloth** on **Google Colab**.

The goal is to adapt a base LLM to answer **medical-related queries** by training it on a **clinical question-answer dataset**.

---

## Key Concepts Used

- **QLoRA (Quantized Low-Rank Adaptation)**
- **Parameter Efficient Fine Tuning (PEFT)**
- **4-bit Quantization**
- **Unsloth Framework**
- **Medical Dataset Fine-Tuning**

---

## Tools & Technologies

- Google Colab
- Python
- PyTorch
- HuggingFace Transformers
- Unsloth
- PEFT
- BitsAndBytes

---

## Base Models Used

Examples:

- **Llama 3**
- **DeepSeek-R1**

---

## Workflow

### 1. Load Base Model

Load a pretrained model using **Unsloth optimized loading** for memory efficiency.

### 2. Load Medical Dataset

Example dataset:

- Clinical Question & Answer pairs
- Medical instruction datasets

### 3. Tokenization

Convert text data into tokens compatible with the base model tokenizer.

### 4. Configure QLoRA

Set up:

- 4-bit quantization
- LoRA rank
- LoRA alpha
- Dropout

### 5. Training

Train the model adapters using:

- Epoch-based training
- Memory monitoring in Colab
- Gradient checkpointing

### 6. Save Adapter

Save the **fine-tuned LoRA adapter** separately from the base model.



## Colab Notebook

The training workflow was implemented using **Unsloth’s prebuilt Colab notebooks**.

Reference tutorial:

https://youtu.be/qcNmOItRw4U

---

## Learning Outcomes

Through these projects I learned:

- How to run **LLMs locally using Ollama**
- Building **interactive AI applications with Streamlit**
- Using **QLoRA for efficient LLM fine-tuning**
- **Memory optimization with 4-bit quantization**
- Implementing **PEFT workflows**
- Adapting LLMs to **domain-specific tasks (medical AI)**

---

# 🚀 Future Improvements

- Add **streaming responses** in Streamlit UI
- Add **chat-style interface**
- Deploy the Streamlit app
- Use larger **medical datasets**
- Integrate **RAG for medical knowledge retrieval**

---

# 👨‍💻 Author

**Huzaifa Ahmed Siddiqui**

AI Student | Generative AI Enthusiast | Frontend Developer  

---

# 📄 License

This project is for **educational and research purposes**.
