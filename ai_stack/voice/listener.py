# voice/listener.py

import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import time

class Listener:
    def __init__(self, model_path="vosk-model-small-cn-0.22", silence_timeout=1.5):
        self.model = Model(model_path)
        self.silence_timeout = silence_timeout

    def listen(self) -> str:
      rec = KaldiRecognizer(self.model, 16000)
      q = queue.Queue()


      def callback(indata, frames, time, status):
          q.put(bytes(indata))
      
      print("🎤 开始说话（Ctrl+C 结束）")

      text_buffer = ""
      last_voice_time = time.time()

      with sd.RawInputStream(
            samplerate=16000,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=callback
        ):
            while True:
                try:
                    data = q.get(timeout=0.1)
                except queue.Empty:
                    # 超时，检查是否静默结束
                    if time.time() - last_voice_time > self.silence_timeout and text_buffer.strip():
                        break
                    continue

                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    sentence = result.get("text", "")
                    if sentence:
                        text_buffer += " " + sentence
                        last_voice_time = time.time()
                else:
                    partial = json.loads(rec.PartialResult())
                    if partial.get("partial"):
                        last_voice_time = time.time()

            return text_buffer.strip()