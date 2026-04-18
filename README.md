<div align="center">

<br/>

```
 █████╗ ██████╗  ██████╗██╗  ██╗    ████████╗███████╗ ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██║  ██║    ╚══██╔══╝██╔════╝██╔════╝██║  ██║
███████║██████╔╝██║     ███████║       ██║   █████╗  ██║     ███████║
██╔══██║██╔══██╗██║     ██╔══██║       ██║   ██╔══╝  ██║     ██╔══██║
██║  ██║██║  ██║╚██████╗██║  ██║       ██║   ███████╗╚██████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝
```

# Generative AI Internship — Task Portfolio

### Arch Technologies · Karachi, Pakistan

**Intern:** Muhammad Huzaifa &nbsp;|&nbsp; **Program:** Generative AI Engineering &nbsp;|&nbsp; **Year:** 2025

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![OpenAI Whisper](https://img.shields.io/badge/Whisper-412991?style=for-the-badge&logo=openai&logoColor=white)

<br/>

---

</div>

## 📌 About This Repository

This repository contains all **four tasks** completed during my **Generative AI Engineering Internship** at **Arch Technologies**. Each task was designed to build hands-on experience with modern AI tooling — from local LLM deployment and efficient fine-tuning, to retrieval-augmented generation and speech-to-reasoning pipelines.

The work spans a wide stack: **Streamlit**, **Ollama**, **Unsloth**, **QLoRA**, **FAISS**, **Whisper**, and quantized transformer models — all targeting real-world, memory-efficient AI deployment scenarios.

<br/>

---

## 👤 Intern Profile

| Field | Details |
|---|---|
| **Name** | Muhammad Huzaifa |
| **Degree** | BS Artificial Intelligence — Bahria University, Karachi |
| **Organization** | Arch Technologies |
| **Program** | Generative AI Engineering Internship |
| **Location** | Karachi, Pakistan |
| **GitHub** | [@huzaifa](https://github.com/) |

<br/>

---

## 🗂️ Repository Structure

```
📦 arch-genai-internship/
├── 📁 Task-01-Streamlit-LLM-Interface/
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
├── 📁 Task-02-Medical-Finetuning-QLoRA/
│   ├── medical_finetune_unsloth.ipynb
│   └── README.md
│
├── 📁 Task-03-RAG-Dynamic-4bit/
│   ├── rag_pipeline_unsloth.ipynb
│   └── README.md
│
├── 📁 Task-04-Speech-to-Reasoning-Pipeline/
│   ├── whisper_llm_pipeline.ipynb
│   └── README.md
│
└── 📄 README.md  ← you are here
```

<br/>

---

## 🧩 Task Breakdown

<br/>

### `TASK 01` — Streamlit Interface for Local LLM Inference

> **Stack:** Python · Streamlit · Ollama · REST API

#### 📋 Overview
Built a fully interactive **Streamlit web interface** that connects to a locally hosted large language model running via **Ollama**. The app provides a clean chat-style interface directly in the browser, with no cloud dependency — everything runs on-device.

#### ⚙️ What Was Implemented
- **Text Input Box** — User can type any query and submit it to the local LLM
- **Response Area** — Displays model-generated answers in real time using streaming output
- **Conversation History Panel** — Retains the full chat session so users can scroll back through prior exchanges
- **Reset Button** — Clears the conversation and starts a fresh session with one click
- **Ollama API Integration** — Streamlit communicates with the LLM backend through Ollama's local REST endpoint (`http://localhost:11434`)

#### 🧠 Key Concepts Learned
- Local LLM deployment and serving via Ollama
- Streamlit session state management for multi-turn conversations
- Building frontend-to-backend communication without a cloud dependency
- Designing a minimal but usable chat UI in pure Python

<br/>

---

### `TASK 02` — Medical Fine-tuning with QLoRA & Unsloth

> **Stack:** Python · Unsloth · QLoRA · Llama 3 / DeepSeek-R1 · Google Colab · HuggingFace

#### 📋 Overview
Implemented a full **QLoRA-based fine-tuning workflow** for a medical language model using **Unsloth's** optimized training framework inside Google Colab. The goal was to adapt a general-purpose base model to a specialized medical Q&A domain — efficiently, within Colab's VRAM constraints.

#### ⚙️ What Was Implemented
- **Dataset Loading** — Loaded a domain-specific medical dataset (clinical Q&A pairs) from HuggingFace
- **4-bit Quantization Setup** — Configured Unsloth to load the base model (Llama 3 / DeepSeek-R1) in **4-bit quantized** format to drastically reduce memory usage
- **LoRA Adapter Configuration** — Set up low-rank adaptation layers (rank, alpha, target modules) for parameter-efficient training
- **Tokenization Pipeline** — Applied instruction-format tokenization tailored to medical prompt templates
- **Epoch-based Training** — Ran the training loop with loss monitoring across multiple epochs
- **Memory Monitoring** — Tracked GPU VRAM usage in Colab throughout the training run
- **Adapter Saving & Testing** — Saved the fine-tuned LoRA adapter and tested it against new, unseen medical queries

#### 🧠 Key Concepts Learned
- PEFT (Parameter-Efficient Fine-Tuning) using LoRA
- 4-bit quantization for memory-efficient training (QLoRA)
- Domain adaptation of large language models
- Working within Colab's resource constraints using Unsloth's speed optimizations

<br/>

---

### `TASK 03` — RAG Pipeline with Unsloth Dynamic 4-bit Quantization

> **Stack:** Python · Unsloth · Dynamic 4-bit Quant · FAISS / LangChain · Google Colab

#### 📋 Overview
Built a complete **Retrieval-Augmented Generation (RAG)** pipeline inside a Google Colab notebook, powered by an **Unsloth dynamic 4-bit quantized** model. Instead of relying solely on a model's parametric knowledge, this system retrieves relevant document chunks at inference time and feeds them into the LLM as grounded context.

#### ⚙️ What Was Implemented
- **Dynamic Quant Model Loading** — Loaded an `unsloth-bnb-4bit` variant that selectively preserves precision for critical model parameters while quantizing the rest
- **Document Indexing** — Chunked and embedded domain-specific documents into a vector index for efficient retrieval
- **Retrieval Logic** — Built similarity-search retrieval to fetch the top-k most relevant chunks given a user query
- **RAG Integration** — Constructed a pipeline where retrieved chunks are injected into the LLM's prompt as context before generation
- **Memory Optimization** — Carefully managed VRAM usage to fit both the retriever and the quantized LLM within Colab's GPU limits
- **End-to-End Testing** — Validated grounded response generation against document-based queries

#### 🧠 Key Concepts Learned
- RAG architecture and its advantages over pure parametric generation
- Dynamic 4-bit quantization and its precision-preservation strategy
- Vector-based document retrieval (FAISS / embedding similarity)
- Prompt engineering for context injection in RAG setups

<br/>

---

### `TASK 04` — Speech-to-Reasoning Pipeline with Whisper & Quantized LLM

> **Stack:** Python · OpenAI Whisper · Unsloth Dynamic 4-bit · Llama / Qwen · Google Colab

#### 📋 Overview
Designed and implemented an **end-to-end speech-to-reasoning pipeline** in a single Google Colab notebook. The system first transcribes spoken audio using **OpenAI's Whisper** ASR model, then feeds the transcription directly into a **quantized reasoning LLM** (Unsloth dynamic 4-bit) to produce a logical, grounded response — turning voice into reasoning in one seamless flow.

#### ⚙️ What Was Implemented
- **Whisper ASR Integration** — Loaded and configured OpenAI Whisper to process raw audio input and produce accurate text transcriptions
- **Audio Preprocessing** — Handled audio encoding, sampling rate normalization, and batching for Whisper's input requirements
- **Quantized LLM Setup** — Loaded a fine-tuned, dynamic 4-bit quantized reasoning model (Llama or Qwen variant via Unsloth) with full GPU offloading
- **Transcription-to-Prompt Pipeline** — Passed Whisper's output directly as a structured prompt into the LLM's reasoning workflow
- **GPU Memory Management** — Coordinated VRAM usage across two models (Whisper + LLM) within Colab's constraints
- **End-to-End Demo** — Demonstrated the full pipeline working on a sample audio query, from spoken input to reasoned text output

#### 🧠 Key Concepts Learned
- Automatic Speech Recognition (ASR) with Whisper
- Multi-model pipeline design and GPU memory coordination
- Connecting ASR output to LLM prompt engineering
- Efficient batching and encoding strategies for audio-to-text-to-reasoning workflows

<br/>

---

## 🛠️ Tech Stack — Full Overview

| Category | Tools & Libraries |
|---|---|
| **LLM Serving** | Ollama, HuggingFace Transformers |
| **Fine-tuning** | Unsloth, QLoRA, PEFT, TRL |
| **Quantization** | BitsAndBytes (4-bit), Unsloth Dynamic Quant |
| **RAG** | FAISS, LangChain, Sentence Transformers |
| **Speech (ASR)** | OpenAI Whisper |
| **Frontend** | Streamlit |
| **Training Env** | Google Colab (T4 / A100 GPU) |
| **Languages** | Python |
| **Base Models** | Llama 3, DeepSeek-R1, Qwen |

<br/>

---

## 🚀 Getting Started

### Prerequisites
```bash
python >= 3.10
pip
git
ollama  # For Task 01
```

### Clone the Repository
```bash
git clone https://github.com/huzaifa/arch-genai-internship.git
cd arch-genai-internship
```

### Task 01 — Run Locally
```bash
cd Task-01-Streamlit-LLM-Interface
pip install -r requirements.txt

# Make sure Ollama is running with a model pulled
ollama pull llama3

# Launch the app
streamlit run app.py
```

### Tasks 02, 03, 04 — Run in Google Colab
Open the respective `.ipynb` notebook in Google Colab, set the runtime to **GPU (T4 or higher)**, and run all cells sequentially.

<br/>

---

## 📈 Skills Developed

```
Local LLM Deployment     ████████████░░  Advanced
Streamlit Development    ████████████░░  Advanced
QLoRA / PEFT             ███████████░░░  Intermediate–Advanced
4-bit Quantization       ███████████░░░  Intermediate–Advanced
RAG Pipeline Design      ██████████░░░░  Intermediate
Whisper ASR Integration  ██████████░░░░  Intermediate
GPU Memory Optimization  █████████░░░░░  Intermediate
Multi-model Pipelines    █████████░░░░░  Intermediate
```

<br/>

---

## 🏢 About Arch Technologies

**Arch Technologies** is a Karachi-based technology company focused on delivering AI-driven solutions and training the next generation of AI engineers in Pakistan. This internship program provided structured, project-based learning across the full generative AI stack.

<br/>

---

## 📄 License

This repository is for educational and portfolio purposes as part of an internship program. All tasks were completed under the supervision of **Arch Technologies**.

<br/>

---

<div align="center">

**Muhammad Huzaifa** · BS Artificial Intelligence · Bahria University Karachi

*Generative AI Internship · Arch Technologies · 2025*

<br/>

⭐ *If you found this useful, consider starring the repository!* ⭐

</div>
