# Task Summary Generator

A modern web application that transforms your task list into organized, actionable summaries using AI. Built with Flask and featuring a beautiful, responsive interface.

## ✨ Features

- **AI-Powered Summaries**: Generate detailed, brief, or prioritized task summaries
- **Multi-language Support**: Input tasks in English or Bangla
- **Voice Input**: Speak your tasks using speech recognition
- **Translation**: Translate summaries between English and Bangla
- **PDF Export**: Download summaries as PDF files
- **Dark Mode**: Toggle between light and dark themes
- **Responsive Design**: Works perfectly on desktop and mobile devices

## 🚀 Live Demo

[View Live Demo](https://your-app-name.herokuapp.com)

## 🛠️ Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML5, CSS3, JavaScript
- **AI**: Together AI API (Mistral-7B)
- **Translation**: Google Translate API
- **Styling**: Modern CSS with gradients and animations
- **Deployment**: Heroku/Railway/Render

## 📋 Prerequisites

- Python 3.8 or higher
- Git
- API key from Together AI

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/task-summary-generator.git
cd task-summary-generator
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
TOGETHER_API_KEY=your_together_ai_api_key_here
FLASK_SECRET_KEY=your_secret_key_here
```

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🌐 Deployment

### Option 1: Heroku

1. **Install Heroku CLI**

   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku**

   ```bash
   heroku login
   ```

3. **Create Heroku App**

   ```bash
   heroku create your-app-name
   ```

4. **Set Environment Variables**

   ```bash
   heroku config:set TOGETHER_API_KEY=your_api_key_here
   heroku config:set FLASK_SECRET_KEY=your_secret_key_here
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

### Option 2: Railway

1. **Connect GitHub Repository**

   - Go to [Railway](https://railway.app)
   - Connect your GitHub account
   - Select this repository

2. **Set Environment Variables**

   - Add `TOGETHER_API_KEY` and `FLASK_SECRET_KEY` in Railway dashboard

3. **Deploy**
   - Railway will automatically deploy your app

### Option 3: Render

1. **Create Render Account**

   - Sign up at [Render](https://render.com)

2. **Create New Web Service**

   - Connect your GitHub repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `gunicorn app:app`

3. **Set Environment Variables**
   - Add your API keys in the environment section

## 🔑 API Keys Setup

### Together AI API Key

1. Go to [Together AI](https://together.ai)
2. Create an account and get your API key
3. Add it to your environment variables

## 📁 Project Structure

```
task-summary-generator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile             # Heroku deployment config
├── runtime.txt          # Python version specification
├── .env                 # Environment variables (not in repo)
├── .gitignore          # Git ignore file
├── README.md           # This file
├── static/
│   └── style.css       # Modern CSS styling
└── templates/
    └── index.html      # Main HTML template
```

## 🎨 Features in Detail

### AI Summarization

- **Default Summary**: Balanced overview of tasks
- **Detailed Summary**: Comprehensive analysis with categories
- **Brief & Prioritized**: Quick, actionable task list

### Voice Input

- Click the 🎙️ button to start voice recognition
- Speak your tasks in English
- Automatically converts speech to text

### Translation

- Toggle between English and Bangla
- Preserves original formatting
- Real-time translation using Google Translate

### Dark Mode

- Toggle between light and dark themes
- Automatically saves preference
- Smooth transitions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Together AI for providing the AI model
- Google Translate for translation services
- Flask community for the web framework
- Modern CSS techniques for beautiful styling

## 📞 Support

If you have any questions or need help, please open an issue on GitHub or contact the maintainer.

---

**Made with ❤️ using Flask and modern web technologies**
