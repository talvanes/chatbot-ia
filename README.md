# 🤖 AI Chatbot with OpenAI Integration

A modern, interactive chatbot application built with Streamlit and OpenAI's GPT API, featuring real-time conversational AI capabilities and a clean, intuitive user interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--5-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- **Real-time AI Conversations**: Seamless integration with OpenAI's GPT-5 Nano model for intelligent responses
- **Persistent Chat History**: Maintains conversation context throughout the session
- **Modern UI/UX**: Clean, responsive interface built with Streamlit
- **Secure API Management**: Environment-based API key configuration
- **Session State Management**: Efficient message handling and state persistence

## 🚀 Live Demo

Experience the chatbot in action: [Launch Demo](#) *(Deploy and add your link here)*

## 📸 Screenshots

```
┌─────────────────────────────────────┐
│  🤖 Chatbot com IA                  │
├─────────────────────────────────────┤
│                                     │
│  👤 User: Hello!                    │
│  🤖 AI: Hi! How can I help you?     │
│                                     │
│  [Type your message here...]        │
└─────────────────────────────────────┘
```

## 🛠️ Tech Stack

- **Frontend Framework**: [Streamlit](https://streamlit.io/) - Fast, interactive web applications
- **AI Integration**: [OpenAI API](https://openai.com/) - GPT-5 Nano model
- **Language**: Python 3.8+
- **Environment Management**: python-dotenv
- **State Management**: Streamlit Session State

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.8 or higher installed
- An OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- pip package manager

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd 04-chatbot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit openai python-dotenv
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example environment file
   copy .env.example .env  # Windows
   cp .env.example .env    # macOS/Linux
   ```

5. **Add your OpenAI API key**
   
   Edit the `.env` file and add your API key:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## 🎯 Usage

1. **Start the application**
   ```bash
   streamlit run main.py
   ```

2. **Access the chatbot**
   
   Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

3. **Start chatting!**
   
   Type your message in the input box and press Enter to interact with the AI.

## 📁 Project Structure

```
04-chatbot/
│
├── main.py              # Main application file
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore rules
├── README.md           # Project documentation
└── Alternativo/        # Alternative implementations
```

## 🔑 Key Components

### [`main.py`](main.py)

The core application file containing:

- **API Configuration**: Secure loading of OpenAI credentials
- **Streamlit UI**: Chat interface and message display
- **Session Management**: Conversation history tracking
- **AI Integration**: OpenAI API calls and response handling

```python
# Key features implemented:
- Environment variable loading with dotenv
- OpenAI client initialization
- Streamlit session state for message persistence
- Real-time chat interface with st.chat_input()
- Dynamic message rendering
```

## 🎨 Customization

### Change AI Model

Modify the model in [`main.py`](main.py:39):
```python
assistant_response = ai_model.chat.completions.create(
    messages=st.session_state["messages"], 
    model="gpt-4"  # Change to your preferred model
)
```

### Add System Instructions

Enhance the AI's personality by adding system instructions:
```python
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant specialized in..."}
    ]
```

### Customize UI Theme

Create a `.streamlit/config.toml` file:
```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

## 🔒 Security Best Practices

- ✅ API keys stored in environment variables
- ✅ `.env` file excluded from version control
- ✅ `.env.example` provided for easy setup
- ⚠️ Never commit sensitive credentials
- 🔐 Consider implementing rate limiting for production

## 🚧 Roadmap

- [ ] Add system instructions for custom AI personas
- [ ] Implement conversation export functionality
- [ ] Add support for multiple AI models
- [ ] Create conversation history persistence (database)
- [ ] Add user authentication
- [ ] Implement message editing and regeneration
- [ ] Add file upload capabilities
- [ ] Create mobile-responsive design improvements

## 🐛 Troubleshooting

### API Key Not Found
```
Error: API key not found. Please set the OPENAI_API_KEY environment variable.
```
**Solution**: Ensure your `.env` file exists and contains a valid `OPENAI_API_KEY`.

### Module Not Found
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solution**: Install required packages: `pip install streamlit openai python-dotenv`

### Port Already in Use
```
Error: Port 8501 is already in use
```
**Solution**: Stop other Streamlit instances or specify a different port:
```bash
streamlit run main.py --server.port 8502
```

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Python dotenv Guide](https://pypi.org/project/python-dotenv/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**

- Portfolio: [yourwebsite.com](#)
- LinkedIn: [linkedin.com/in/yourprofile](#)
- GitHub: [@yourusername](#)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Built as part of the **Jornada Python 2026** course by Hashtag
- Powered by [OpenAI](https://openai.com/)
- UI framework by [Streamlit](https://streamlit.io/)

## 📊 Project Stats

- **Development Time**: 2-3 hours
- **Lines of Code**: ~50
- **Dependencies**: 3 main packages
- **Complexity**: Beginner to Intermediate

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ and Python

[Report Bug](../../issues) · [Request Feature](../../issues) · [Documentation](#)

</div>
