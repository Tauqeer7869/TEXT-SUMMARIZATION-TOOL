from transformers import pipeline

# Load model once
summarizer = pipeline("summarization")

def abstractive_summary(text):
    if len(text) > 1024:
        text = text[:1024]  # Transformers have max token limits
    summary = summarizer(text, max_length=120, min_length=180, do_sample=False)
    return summary[0]['summary_text']
