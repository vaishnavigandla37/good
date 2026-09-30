# DevOps Quest - Web Version 🚀

A modern web-based version of the DevOps Quest educational game built with Flask and vanilla JavaScript.

## Features

- 🎮 Interactive web interface with modern UI
- 🎯 8 challenging DevOps scenarios
- 📊 Real-time score and health tracking
- 🏆 Dynamic ranking system
- 📱 Responsive design (works on desktop and mobile)
- 🎓 Educational lessons for each challenge
- 💾 Session-based game state management

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone or navigate to the repository**
   ```bash
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

5. **Open your browser**
   - Navigate to `http://localhost:5000`

## Project Structure

```
.
├── app.py                 # Flask application and API endpoints
├── requirements-web.txt   # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── css/
    │   └── style.css     # Styling
    └── js/
        └── app.js        # Frontend logic
```

## How to Play

1. **Enter your name** and choose your role:
   - 👤 Junior Dev (50 HP) - Takes more damage, learns faster
   - ⚔️ DevOps Warrior (100 HP) - Balanced stats
   - 🧙 Kubernetes Wizard (150 HP) - Takes less damage, harder challenges

2. **Answer DevOps challenges** and increase your production stability

3. **Learn through gameplay** - Each challenge includes a lesson explaining the correct DevOps practice

4. **Track your progress** - Monitor your health, score, and production stability in real-time

5. **Achieve your rank** based on your final production stability:
   - 🏆 LEGENDARY (80%+)
   - 🎖️ EXCELLENT (60-79%)
   - 👍 GOOD (40-59%)
   - 😅 LEARNING (<40%)

## API Endpoints

### POST `/api/start-game`
Initialize a new game session
- **Request**: `{ "player_name": "string", "role": "JUNIOR_DEV|DEVOPS_WARRIOR|KUBERNETES_WIZARD" }`
- **Response**: Game initialization data

### GET `/api/next-challenge`
Get the next challenge
- **Response**: Challenge data with title, description, options, and difficulty

### POST `/api/submit-answer`
Submit an answer to the current challenge
- **Request**: `{ "answer": "A|B|C|D" }`
- **Response**: Result with lesson, points, and updated stats

### GET `/api/game-status`
Get current game status
- **Response**: Player stats and game progress

### POST `/api/end-game`
End the game and get results
- **Response**: Final results and ranking

## Customization

### Add More Challenges

Edit the `get_challenges()` function in `app.py` to add more challenges:

```python
Challenge(
    id=8,
    title="🎯 Your Challenge Title",
    description="Challenge description here",
    difficulty="MEDIUM",
    correct_answer="B",
    options=["A) Option", "B) Option", "C) Option", "D) Option"],
    lesson="📚 LESSON: The lesson here"
)
```

### Customize Colors

Edit `static/css/style.css` to change the color scheme. The main gradient is:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

## Deployment

### Heroku

1. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Install gunicorn:
   ```bash
   pip install gunicorn
   ```

3. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku web-version:main
   ```

### Other Platforms

- **Vercel**: Use with serverless Python support
- **Railway**: Simple Git deployment
- **PythonAnywhere**: Free Python hosting
- **AWS/Google Cloud**: Traditional server deployment

## Development

### Enable Debug Mode

Edit `app.py`:
```python
app.run(debug=True)  # Already enabled
```

### Modify Game Difficulty

Adjust the damage and points multipliers in `submit_answer()` function:
```python
points = difficulty_value * 10  # Change multiplier
damage = difficulty_value * 10  # Change multiplier
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: Vanilla JavaScript (no frameworks)
- **Styling**: CSS3 with flexbox and gradients
- **State Management**: Flask sessions
- **API**: RESTful JSON endpoints

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## License

GNU Affero General Public License v3.0 - See LICENSE file

## Fun Facts 🎓

- Netflix's Chaos Monkey intentionally breaks things to test resilience
- Kubernetes means 'pilot' in Greek
- Amazon deploys to production every 11.7 seconds
- Docker was named after the British children's show

## Support

For issues or suggestions, please open a GitHub issue!

Happy learning! 🚀
