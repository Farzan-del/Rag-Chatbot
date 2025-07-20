from gtts import gTTS
import os

def convert_text_to_speech(text: str, filename="response.mp3") -> str:
    """
    Converts text to speech, saves it as MP3 file inside Data/Audio,
    and returns the file name (not full path, because we will serve via FastAPI).
    """
    audio_dir = os.path.join("Data", "Audio")
    os.makedirs(audio_dir, exist_ok=True)

    file_path = os.path.join(audio_dir, filename)

    try:
        tts = gTTS(text=text, lang="en")
        tts.save(file_path)
        print(f" [INFO] Audio saved at: {file_path}")
        return filename  # Return only filename for FastAPI URL
    except Exception as e:
        print(f" [ERROR] TTS conversion failed: {str(e)}")
        return ""
