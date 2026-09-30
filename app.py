#!/usr/bin/env python3
"""
Flask web version of DevOps Quest
The Hilarious Journey to Production 🚀
"""

from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import random
from enum import Enum
from dataclasses import dataclass, asdict
import os
from datetime import timedelta

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'devops-quest-secret-key-change-in-production')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)

Session(app)

class DevOpsRole(Enum):
    JUNIOR_DEV = 1
    DEVOPS_WARRIOR = 2
    KUBERNETES_WIZARD = 3

class Severity(Enum):
    LOW = 1
    MEDIUM = 2
    CRITICAL = 3
    ABSOLUTE_DISASTER = 4

@dataclass
class Challenge:
    title: str
    description: str
    difficulty: str
    correct_answer: str
    options: list
    lesson: str
    id: int = 0

def get_challenges():
    """Load all DevOps challenges"""
    challenges = [
        Challenge(
            id=0,
            title="🔥 THE 3AM OUTAGE",
            description="Your app just went down at 3 AM. Your boss is calling. What do you do?",
            difficulty="CRITICAL",
            correct_answer="B",
            options=[
                "A) Pretend your phone died",
                "B) Check the logs immediately and use monitoring tools to identify the issue",
                "C) Deploy the 'fix' you wrote while half-asleep last week",
                "D) Blame it on Mercury retrograde"
            ],
            lesson="✨ LESSON: Always monitor your applications! Set up proper logging and alerting systems."
        ),
        Challenge(
            id=1,
            title="🐳 THE DOCKER DILEMMA",
            description="Your colleague says: 'It works on my machine!' But it doesn't work in production. Why?",
            difficulty="MEDIUM",
            correct_answer="B",
            options=[
                "A) Your colleague is secretly a wizard",
                "B) Different environments! Containerize with Docker for consistency",
                "C) The production server is just being moody",
                "D) Sacrifice a USB drive to the DevOps gods"
            ],
            lesson="🐳 LESSON: Docker containers ensure your app runs the same everywhere - dev, test, and production!"
        ),
        Challenge(
            id=2,
            title="📊 THE SCALING CRISIS",
            description="Your startup just went viral! Traffic increased 1000x. Your server is on fire. What's the solution?",
            difficulty="CRITICAL",
            correct_answer="C",
            options=[
                "A) Buy a really expensive laptop",
                "B) Hope for the best and pray to the cloud gods",
                "C) Use load balancing and auto-scaling with Kubernetes/Docker",
                "D) Tell users to refresh less often"
            ],
            lesson="⚖️ LESSON: Horizontal scaling (adding more servers) beats vertical scaling. Auto-scaling handles traffic spikes automatically!"
        ),
        Challenge(
            id=3,
            title="🔐 THE SECURITY NIGHTMARE",
            description="You just realized your database password is 'password123' and it's in your GitHub repo. What do you do?",
            difficulty="ABSOLUTE_DISASTER",
            correct_answer="A",
            options=[
                "A) Immediately rotate the password and use environment variables/secrets manager",
                "B) Hope no one noticed and keep scrolling",
                "C) Delete the repo from GitHub to 'erase' history",
                "D) Change it to 'password124' - nobody will guess that!"
            ],
            lesson="🔐 LESSON: NEVER commit secrets to version control! Use environment variables and secrets management tools."
        ),
        Challenge(
            id=4,
            title="🚀 THE DEPLOYMENT DISASTER",
            description="You're about to deploy to production. You haven't tested it. Your manager is watching. What do you do?",
            difficulty="CRITICAL",
            correct_answer="B",
            options=[
                "A) YOLO deploy it at 5:55 PM on Friday",
                "B) Create a staging environment and test thoroughly first",
                "C) Ask your cat to review the code",
                "D) Deploy to production as a 'beta test'"
            ],
            lesson="🛡️ LESSON: Always test in staging first! Use CI/CD pipelines to automate testing and catch bugs early."
        ),
        Challenge(
            id=5,
            title="📈 THE MONITORING MYSTERY",
            description="Your application is slow but you have no idea why. How do you find the culprit?",
            difficulty="MEDIUM",
            correct_answer="A",
            options=[
                "A) Set up comprehensive monitoring and observability tools (Prometheus, ELK, Datadog, etc.)",
                "B) Add console.log() statements everywhere and hope for the best",
                "C) Blame the database and delete random tables",
                "D) Restart the server until it feels faster"
            ],
            lesson="📊 LESSON: Monitoring, logging, and tracing are essential! They help you understand what's happening in production."
        ),
        Challenge(
            id=6,
            title="🔄 THE BACKUP BLUNDER",
            description="Your database just corrupted. When's the last time you tested your backup recovery?",
            difficulty="ABSOLUTE_DISASTER",
            correct_answer="C",
            options=[
                "A) Last year? Maybe?",
                "B) Never - who needs backups?",
                "C) Regularly! Test backups monthly - backups you can't restore are useless",
                "D) That's what the cloud is for!"
            ],
            lesson="💾 LESSON: Regular backups + regular recovery testing = sleep at night! 'Untested backups are not backups.'"
        ),
        Challenge(
            id=7,
            title="🔗 THE CI/CD CONFUSION",
            description="You manually deploy code to production every time. Your teammates hate you. What's the modern way?",
            difficulty="MEDIUM",
            correct_answer="B",
            options=[
                "A) Deploy faster - work harder!",
                "B) Set up CI/CD pipelines (GitHub Actions, Jenkins, GitLab CI) for automated testing and deployment",
                "C) Deploy via interpretive dance",
                "D) Make someone else do it"
            ],
            lesson="⚙️ LESSON: CI/CD automates build, test, and deploy. Faster, safer, and humans stop clicking deploy buttons at 3 AM!"
        ),
    ]
    return challenges

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/api/start-game', methods=['POST'])
def start_game():
    """Initialize a new game session"""
    data = request.json
    player_name = data.get('player_name', 'DevOps Hero')
    role = data.get('role', 'DEVOPS_WARRIOR')
    
    # Initialize session
    session['player_name'] = player_name
    session['role'] = role
    session['level'] = 0
    session['score'] = 0
    session['health'] = {'JUNIOR_DEV': 50, 'DEVOPS_WARRIOR': 100, 'KUBERNETES_WIZARD': 150}[role]
    session['production_stability'] = 50
    session['challenges_completed'] = 0
    session['total_challenges'] = len(get_challenges())
    session['challenge_pool'] = list(range(len(get_challenges())))
    random.shuffle(session['challenge_pool'])
    session['current_challenge_index'] = None
    session.permanent = True
    
    return jsonify({
        'status': 'success',
        'message': f'Game started! Welcome, {player_name}!',
        'player_name': player_name,
        'role': role,
        'health': session['health'],
        'production_stability': session['production_stability']
    })

@app.route('/api/next-challenge', methods=['GET'])
def next_challenge():
    """Get next challenge"""
    if 'player_name' not in session:
        return jsonify({'error': 'Game not started'}), 400
    
    if not session.get('challenge_pool'):
        return jsonify({'error': 'No more challenges'}), 400
    
    challenge_id = session['challenge_pool'].pop(0)
    session['current_challenge_index'] = challenge_id
    
    challenges = get_challenges()
    challenge = challenges[challenge_id]
    
    return jsonify({
        'id': challenge.id,
        'title': challenge.title,
        'description': challenge.description,
        'difficulty': challenge.difficulty,
        'options': challenge.options,
        'challenges_remaining': len(session['challenge_pool']) + 1
    })

@app.route('/api/submit-answer', methods=['POST'])
def submit_answer():
    """Submit answer to current challenge"""
    if 'player_name' not in session:
        return jsonify({'error': 'Game not started'}), 400
    
    data = request.json
    answer = data.get('answer', '').upper()
    
    challenge_id = session.get('current_challenge_index')
    if challenge_id is None:
        return jsonify({'error': 'No active challenge'}), 400
    
    challenges = get_challenges()
    challenge = challenges[challenge_id]
    
    if answer not in ['A', 'B', 'C', 'D']:
        return jsonify({'error': 'Invalid answer format'}), 400
    
    is_correct = answer == challenge.correct_answer
    
    if is_correct:
        difficulty_value = {'LOW': 1, 'MEDIUM': 2, 'CRITICAL': 3, 'ABSOLUTE_DISASTER': 4}[challenge.difficulty]
        points = difficulty_value * 10
        session['score'] += points
        session['production_stability'] = min(100, session['production_stability'] + (difficulty_value * 5))
    else:
        difficulty_value = {'LOW': 1, 'MEDIUM': 2, 'CRITICAL': 3, 'ABSOLUTE_DISASTER': 4}[challenge.difficulty]
        damage = difficulty_value * 10
        session['health'] -= damage
        session['production_stability'] = max(0, session['production_stability'] - (difficulty_value * 5))
    
    session['challenges_completed'] += 1
    
    return jsonify({
        'is_correct': is_correct,
        'correct_answer': challenge.correct_answer,
        'lesson': challenge.lesson,
        'health': session['health'],
        'score': session['score'],
        'production_stability': session['production_stability'],
        'challenges_completed': session['challenges_completed']
    })

@app.route('/api/game-status', methods=['GET'])
def game_status():
    """Get current game status"""
    if 'player_name' not in session:
        return jsonify({'error': 'Game not started'}), 400
    
    return jsonify({
        'player_name': session.get('player_name'),
        'role': session.get('role'),
        'health': session.get('health', 0),
        'score': session.get('score', 0),
        'production_stability': session.get('production_stability', 50),
        'challenges_completed': session.get('challenges_completed', 0),
        'total_challenges': session.get('total_challenges', 0)
    })

@app.route('/api/end-game', methods=['POST'])
def end_game():
    """End game and get results"""
    if 'player_name' not in session:
        return jsonify({'error': 'Game not started'}), 400
    
    results = {
        'player_name': session.get('player_name'),
        'role': session.get('role'),
        'final_score': session.get('score', 0),
        'final_health': session.get('health', 0),
        'final_stability': session.get('production_stability', 50),
        'challenges_completed': session.get('challenges_completed', 0),
        'total_challenges': session.get('total_challenges', 0)
    }
    
    # Determine rank
    stability = results['final_stability']
    health = results['final_health']
    
    if health <= 0:
        results['rank'] = '💔 CRASHED'
        results['message'] = 'Your infrastructure crashed spectacularly! Your boss is updating their LinkedIn...'
    elif stability >= 80:
        results['rank'] = '🏆 LEGENDARY'
        results['message'] = 'You\'ve mastered DevOps! Your infrastructure is bulletproof!'
    elif stability >= 60:
        results['rank'] = '🎖️ EXCELLENT'
        results['message'] = 'You\'re a DevOps professional! Your systems are stable and reliable!'
    elif stability >= 40:
        results['rank'] = '👍 GOOD'
        results['message'] = 'You understand DevOps basics! Keep learning and you\'ll be amazing!'
    else:
        results['rank'] = '😅 LEARNING'
        results['message'] = 'Keep practicing - you\'ll get there!'
    
    # Fun facts
    facts = [
        "💡 Did you know? Netflix's Chaos Monkey intentionally breaks things to test resilience!",
        "🐧 Did you know? Kubernetes means 'pilot' in Greek!",
        "🚀 Did you know? Amazon deploys to production every 11.7 seconds!",
        "📦 Did you know? Docker was named after the British children's show!",
    ]
    results['fun_fact'] = random.choice(facts)
    
    # Clear session
    session.clear()
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
