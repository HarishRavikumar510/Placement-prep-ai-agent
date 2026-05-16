# 🚀 Placement Prep AI Agent

An AI-powered placement preparation platform built using React, Vite, and Gemini AI.

This application helps students prepare for placement interviews by generating:
- MCQ questions
- Personalized study plans
- Weak topic recommendations
- Practice roadmaps
- Smart preparation workflows

---

# ✨ Features

## 🧠 AI MCQ Generator

Generate placement preparation MCQs for topics like:
- SQL
- DSA
- OOP
- Aptitude
- Probability
- Gen AI
- SDLC
- Git

Users can:
- Select question limits
- Generate AI-powered MCQs
- View answers and explanations
- Practice topic-wise preparation

---

## 📅 AI Study Plan Generator

The app creates personalized preparation plans based on:
- Target company
- Preparation days
- Weak topics

The AI generates:
- Daily preparation schedule
- Practice tasks
- Coding suggestions
- MCQ recommendations
- Improvement strategies

---

## 🧠 Local Memory System

The app remembers:
- Recently practiced topics
- Last selected topic

This creates a lightweight agentic AI experience using browser localStorage.

---

## 🎨 Modern UI

- Responsive design
- Dark futuristic theme
- Dynamic MCQ cards
- Interactive topic buttons
- Smart layouts

---

# 🛠️ Tech Stack

## Frontend
- React.js
- Vite
- JavaScript

## AI Integration
- Gemini API
- @google/generative-ai

## Storage
- localStorage

---

# 📂 Project Structure

```bash
placement-ai-agent
│
├── public
├── src
│   ├── App.jsx
│   ├── gemini.js
│   ├── main.jsx
│   └── assets
│
├── .env
├── package.json
├── vite.config.js
└── README.md