import whisper
import os 
import asyncio
import aiofiles
# from pydub import AudioSegment
# from pydub.silence import split_on_silence
# Load Whisper model (you can choose: tiny, base, small, medium, large)

model = whisper.load_model("base")

def transcribe_audio(path):
    result = model.transcribe(path)
    return result["text"]

def transcribe_audio_simple(path):
    """
    Simple transcription function that processes the entire audio file at once.
    Whisper is good at handling longer audio files without chunking.
    """
    result = model.transcribe(path)
    return result["text"].strip()

async def Async_transcribe_audio(path):
    """
    Whisper with async
    """    
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, model.transcribe, path)
    return result["text"].strip()
    
# def get_large_audio_transcription_on_silence(path):

#     sound = AudioSegment.from_file(path)

#     chunks = split_on_silence(sound,
#                               min_silence_len= 500,
#                               silence_thresh= sound.dBFS-14,
#                               keep_silence=500,
                            
#     )
#     folder_name = "audio-chunks"

#     if not os.path.isdir(folder_name):
#         os.mkdir(folder_name)
#     whole_text = ""

#     for i, audio_chunk in enumerate(chunks, start=1):
#         chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
#         audio_chunk.export(chunk_filename,format="wav")

#         try:
#             text = transcribe_audio(chunk_filename)
        
#         except Exception as e :
#             print("Error:", str(e))

#         else:
#             text = f"{text.strip().capitalize()}."
#             print(chunk_filename, ":", text)
#             whole_text += text
        
#     return whole_text

path = "Project-Jarvis/it-had-been-a-wonderful-evening-and-what-i-needed-now-to-give-it-the-perfect-ending-was-a-bit-of-the-old-ludwig-van.wav"

# Option 1: Your Logic of chunking and transcribing 
#print("\nFull text (with chunking):", get_large_audio_transcription_on_silence(path))

# Option 2: My Simple transcription Logic of processing the entire audio file at once with Whisper
print("\nFull text (simple):", transcribe_audio_simple(path))

# Option 3: Async transcription
# print("\nFull text (async):", asyncio.run(Async_transcribe_audio(path)))
