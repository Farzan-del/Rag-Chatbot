# import speech_recognition as sr

# def convert_speech_to_text(audio_file: str) -> str:
#     """
#     Converts speech from an audio file to text using Google's Speech Recognition API.
#     :param audio_file: Path to the audio file (WAV or MP3)
#     :return: Recognized text as string
#     """
#     recognizer = sr.Recognizer()
#     try:
#         with sr.AudioFile(audio_file) as source:
#             audio = recognizer.record(source)  # Read the entire audio file
#             text = recognizer.recognize_google(audio)  # Use Google Speech API
#             print(f" [INFO] Speech recognized: {text}")
#             return text
#     except sr.UnknownValueError:
#         print(" [ERROR] Could not understand audio")
#         return ""
#     except sr.RequestError as e:
#         print(f" [ERROR] STT service error: {e}")
#         return ""
#updated code is below

import speech_recognition as sr

def convert_speech_to_text(audio_file: str) -> str:
    """
    Converts speech from an audio file to text using Google's Speech Recognition API.
    :param audio_file: Path to the audio file (WAV or MP3)
    :return: Recognized text as string
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)  # Read the entire audio file
            text = recognizer.recognize_google(audio)  # Use Google Speech API
            print(f" [INFO] Speech recognized: {text}")
            return text
    except sr.UnknownValueError:
        print(" [ERROR] Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f" [ERROR] STT service error: {e}")
        return ""


