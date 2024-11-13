import spacy
from transformers import AutoTokenizer, AutoModel
import torch


# Load spaCy model for advanced preprocessing
nlp = spacy.load('en_core_web_sm')

# Initialize the SciBERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
model = AutoModel.from_pretrained('allenai/scibert_scivocab_uncased')

# Helper function for advanced text preprocessing with spaCy
def preprocess_text_spacy(text):
    doc = nlp(text.lower())  # Process text with spaCy
    tokens = []

    for token in doc:
        # Remove stopwords, punctuation, and keep only nouns/adjectives/verbs
        if not token.is_stop and not token.is_punct and token.pos_ in ('NOUN', 'VERB', 'ADJ'):
            tokens.append(token.lemma_)  # Lemmatize the token (e.g., "running" -> "run")

    return ' '.join(tokens)


# Function to generate SciBERT embeddings
def get_embedding(text):

    text = preprocess_text_spacy(text)
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    # Get the embeddings from the model
    with torch.no_grad():
        outputs = model(**inputs)

    # Use the mean of the token embeddings as the sentence embedding
    embeddings = outputs.last_hidden_state.mean(dim=1)

    return embeddings.numpy()


