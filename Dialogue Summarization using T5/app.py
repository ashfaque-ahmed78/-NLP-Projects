import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# -----------------------------
# Load Model
# -----------------------------
MODEL_PATH = "t5_dialogue_summarizer"

@st.cache_resource
def load_model():
    tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    return tokenizer, model, device

tokenizer, model, device = load_model()

# -----------------------------
# Summarization Function
# -----------------------------
def summarize(dialogue):

    text = "summarize: " + dialogue

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=60,
            num_beams=4,
            early_stopping=True,
            no_repeat_ngram_size=2
        )

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return summary

# -----------------------------
# UI
# -----------------------------

st.set_page_config(
    page_title="Dialogue Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Dialogue Summarization using T5")

st.write(
    "Paste any conversation below and click **Generate Summary**."
)

dialogue = st.text_area(
    "Enter Dialogue",
    height=300
)

if st.button("Generate Summary"):

    if dialogue.strip() == "":
        st.warning("Please enter a dialogue.")

    else:

        with st.spinner("Generating Summary..."):

            summary = summarize(dialogue)

        st.success("Summary Generated!")

        st.subheader("Summary")

        st.write(summary)