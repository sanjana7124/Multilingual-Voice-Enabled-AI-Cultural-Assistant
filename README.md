# LinguaVoice AI: Multilingual-Voice-Enabled-AI-Cultural-Assistant
It is a sophisticated, voice-enabled communication platform engineered to dismantle digital barriers and foster universal accessibility. By prioritizing auditory interaction over traditional text-based interfaces, this project specifically addresses the needs of users with visual impairments, literacy challenges, or regional language preferences.

# 🌟 Key FeaturesAudio-First Accessibility: 
Integrated real-time Text-to-Speech (TTS) and Speech Recognition provide a hands-free experience for blind or low-vision users.
Multilingual Eradication of Barriers: Supports major Indian regional languages including Kannada, Malayalam, Bengali, Tamil, Hindi, Marathi, and Punjabi.
Talking Avatar UI: A professional interface where the assistant’s avatar enlarges during audio playback to provide intuitive visual feedback.
Cultural Representation: The UI dynamically displays state-specific traditional attire—such as Ilkal, Kasavu, or Paithani sarees—corresponding to the selected language.
Contextual AI Intelligence: Powered by a FastAPI backend and OpenAI’s GPT models for culturally sensitive and accurate responses.

# 🛠️ Tech Stack
Component: Technology
Frontend: React.js, Tailwind CSSBackendFastAPI (Python)
AI Model: OpenAI GPT-4o-miniVoice APIsWeb Speech API (Recognition & Synthesis)

# 🚀 Getting Started. 
PrerequisitesNode.js (v18+)
Python 3.10+
OpenAI API Key
Backend Setup
Bash# 
Navigate to backend folder
cd backend
pip install fastapi uvicorn openai pydantic
Run the server (defaults to port 8000)
uvicorn main:app -reload
3.⁠ ⁠Frontend SetupBash# Navigate to project folder
npm install
Start the development server on port 5174
npm run dev  - port 5174

Note: Ensure your package.json dev script is set to port 5174 to avoid localhost conflicts.

# 📸 Interface Design.
The application uses a "Glassmorphism" design style for a modern, professional look. When the Audio Button is clicked:The SpeechSynthesis API is triggered in the native language.The Avatar image smoothly scales up to 1.25x its size.A glowing accent border appears around the assistant to indicate active speaking.
# 🤝 Accessibility Mission.
Our goal is to ensure that language and physical disabilities are no longer a barrier to digital information. By converting complex data into native-tongue audio, we provide a pathway for every user to interact with AI with dignity and ease.
