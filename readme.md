# GPTermi: The Linux Terminal Assistant

## Introduction

Welcome to GPTermi, where the power of Linux meets the intelligence of AI. Born from the idea that the command line should be accessible to everyone, GPTermi is a groundbreaking terminal application designed to simplify the intricacies of Linux commands through the conversational ease of natural language. 

Powered by OpenAI's ChatGPT, this application serves as your personal assistant, answering your Linux terminal and scripting queries in an intuitive, human-like manner. 

Whether you're a seasoned sysadmin, a developer, or a newcomer to the Linux world, GPTermi elevates your command line experience, making it more efficient, insightful, and, dare we say, delightful.

## How to Run GPTermi

To bring the capabilities of GPTermi to your desktop, follow these steps:

### Prerequisites

- Python 3.x
- `pip` for Python 3
- Internet connection for API communication

### Installation

1. **Clone the Repository:**
   
   Start by cloning the repository to your local machine using git:
   ```sh
   git clone https://github.com/77ethers/GPTermi.git
   cd GPTermi
   ```

2. **Install Dependencies:**
   
   Install the required Python libraries using `pip`:
   ```sh
   pip install -r requirements.txt
   ```

### Setting Up the ChatGPT API Key

GPTermi relies on OpenAI's ChatGPT API to process natural language commands. To use the application, you'll need to obtain an API key from OpenAI.

1. **Obtain an API Key:**
   
   - Sign up or log in to your account at [OpenAI](https://openai.com).
   - Navigate to the API section and generate your API key.

2. **Configure Your API Key:**
   
   For security reasons, it is crucial not to hardcode your API key into the application. Instead, use an environment variable or a configuration file that is not tracked by git. For instance, you could create a `.env` file in your project directory with the following content:
   ```env
   OPENAI_API_KEY='your_api_key_here'
   ```
   Make sure to add `.env` to your `.gitignore` file to prevent it from being committed to your repository.

### Running GPTermi

With the API key set up, you can now run the application:

```sh
python gptermi.py
```

The GPTermi interface should now open, presenting you with a terminal window where you can start typing your Linux related queries.

## Features

- **Natural Language Command Interpretation**: Interact with your Linux system using natural, conversational language.
- **Real-Time GPT Responses**: Get immediate assistance from the underlying GPT model, trained to understand Linux terminal commands.
- **Accessible Terminal Experience**: Designed for both beginners and experts, GPTermi makes the terminal more user-friendly.

## Contributing

We welcome contributions to GPTermi! If you have suggestions for improvements, encounter any issues, or would like to contribute code, please feel free to open an issue or a pull request.

## License

GPTermi is open source software [licensed as MIT](LICENSE).