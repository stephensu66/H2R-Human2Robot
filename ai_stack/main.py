
from dotenv import load_dotenv
from ai.agent_factory import build_agent
from voice import VoiceAgent, VoiceRuntime, Speaker, Listener

load_dotenv()

def main():
    agent = build_agent()
    
    runtime = VoiceRuntime()
    listener = Listener()
    speaker = Speaker(runtime)

    bot = VoiceAgent(agent, listener, speaker, runtime)
    bot.run()

if __name__ == "__main__":
    main()
