import torch
import librosa
import soundfile as sf
from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2Processor

# Load the pre-trained emotion model
model_name = "audeering/wav2vec2-large-robust-12-ft-emotion-msp-dim"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForSequenceClassification.from_pretrained(model_name)

def detect_emotion(audio_file):
    print("🔍 Detecting Emotion...")

    # Load the recorded audio file
    waveform, sample_rate = librosa.load(audio_file, sr=16000)
    inputs = processor(waveform, sampling_rate=sample_rate, return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

    emotions = ["happy", "sad", "angry", "neutral"]
    detected_emotion = emotions[predictions.argmax()]
    
    print(f"🎭 Detected Emotion: {detected_emotion}")
    return detected_emotion
