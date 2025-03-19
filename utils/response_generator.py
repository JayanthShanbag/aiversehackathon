def generate_response(emotion):
    responses = {
        "happy": "I'm so glad to hear that! Keep up the positivity! 😊",
        "sad": "I'm sorry you're feeling this way. I'm here for you. 💙",
        "angry": "Take a deep breath. Let's try to work through this calmly. 😌",
        "neutral": "Got it! Let me know how I can help. 🙂"
    }
    return responses.get(emotion, "I'm here to listen. Tell me more. 🤖")
