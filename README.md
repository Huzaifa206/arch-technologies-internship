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

**Intern:** Huzaifa Ahmed Siddiqui &nbsp;|&nbsp; **Intern ID:** `ARCH-2603-1066` &nbsp;|&nbsp; **Domain:** Generative AI &nbsp;|&nbsp; **Year:** 2026

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI Whisper](https://img.shields.io/badge/Whisper-412991?style=for-the-badge&logo=openai&logoColor=white)
![WandB](https://img.shields.io/badge/Weights%20&%20Biases-FFBE00?style=for-the-badge&logo=weightsandbiases&logoColor=black)

<br/>

---

</div>

## 📌 About This Repository

This repository contains all **four tasks** completed during my **Generative AI Engineering Internship** at **Arch Technologies**. Each task was a hands-on implementation built from scratch — from deploying a local LLM chat interface, to fine-tuning a medical reasoning model with QLoRA, building a full RAG pipeline, and finally creating an end-to-end speech-to-reasoning system.

The stack spans **Streamlit**, **Ollama**, **Unsloth**, **QLoRA**, **LangChain**, **FAISS**, **Whisper**, and **quantized transformer models** — all targeting real-world, memory-efficient AI deployment.

<br/>

---

## 👤 Intern Profile

| Field | Details |
|---|---|
| **Name** | Huzaifa Ahmed Siddiqui |
| **Intern ID** | `ARCH-2603-1066` |
| **Degree** | BS Artificial Intelligence — Bahria University, Karachi |
| **Organization** | Arch Technologies |
| **Domain** | Generative AI Internship |
| **GitHub** | [@huzaifa206](https://github.com/) |

<br/>

---

## 🗂️ Repository Structure

```
📦 arch-genai-internship/
├── 📁 Task-01-Streamlit-LLM-Interface/
│   ├── main.py
│   └── requirements.txt
│
├── 📁 Task-02-Medical-Finetuning-QLoRA/
│   └── Task_2.ipynb
│
├── 📁 Task-03-RAG-Dynamic-4bit/
│   └── Task_3.ipynb
│
├── 📁 Task-04-Speech-to-Reasoning/
│   └── Task4.ipynb
│
└── 📄 README.md
```

<br/>

---

## 🧩 Task Breakdown

<br/>

### `TASK 01` — Streamlit Interface for Local LLM Inference

> **File:** `main.py` &nbsp;|&nbsp; **Stack:** Python · Streamlit · Ollama · `qwen2.5:3b`

#### 📋 Overview
Built a fully interactive **Streamlit chat interface** that connects to a locally hosted LLM via **Ollama**, using the **Qwen 2.5 3B** model. Everything runs on-device with zero cloud dependency. The interface mimics a polished chat app with real-time streaming output.

#### ⚙️ Implementation Details

**Model & Backend**
- Model served locally via Ollama: `qwen2.5:3b`
- Used `ollama.chat()` with `stream=True` for real-time token-by-token streaming
- Full conversation history is passed on every call to preserve multi-turn context

**Frontend Features**
- **Streaming Response** — Tokens appear live with a `▌` cursor indicator while generating, replaced with the final clean output once done
- **Conversation History Panel** — `st.session_state.messages` maintains the full chat session and feeds it into every Ollama call for proper memory
- **Clear Conversation Button** — Sidebar button resets messages to `[]` and calls `st.rerun()` for an instant fresh session
- **Sidebar Info Panel** — Displays developer name (`Huzaifa`), intern ID (`ARCH-2603-1066`), and the active model
- **Error Handling** — Wrapped in `try/except`; shows a friendly `st.error()` if Ollama isn't running locally

#### 📦 Key Libraries
```
streamlit
ollama
```

#### ▶️ How to Run
```bash
# 1. Pull the model via Ollama
ollama pull qwen2.5:3b

# 2. Install dependencies
pip install streamlit ollama

# 3. Launch the app
streamlit run main.py
```

> Make sure Ollama is running in the background (`ollama serve`) before launching the app.

<br/>

---

### `TASK 02` — Medical Fine-tuning with QLoRA & Unsloth

> **File:** `Task_2.ipynb` &nbsp;|&nbsp; **Stack:** Unsloth · QLoRA · DeepSeek-R1-Distill-Llama-8B · WandB · Google Colab

#### 📋 Overview
Implemented a complete **QLoRA fine-tuning pipeline** on the **DeepSeek-R1-Distill-Llama-8B** model using Unsloth, trained on a medical chain-of-thought reasoning dataset. The entire workflow — dataset loading, tokenization, LoRA setup, training, adapter saving, and inference testing — is contained in a single Colab notebook.

#### ⚙️ Implementation Details

**Model Loading**
- Base model: `unsloth/DeepSeek-R1-Distill-Llama-8B`
- Loaded via **ModelScope** (`UNSLOTH_USE_MODELSCOPE=1`) as a reliable fallback to HuggingFace
- Quantized with `load_in_4bit=True`, `max_seq_length=2048`

**LoRA Adapter Configuration**
- Rank: `r=16`, Alpha: `lora_alpha=16`
- Target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- Dropout: `0`, Bias: `none` (Unsloth-optimized defaults)
- Gradient checkpointing: `"unsloth"` mode — critical for saving VRAM on long sequences

**Dataset**
- Source: `FreedomIntelligence/medical-o1-reasoning-SFT` (English config, first 500 samples)
- Prompt format: Instruction → Question → `<think>` Chain-of-Thought `</think>` → Response
- Tokenized in batched mode with `EOS_TOKEN` appended to every sample

**Training Config — `SFTTrainer` + `SFTConfig`**

| Parameter | Value |
|---|---|
| Batch size per device | `2` |
| Gradient accumulation | `4` steps (effective batch = 8) |
| Epochs | `1` |
| Learning rate | `2e-4` |
| Optimizer | `adamw_8bit` |
| LR Scheduler | `linear` |
| Precision | `bf16` (if supported), else `fp16` |
| Warmup steps | `5` |
| Logging | Every `10` steps → **WandB** (project: `medical-qlora-unsloth`) |

**Memory Monitoring**
- GPU name, total VRAM, and reserved VRAM logged before and after training
- LoRA-specific memory delta calculated and reported

**Adapter Saving & Inference**
- Adapter saved locally to `./medical_qlora_adapter/`
- Inference enabled with `FastLanguageModel.for_inference(model)` for 2x faster generation
- Tested on a clinical scenario: 65-year-old male with sudden right-sided weakness and speech difficulty

#### 📦 Key Libraries
```
unsloth · trl · peft · datasets · wandb · huggingface_hub · modelscope · torch
```

<br/>

---

### `TASK 03` — RAG Pipeline with Unsloth Dynamic 4-bit Quantization

> **File:** `Task_3.ipynb` &nbsp;|&nbsp; **Stack:** Unsloth · LangChain · FAISS · Sentence Transformers · Llama-3-8B-Instruct · Google Colab

#### 📋 Overview
Built a complete **Retrieval-Augmented Generation (RAG)** pipeline powered by a **4-bit quantized Llama-3-8B-Instruct** model. The system chunks and indexes documents into a FAISS vector store, retrieves the top relevant chunks at query time, and injects them into the LLM's prompt for grounded, document-faithful answers — running as an interactive Q&A assistant in Colab.

#### ⚙️ Implementation Details

**Model Loading**
- Model: `unsloth/llama-3-8b-Instruct-bnb-4bit` — pre-quantized 4-bit Instruct variant
- Loaded with `load_in_4bit=True`, `max_seq_length=2048`
- Immediately set to inference mode: `FastLanguageModel.for_inference(model)`

**Document Processing & Vector Store**
- Document: custom company knowledge base (embedded inline in the notebook)
- Chunked with `RecursiveCharacterTextSplitter`: `chunk_size=100`, `chunk_overlap=20`
- Embedded using `sentence-transformers/all-MiniLM-L6-v2` via `HuggingFaceEmbeddings`
- Indexed into a **FAISS** vector store; retriever returns top `k=2` relevant chunks per query

**RAG Pipeline — `ask_rag_pipeline(query)`**
1. Calls `retriever.invoke(query)` → fetches 2 semantically closest document chunks
2. Joins chunks into a `context` string
3. Constructs a grounded prompt: *"Use only the context below to answer. If the answer isn't there, say 'I don't know.'"*
4. Tokenizes and sends to CUDA, generates up to `150` new tokens
5. Decodes output and splits on `"Answer:\n"` to isolate the model's reply cleanly

**Interactive Loop**
- Runs a `while True` input loop for live Q&A directly in the Colab cell
- Exits on `"exit"` / `"quit"`, skips blank inputs

#### 📦 Key Libraries
```
unsloth · langchain · langchain-community · langchain-huggingface
faiss-cpu · sentence-transformers · pypdf · transformers · torch
```

<br/>

---

### `TASK 04` — Speech-to-Reasoning Pipeline with Whisper & Quantized LLM

> **File:** `Task4.ipynb` &nbsp;|&nbsp; **Stack:** Whisper-small · Qwen2.5-7B-Instruct · Unsloth · gTTS · Google Colab

#### 📋 Overview
Built an **end-to-end speech-to-reasoning pipeline** in a single Colab notebook. **OpenAI Whisper** transcribes a spoken audio clip into text, which is then passed to a **Qwen 2.5 7B** quantized reasoning model that generates a structured, step-by-step logical response. A `gTTS`-generated `.mp3` file serves as the test input, making the whole pipeline self-contained and reproducible.

#### ⚙️ Implementation Details

**Environment Setup**
- VRAM cleared upfront with `torch.cuda.empty_cache()` + `gc.collect()` before loading either model
- Both models loaded sequentially to keep peak memory usage manageable

**Step 1 — Whisper ASR**
- Model: `openai/whisper-small` via HuggingFace `pipeline("automatic-speech-recognition")`
- Pushed to CUDA with `torch.float16` for memory-efficient inference
- Returns a `{"text": "..."}` dict with the full transcription

**Step 2 — Quantized Reasoning LLM**
- Model: `unsloth/Qwen2.5-7B-Instruct-bnb-4bit` (dynamic 4-bit quantized)
- Loaded with `load_in_4bit=True`, `max_seq_length=2048`
- Inference optimized: `FastLanguageModel.for_inference(model)`

**Test Audio Generation**
- `gTTS` converts a medical text query to `sample_query.mp3`
- Audio player rendered inline in Colab via `IPython.display.Audio`
- Demo query: *"A patient presents with severe headache, stiff neck, high fever, and sensitivity to light — most likely diagnosis and immediate test to order?"*

**Full Pipeline — `speech_to_reasoning(audio_path)`**
1. **ASR** — Passes audio to Whisper, extracts `transcribed_text`
2. **Prompt Construction** — Wraps transcription in Qwen's chat template with system prompt: *"You are a logical reasoning medical assistant. Always break down your thought process step-by-step before providing a final answer."*
3. **Template Application** — `tokenizer.apply_chat_template()` with `add_generation_prompt=True`
4. **Generation** — Generates up to `500` new tokens with `use_cache=True`, `pad_token_id=tokenizer.eos_token_id`
5. **Output Cleaning** — Splits decoded output on `"assistant\n"` to isolate the model's reasoning chain and final answer

#### 📦 Key Libraries
```
unsloth · transformers · torch · gTTS · librosa · soundfile · IPython
```

<br/>

---

## 🛠️ Full Tech Stack

| Category | Tools / Models |
|---|---|
| **LLM Serving (Local)** | Ollama, `qwen2.5:3b` |
| **LLM Models (Colab)** | DeepSeek-R1-Distill-Llama-8B, Llama-3-8B-Instruct, Qwen2.5-7B-Instruct |
| **Efficient Fine-tuning** | Unsloth, QLoRA, PEFT, TRL (SFTTrainer + SFTConfig) |
| **Quantization** | BitsAndBytes 4-bit, Unsloth `bnb-4bit` variants |
| **RAG Stack** | LangChain, FAISS, Sentence Transformers (`all-MiniLM-L6-v2`) |
| **Speech Recognition** | OpenAI Whisper (`whisper-small`, fp16 on CUDA) |
| **TTS (Test Audio)** | gTTS (Google Text-to-Speech) |
| **Frontend** | Streamlit |
| **Experiment Tracking** | Weights & Biases — project: `medical-qlora-unsloth` |
| **Training Environment** | Google Colab (T4 / A100 GPU) |
| **Model Sources** | HuggingFace Hub, ModelScope |
| **Language** | Python |

<br/>

---

## 🚀 Getting Started

### Task 01 — Run Locally

```bash
# Pull the model
ollama pull qwen2.5:3b

# Install dependencies
pip install streamlit ollama

# Run the app
streamlit run main.py
```

### Tasks 02, 03, 04 — Run in Google Colab

1. Open the `.ipynb` in **Google Colab**
2. Go to **Runtime → Change runtime type → GPU** (T4 or better)
3. For Task 02: add `HF_TOKEN` and `wnb` keys under **Colab Secrets**
4. Run all cells sequentially from top to bottom

<br/>

---

## 📈 Skills Developed

```
Local LLM Deployment         ████████████░░  Advanced
Streamlit Development        ████████████░░  Advanced
QLoRA / PEFT Fine-tuning     ████████████░░  Advanced
4-bit Quantization           ███████████░░░  Intermediate–Advanced
RAG Pipeline Design          ███████████░░░  Intermediate–Advanced
LangChain + FAISS            ██████████░░░░  Intermediate
Whisper ASR Integration      ██████████░░░░  Intermediate
Multi-model Pipeline Design  ██████████░░░░  Intermediate
GPU Memory Optimization      █████████░░░░░  Intermediate
WandB Experiment Tracking    █████████░░░░░  Intermediate
```

<br/>

---

## 📄 License

This repository is for **educational and portfolio purposes** as part of the Arch Technologies Generative AI Internship. All tasks were completed under the supervision of Arch Technologies.

<br/>

---

<div align="center">

** Huzaifa Ahmed Siddiqui** &nbsp;·&nbsp; `ARCH-2603-1066` &nbsp;·&nbsp; BS Artificial Intelligence · Bahria University Karachi

*Generative AI Internship &nbsp;·&nbsp; Arch Technologies &nbsp;·&nbsp; 2026*

<br/>

⭐ *If you found this useful, consider starring the repository!* ⭐

</div>
