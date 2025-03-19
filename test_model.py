from speechbrain.pretrained import EncoderClassifier

classifier = EncoderClassifier.from_hparams(
    source="speechbrain/emotion-recognition-wav2vec2-large",
    savedir="models/"
)


print("Model downloaded successfully!")
