# 🎮 DevOps Quest: The Hilarious Journey to Production 🚀

> Learn DevOps concepts while saving your company from chaos! An interactive, educational game that makes learning DevOps fun and memorable.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-AGPL--3.0-red)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

## 📖 Overview

**DevOps Quest** is an engaging, browser-based educational game designed to teach fundamental DevOps concepts through interactive challenges and real-world scenarios. Whether you're a Junior Developer, a DevOps Warrior, or a Kubernetes Wizard, this game will test your knowledge and improve your understanding of production infrastructure, monitoring, deployment strategies, and more.

### Why DevOps Quest?

- 🎯 **Learning Through Gameplay** - Master DevOps concepts while having fun
- 🚀 **Real-World Scenarios** - Face authentic challenges that DevOps engineers encounter
- 💡 **Educational Lessons** - Each challenge includes detailed explanations
- 🏆 **Achievement System** - Get ranked based on your performance
- 📱 **Play Anywhere** - Works on desktop, tablet, and mobile browsers
- 🎨 **Beautiful UI** - Modern, responsive design with smooth animations

## 🎯 Features

### Gameplay
- 🎮 **8 Challenging Scenarios** covering:
  - 🔥 Production Outages & Monitoring
  - 🐳 Docker & Containerization
  - 📊 Scaling & Load Balancing
  - 🔐 Security & Secrets Management
  - 🚀 Deployment Strategies
  - 📈 Application Performance
  - 💾 Backup & Disaster Recovery
  - ⚙️ CI/CD Pipelines

### Player Roles
- **👶 Junior Dev** (50 HP) - Takes more damage, learns faster
- **⚔️ DevOps Warrior** (100 HP) - Balanced difficulty and rewards
- **🧙 Kubernetes Wizard** (150 HP) - Expert mode with challenging scenarios

### Game Mechanics
- ❤️ **Health System** - Make wrong decisions and lose health
- ⚡ **Production Stability** - Track your infrastructure reliability
- 💯 **Score System** - Earn points for correct answers
- 📊 **Real-time Stats** - Monitor your progress live
- 🏆 **Ranking System**:
  - 🏆 LEGENDARY (80%+ stability)
  - 🎖️ EXCELLENT (60-79%)
  - 👍 GOOD (40-59%)
  - 😅 LEARNING (<40%)

### Educational Value
- 📚 **Detailed Lessons** - Learn the "why" behind each answer
- 🔄 **Multiple Attempts** - Replay to improve your score
- 💡 **Real DevOps Practices** - Industry-standard best practices
- 🎓 **Beginner Friendly** - No prior DevOps experience needed

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vaishnavigandla37/good.git
   cd good
   git checkout web-version
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements-web.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## 🎮 How to Play

### Step 1: Choose Your Role
```
👤 Junior Dev       (50 HP)  - Beginner-friendly
⚔️ DevOps Warrior   (100 HP) - Recommended for most
🧙 Kubernetes Wizard (150 HP) - Expert challenge
```

### Step 2: Answer Challenges
- Read each scenario carefully
- Choose the best DevOps practice from 4 options
- Submit your answer and get instant feedback

### Step 3: Learn from Mistakes
- Review the lesson after each answer
- Understand the correct approach
- Track your health and stability

### Step 4: Achieve Your Rank
- Complete all 8 challenges
- Reach your highest possible production stability
- Earn achievements based on your final score

## 📁 Project Structure

```
good/
├── app.py                      # Flask backend & API
├── requirements-web.txt        # Python dependencies
├── README.md                   # This file
├── README_WEB.md              # Detailed setup guide
├── LICENSE                     # GNU AGPL v3.0
├── templates/
│   └── index.html             # Main web interface
└── static/
    ├── css/
    │   └── style.css          # Styling & animations
    └── js/
        └── app.js             # Game logic & API calls
```

## 🔧 API Reference

### Start Game
```
POST /api/start-game
{
  "player_name": "string",
  "role": "JUNIOR_DEV|DEVOPS_WARRIOR|KUBERNETES_WIZARD"
}
```

### Get Next Challenge
```
GET /api/next-challenge
Returns: Challenge data with options and difficulty
```

### Submit Answer
```
POST /api/submit-answer
{
  "answer": "A|B|C|D"
}
Returns: Result with lesson, points, and updated stats
```

### Get Game Status
```
GET /api/game-status
Returns: Current player stats and progress
```

### End Game
```
POST /api/end-game
Returns: Final results and ranking
```

## 📚 Challenges Included

### 🔥 The 3AM Outage
**Scenario:** Your app crashed at 3 AM. Your boss is calling.
**Lesson:** Importance of monitoring and logging systems

### 🐳 The Docker Dilemma
**Scenario:** "It works on my machine!" but fails in production.
**Lesson:** Docker containerization for environment consistency

### 📊 The Scaling Crisis
**Scenario:** Traffic increased 1000x. Server on fire.
**Lesson:** Load balancing and auto-scaling strategies

### 🔐 The Security Nightmare
**Scenario:** Database password 'password123' is in your GitHub repo.
**Lesson:** Secrets management and security best practices

### 🚀 The Deployment Disaster
**Scenario:** Deploy to production without testing?
**Lesson:** CI/CD pipelines and staging environments

### 📈 The Monitoring Mystery
**Scenario:** Application is slow. No idea why.
**Lesson:** Observability tools and performance monitoring

### 🔄 The Backup Blunder
**Scenario:** Database corrupted. When did you last test backups?
**Lesson:** Backup strategy and disaster recovery

### 🔗 The CI/CD Confusion
**Scenario:** Manual deployments every time.
**Lesson:** Automated testing and deployment pipelines

## 🎨 Technology Stack

| Category | Technology |
|----------|-----------|
| **Backend** | Flask 2.3.3 (Python) |
| **Frontend** | Vanilla JavaScript, HTML5, CSS3 |
| **Session Management** | Flask-Session |
| **Server** | Development/Production Ready |
| **Deployment** | Heroku, Railway, PythonAnywhere, AWS |

## 🚀 Deployment

### Deploy to Heroku (Free)

1. **Create Procfile**
   ```
   web: gunicorn app:app
   ```

2. **Install gunicorn**
   ```bash
   pip install gunicorn
   ```

3. **Deploy**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku web-version:main
   heroku open
   ```

### Deploy to Railway
- Connect GitHub repository
- Select `web-version` branch
- Deploy automatically

### Deploy to PythonAnywhere
- Upload files via web console
- Set Python 3.8+ version
- Configure WSGI file

### Deploy to AWS/Google Cloud
- Use traditional Docker/container deployment
- Set `FLASK_ENV=production`
- Configure proper SECRET_KEY

## ⚙️ Configuration

### Change Colors
Edit `static/css/style.css`:
```css
/* Main gradient (line ~16) */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Adjust Difficulty
Edit `app.py` in `submit_answer()`:
```python
points = difficulty_value * 10  # Change multiplier
damage = difficulty_value * 10  # Change multiplier
```

### Add Custom Challenges
Edit `get_challenges()` in `app.py`:
```python
Challenge(
    id=8,
    title="🎯 Your Challenge Title",
    description="Challenge description",
    difficulty="MEDIUM",
    correct_answer="B",
    options=["A) ...", "B) ...", "C) ...", "D) ..."],
    lesson="📚 LESSON: ..."
)
```

## 🌐 Browser Support

| Browser | Status |
|---------|--------|
| Chrome 90+ | ✅ Full Support |
| Firefox 88+ | ✅ Full Support |
| Safari 14+ | ✅ Full Support |
| Edge 90+ | ✅ Full Support |
| Mobile Browsers | ✅ Responsive Design |

## 📊 Game Mechanics Explained

### Health System
- Start with role-specific HP (50, 100, or 150)
- Wrong answers cause damage (multiplied by difficulty)
- Game ends if health reaches 0
- "Legendary" status requires surviving with health > 0

### Production Stability
- Starts at 50%
- Increases on correct answers (+5% to +20%)
- Decreases on wrong answers (-5% to -20%)
- Determines your final rank

### Scoring System
- Points = Difficulty Level × 10
- LOW difficulty = 10 points
- MEDIUM difficulty = 20 points
- CRITICAL difficulty = 30 points
- ABSOLUTE_DISASTER difficulty = 40 points

### Ranking Algorithm
```
Health > 0 + Stability >= 80%  → 🏆 LEGENDARY
Health > 0 + Stability >= 60%  → 🎖️ EXCELLENT
Health > 0 + Stability >= 40%  → 👍 GOOD
Health > 0 + Stability < 40%   → 😅 LEARNING
Health <= 0                     → 💔 CRASHED
```

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the **GNU Affero General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

```
DevOps Quest
Copyright (C) 2026 vaishnavigandla37

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
```

## 🎓 Learning Resources

After playing DevOps Quest, deepen your knowledge:

- **Docker** - [docs.docker.com](https://docs.docker.com)
- **Kubernetes** - [kubernetes.io](https://kubernetes.io)
- **CI/CD** - [GitHub Actions](https://github.com/features/actions), [Jenkins](https://www.jenkins.io/)
- **Monitoring** - [Prometheus](https://prometheus.io/), [ELK Stack](https://www.elastic.co/)
- **DevOps Practices** - [The Phoenix Project](https://itrevolution.com/the-phoenix-project/), [Site Reliability Engineering](https://sre.google/)

## 📞 Support & Feedback

- 🐛 **Report Bugs** - Open an [Issue](https://github.com/vaishnavigandla37/good/issues)
- 💡 **Suggest Features** - Create a [Discussion](https://github.com/vaishnavigandla37/good/discussions)
- 📧 **Contact** - Email: vaishnavigandla37@gmail.com

## 🎉 Fun Facts

- 🐵 Netflix's **Chaos Monkey** intentionally breaks production systems to test resilience!
- 🐧 **Kubernetes** means "helmsman" or "pilot" in Greek!
- 📦 **Amazon** deploys to production **every 11.7 seconds**!
- 🐳 **Docker** was named after the British children's TV show "Clangers"!

## 🏆 Achievements

- ✅ 8 Challenging scenarios
- ✅ 3 Difficulty levels
- ✅ Dynamic ranking system
- ✅ Educational content
- ✅ Mobile responsive
- ✅ Fast & smooth gameplay
- ✅ Production-ready code

## 🚀 Roadmap

- [ ] Multiplayer mode
- [ ] Leaderboard system
- [ ] Achievement badges
- [ ] Custom challenge creation
- [ ] Mobile app version
- [ ] Team competitions
- [ ] API for custom integrations
- [ ] Gamification features (streaks, combos)

## ⭐ Show Your Support

If you found DevOps Quest helpful, please:
- ⭐ Star this repository
- 🔗 Share it with your friends
- 💬 Leave feedback and suggestions
- 🐛 Report any issues you find

---

## 📧 Contact & Credits

**Created by:** [vaishnavigandla37](https://github.com/vaishnavigandla37)

**Special Thanks to:**
- DevOps community for inspiration
- Open-source contributors
- Everyone learning DevOps!

---

**Happy Learning! Keep your infrastructure running! 🚀**

*Last Updated: 2026-09-30*
*Version: 2.0 (Web Edition)*
