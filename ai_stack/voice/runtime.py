
import threading

# 全局变量，阻断时使用
# 保存共享状态（当前轮次）
class VoiceRuntime:
    def __init__(self):
        self.current_say_process = None
        self.interrupt_event = threading.Event()
