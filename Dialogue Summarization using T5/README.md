# 📝 Dialogue Summarization using T5 Transformer

A Natural Language Processing (NLP) project that automatically generates concise summaries from lengthy conversations using a fine-tuned **T5-Small Transformer**. This project demonstrates the complete NLP workflow, including data preprocessing, tokenization, model fine-tuning, evaluation, inference, and deployment with Streamlit.

---

# 🚀 Project Overview

Dialogue Summarization is a Sequence-to-Sequence NLP task where long conversations are converted into short, meaningful summaries while preserving the key information.

This project fine-tunes Google's **T5-Small** model on the **SAMSum Dialogue Summarization Dataset** using the Hugging Face Transformers library.

---

# ✨ Features

- Fine-tuned T5-Small model
- Dialogue summarization
- Data preprocessing pipeline
- Tokenization using Hugging Face Tokenizer
- Transformer fine-tuning
- ROUGE evaluation
- Model saving & loading
- Streamlit Web Application
- Ready for deployment

---

# 🛠️ Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- T5 Transformer
- SentencePiece
- Evaluate
- ROUGE Score
- Streamlit
- Google Colab

---

# 📂 Project Structure

```text
Dialogue-Summarization-T5/
│
├── app.py
├── requirements.txt
├── README.md
├── Dialogue_Summarization_T5.ipynb
├── .gitignore
│
├── t5_dialogue_summarizer/
│   ├── config.json
│   ├── generation_config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── special_tokens_map.json
│   └── spiece.model
│
├── assets/
│   ├── app_demo.png
│   └── architecture.png
│
└── sample_data/
    └── sample_dialogues.txt
```

---

# 📊 Dataset

**Dataset:** SAMSum

The SAMSum dataset contains human-written conversations paired with human-written summaries. It is widely used for dialogue summarization research.

---

# 🔄 Workflow

1. Load Dataset
2. Data Exploration
3. Data Cleaning
4. Tokenization
5. Fine-Tune T5 Model
6. Evaluate with ROUGE
7. Save Model
8. Load Model
9. Generate Summary
10. Deploy with Streamlit

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Dialogue-Summarization-T5.git
```

## Move to Project Folder

```bash
cd Dialogue-Summarization-T5
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Streamlit

```bash
streamlit run app.py
```

---

# 📌 Example

## Input

```text
John: Hey Sarah, have you seen the latest smartwatch?

Sarah: Not yet.

John: It tracks heart rate, sleep, oxygen levels and stress.

Sarah: Sounds interesting but I don't really want another distraction.

John: The battery also lasts much longer.

Sarah: That's definitely a big improvement.
```

## Output

```text
John and Sarah discuss the features of a new smartwatch, including its health tracking capabilities and improved battery life.
```

---

# 📈 Model Information

| Property | Value |
|----------|-------|
| Model | T5-Small |
| Dataset | SAMSum |
| Framework | Hugging Face Transformers |
| Task | Dialogue Summarization |
| Training API | Hugging Face Trainer |

---

# 📊 Evaluation

The model was evaluated using:

- ROUGE-1
- ROUGE-2
- ROUGE-L

---

# 💻 Streamlit Application

The web application allows users to:

- Paste a dialogue
- Generate summaries instantly
- Test the fine-tuned T5 model
- Experience an intuitive interface

---

# 📸 Screenshots

## Home Page

> Add screenshot here

## Summary Output

> Add screenshot here

---

# 🔮 Future Improvements

- Fine-tune T5-Base / T5-Large
- Support long conversations
- Batch summarization
- REST API using FastAPI
- Docker deployment
- Hugging Face Spaces deployment

---

# 📚 Learning Outcomes

This project demonstrates knowledge of:

- Natural Language Processing
- Transformers
- Text Summarization
- Hugging Face Ecosystem
- Transfer Learning
- Sequence-to-Sequence Models
- ROUGE Evaluation
- Streamlit Deployment

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ashfaque Ahmed**

- GitHub: (https://github.com/ashfaque-ahmed78)
- LinkedIn: (https://www.linkedin.com/in/ashfaque-ahmed-29a05332b/)

---

# ⭐ Support

If you found this project helpful, please ⭐ the repository.
