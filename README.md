# 🤖 AI Chatbot with OpenAI Integration

A modern, interactive chatbot application built with Streamlit and OpenAI's GPT API, featuring real-time conversational AI capabilities and a clean, intuitive user interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- **Real-time AI Conversations**: Seamless integration with OpenAI's GPT-4o-mini model for intelligent responses
- **Persistent Chat History**: Maintains conversation context throughout the session
- **Modern UI/UX**: Clean, responsive interface built with Streamlit
- **Secure API Management**: Environment-based API key configuration
- **Session State Management**: Efficient message handling and state persistence
- **Robust Error Handling**: Comprehensive exception handling for API errors
- **Type Safety**: Full type hints for better code reliability
- **Modular Architecture**: Well-organized functions with clear responsibilities

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
- **AI Integration**: [OpenAI API](https://openai.com/) - GPT-4o-mini model
- **Language**: Python 3.8+ with type hints
- **Environment Management**: python-dotenv
- **State Management**: Streamlit Session State
- **Error Handling**: Comprehensive exception handling with OpenAIError

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
├── main.py             # Main application file
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
├── README.md           # Project documentation
└── LICENSE             # License file
```

## 🏗️ Code Architecture

The application follows best practices with a clean, modular architecture:

### Design Principles

- **Separation of Concerns**: Each function has a single, well-defined responsibility
- **Type Safety**: Full type hints using `typing` module (`Optional`, `List`, `Dict`)
- **Error Handling**: Comprehensive exception handling with specific error types
- **Documentation**: Detailed docstrings for all functions following Google style
- **Constants**: Configuration values defined as module-level constants
- **Immutability**: System prompt defined as constant to prevent accidental modification

### Code Quality Features

- ✅ **Type Hints**: All functions include parameter and return type annotations
- ✅ **Error Recovery**: Graceful handling of API errors with user-friendly messages
- ✅ **Input Validation**: API key validation before client initialization
- ✅ **State Management**: Proper initialization and handling of session state
- ✅ **User Feedback**: Loading spinners and clear error messages
- ✅ **Clean Code**: Well-organized imports (standard → third-party → local)

## 🔑 Key Components

### [`main.py`](main.py)

The core application file with a modular, well-documented architecture:

#### Core Functions

- **[`initialize_environment()`](main.py:24)**: Loads environment variables and retrieves the OpenAI API key
- **[`initialize_openai_client()`](main.py:35)**: Creates and configures the OpenAI client instance
- **[`initialize_session_state()`](main.py:48)**: Sets up Streamlit session state with system prompt
- **[`display_chat_history()`](main.py:54)**: Renders conversation history (excluding system messages)
- **[`get_ai_response()`](main.py:61)**: Handles API calls with comprehensive error handling
- **[`main()`](main.py:89)**: Application entry point with full workflow orchestration

#### Key Features

```python
# Architecture highlights:
- Type hints for all functions (Optional[str], List[Dict[str, str]], etc.)
- Comprehensive error handling with try-except blocks
- System prompt configuration for AI personality
- Temperature (0.7) and max_tokens (1000) parameters for balanced responses
- Separation of concerns with dedicated functions
- Detailed docstrings following Google style
```

#### Configuration Constants

- **DEFAULT_MODEL**: `"gpt-4o-mini"` - Reliable and efficient model
- **SYSTEM_PROMPT**: Configurable AI assistant personality
- **Temperature**: 0.7 for balanced creativity
- **Max Tokens**: 1000 for reasonable response length

## 🎨 Customization

### Change AI Model

Modify the [`DEFAULT_MODEL`](main.py:17) constant:
```python
DEFAULT_MODEL = "gpt-4"  # Change to your preferred model
# Options: "gpt-4", "gpt-4-turbo", "gpt-3.5-turbo", etc.
```

### Customize System Instructions

Edit the [`SYSTEM_PROMPT`](main.py:18) constant to change AI personality:
```python
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a helpful assistant specialized in Python programming."
}
```

### Adjust Response Parameters

Modify parameters in [`get_ai_response()`](main.py:74):
```python
response = client.chat.completions.create(
    messages=messages,
    model=model,
    temperature=0.9,  # Higher = more creative (0.0-2.0)
    max_tokens=2000,  # Longer responses
)
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

- [x] Add system instructions for custom AI personas
- [x] Implement comprehensive error handling
- [x] Add type hints for better code quality
- [x] Modular function architecture
- [ ] Implement conversation export functionality
- [ ] Add support for multiple AI models (model selector)
- [ ] Create conversation history persistence (database)
- [ ] Add user authentication
- [ ] Implement message editing and regeneration
- [ ] Add file upload capabilities
- [ ] Create mobile-responsive design improvements
- [ ] Add conversation reset/clear button

## 🐛 Troubleshooting

### API Key Not Found
```
⚠️ API key not found. Please set the OPENAI_API_KEY environment variable.
```
**Solution**: Ensure your `.env` file exists and contains a valid `OPENAI_API_KEY`. The app will display a helpful info message with instructions.

### OpenAI API Errors
```
OpenAI API Error: [error message]
```
**Solution**: The application includes comprehensive error handling. Common causes:
- Invalid API key
- Rate limit exceeded
- Network connectivity issues
- Insufficient API credits

Check the error message displayed in the app for specific details.

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

### Client Initialization Failed
```
Failed to initialize OpenAI client: [error message]
```
**Solution**: Verify your API key is valid and properly formatted in the `.env` file.

## 🎯 API Configuration Details

The application uses optimized parameters for the OpenAI API:

| Parameter | Value | Purpose |
|-----------|-------|---------|
| **model** | `gpt-4o-mini` | Balanced performance and cost-efficiency |
| **temperature** | `0.7` | Balanced creativity (0=deterministic, 2=very creative) |
| **max_tokens** | `1000` | Reasonable response length limit |
| **system prompt** | Custom | Defines AI assistant personality and behavior |

### Response Quality

The [`get_ai_response()`](main.py:61) function includes:
- Automatic retry logic through OpenAI client
- Error-specific handling for `OpenAIError` exceptions
- Fallback error messages for unexpected issues
- None return on failure to prevent crashes

## 📚 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Python dotenv Guide](https://pypi.org/project/python-dotenv/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

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

- **Development Time**: 3-4 hours
- **Lines of Code**: ~150 (with documentation)
- **Functions**: 6 modular functions
- **Dependencies**: 3 main packages
- **Type Coverage**: 100% (all functions typed)
- **Error Handling**: Comprehensive with try-except blocks
- **Complexity**: Intermediate

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ and Python

[Report Bug](../../issues) · [Request Feature](../../issues) · [Documentation](#)

</div>
