import subprocess
import time

class Speaker:
  def __init__(self, runtime, voice="Ting-Ting"):
        self.runtime = runtime
        self.voice = voice

  def stop(self):
        proc = self.runtime.current_say_process
        if proc and proc.poll() is None:
            proc.terminate()
        self.runtime.current_say_process = None

  def speak(self, text):
        # 停掉上一次
        if self.runtime.current_say_process:
            self.stop()

        cmd = ["say", "-v", self.voice, text]
        proc = subprocess.Popen(cmd)
        self.runtime.current_say_process = proc

        # 轮询中断
        while proc.poll() is None:
            if self.runtime.interrupt_event.is_set():
                self.stop()
                return
            time.sleep(0.05)

