#!/bin/bash

# Task Summary Generator - Deployment Script
echo "🚀 Setting up Task Summary Generator for deployment..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Initialize git repository if not already done
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
fi

# Add all files to git
echo "📝 Adding files to Git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Initial commit: Task Summary Generator"

# Check if remote origin exists
if ! git remote get-url origin &> /dev/null; then
    echo "🔗 Please add your GitHub repository as remote origin:"
    echo "git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
    echo ""
    echo "Then run: git push -u origin main"
else
    echo "✅ Remote origin already configured"
    echo "🚀 Ready to push to GitHub!"
    echo "Run: git push -u origin main"
fi

echo ""
echo "📋 Next Steps:"
echo "1. Create a GitHub repository"
echo "2. Add your repository as remote: git remote add origin YOUR_REPO_URL"
echo "3. Push to GitHub: git push -u origin main"
echo "4. Deploy to your preferred platform (Heroku/Railway/Render)"
echo ""
echo "🔑 Don't forget to set your environment variables:"
echo "- TOGETHER_API_KEY"
echo "- FLASK_SECRET_KEY"
echo ""
echo "✨ Your Task Summary Generator is ready for deployment!" 