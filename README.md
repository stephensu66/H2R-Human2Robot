# H2R-Human2Robot

[English](README.md) | [中文](README.zh.md)

H2R-Human2Robot is an open-source initiative to build a real-world, voice-first robot inspired by Iron Man’s J.A.R.V.I.S.—a system that can listen, reason, and execute actions in real time.

## Vision
- Bring LLM-native intelligence to affordable hardware so hobbyists and researchers can prototype assistive robots.
- Keep the full speech → reasoning → action loop local-first to protect privacy and ensure low latency.
- Provide modular interfaces so teams can swap models, sensors, or robot bases without rewriting the entire stack.

## Key Capabilities
- **Streaming speech interface**: Always-on microphone pipeline tuned for Mandarin/English with FunASR paraformer-zh-streaming.
- **LLM-driven reasoning**: LocalAI / OpenAI-compatible adapters handle dialogue, intent parsing, and tool invocation.
- **Actionable outputs**: Commands can branch to realtime TTS (RealtimeTTS / fasterTTS) or to ROS2 / Python robot skills.
- **Human-in-the-loop friendly**: Clear logging hooks and state broadcasting so operators can visualize and intervene.

## System Architecture
```
🎙️ Speech Input
    ↓
🗣️ ASR  (FunASR paraformer-zh-streaming)
    ↓
💬 LLM Layer  (LocalAI / OpenAI-compatible)
   ┌──────────────┐
   │ Dialogue Core│
   │ Command Parser│
   └──────────────┘
    ↓                 ↓
🔊 TTS (RealtimeTTS / fasterTTS)    ⚙️ Control (ROS2 / Python APIs)
    ↓
🎧 Playback / Robot Actions
```

## Design Principles
- **Local-first**: All critical modules (ASR, LLM, TTS) run on-device (Mac or edge GPU) to stay private and responsive.
- **Modular adapters**: Standardized interfaces make it easy to swap in new models or connect to different robot bases.
- **ROS2-native control**: Python control layer exposes topic/service bridges for motion, sensing, and safety checks.
- **Open collaboration**: Encourages AI engineers, roboticists, and designers to co-build hardware + software experiences.

## Quick Start
1. Clone this repository and install Python dependencies for ASR, TTS, and ROS2 bindings (see upcoming setup scripts).
2. Configure model weights and API keys inside `config/` (planned) to point to LocalAI or OpenAI-compatible endpoints.
3. Launch the voice pipeline script to test end-to-end speech → LLM → speech.
4. Connect a ROS2-enabled robot or simulator to the control bridge to execute motion commands from the LLM outputs.

_Note: Detailed installation scripts and hardware wiring guides are being assembled. Contributions and early testing feedback are welcome._

## Roadmap
- ✅ **Phase 1 – Voice assistant prototype**: Offline speech + LLM loop on macOS.
- 🚧 **Phase 2 – Robot embodiment**: Map LLM intents to ROS2 motion primitives and safety rules.
- 🌐 **Phase 3 – Public showcase**: Release demo hardware specs, videos, and collaboration guide.

## Contributing
Open an issue or discussion with the robot platform you want to integrate, the model stack you prefer, or datasets you can share. Pull requests that improve documentation, add adapters, or extend safety tooling are especially welcome.
