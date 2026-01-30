
import threading

class VoiceAgent:
    def __init__(self, agent, listener, speaker, runtime):
        self.agent = agent
        self.current_say_process = None
        self.interrupt_event = threading.Event()
        self.listener = listener

    def run(self):
        while True:
            # 1. 听人说话
            human_text = self.listener.listen()
            if not human_text:
                continue

            print("Human:", human_text)

            # 2. 打断当前说话
            self.runtime.interrupt_event.set()
            self.speaker.stop()
            self.runtime.interrupt_event.clear()

            # 3. 新线程处理这一轮
            threading.Thread(
                target=self.handle_turn,
                args=(human_text,)
            ).start()

    def handle_turn(self, text):
        if self.runtime.interrupt_event.is_set():
            return

        resp = self.agent.invoke(
            {"messages": [{"role": "user", "content": text}]}
        )

        reply = resp["messages"][-1].content

        if self.runtime.interrupt_event.is_set():
            return

        self.speaker.speak(reply)