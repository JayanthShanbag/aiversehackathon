import speech_recognition as sr
import wave

def record_and_transcribe():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    audio_file = "recorded_audio.wav"  # Save the recorded audio

    print("🎙️ Recording... Speak now...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Save the recorded audio
    with open(audio_file, "wb") as f:
        f.write(audio.get_wav_data())

    print("📝 Transcribing audio...")
    try:
        transcription = recognizer.recognize_google(audio)
        print(f"📝 Transcribed Text: {transcription}")
    except sr.UnknownValueError:
        transcription = ""
        print("❌ Could not understand audio.")
    except sr.RequestError:
        transcription = ""
        print("❌ API request failed.")

    return transcription, audio_file  # Return transcription + audio file path
