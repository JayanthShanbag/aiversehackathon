import os
from utils.speech_recognition import record_and_transcribe
from utils.emotion_detection import detect_emotion
import utils.response_generator as rg


from utils.text_to_speech import text_to_speech

def main():
    print("🎤 Starting AI Voice Assistant...")

    # Step 1: Record and Transcribe Speech
    transcription, audio_file = record_and_transcribe()

    if not transcription:
        print("❌ No speech detected. Exiting...")
        return

    # Step 2: Detect Emotion from Audio
    emotion = detect_emotion(audio_file)

    # Step 3: Generate AI Response Based on Transcription & Emotion
    response = rg.generate_response(emotion)


    # Step 4: Convert AI Response to Speech
    text_to_speech(response)

    print(f"🗣️ Transcription: {transcription}")
    print(f"🎭 Detected Emotion: {emotion}")
    print(f"💬 AI Response: {response}")

    # Cleanup: Delete the recorded audio file
    if os.path.exists(audio_file):
        os.remove(audio_file)
        print("🗑️ Temporary audio file deleted.")

if __name__ == "__main__":
    main()
