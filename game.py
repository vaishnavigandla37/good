#!/usr/bin/env python3
"""
🎮 DevOps Quest: The Hilarious Journey to Production 🚀
Learn DevOps by saving your company from chaos!
"""

import random
import time
from enum import Enum
from dataclasses import dataclass

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
    difficulty: Severity
    correct_answer: str
    options: list
    lesson: str
    
class DevOpsGame:
    def __init__(self):
        self.player_name = ""
        self.role = None
        self.level = 0
        self.score = 0
        self.health = 100
        self.production_stability = 50
        self.challenges_completed = 0
        self.challenges = self._load_challenges()
        
    def _load_challenges(self):
        """Load all hilarious DevOps challenges"""
        return [
            Challenge(
                title="🔥 THE 3AM OUTAGE",
                description="Your app just went down at 3 AM. Your boss is calling. What do you do?",
                difficulty=Severity.CRITICAL,
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
                title="🐳 THE DOCKER DILEMMA",
                description="Your colleague says: 'It works on my machine!' But it doesn't work in production. Why?",
                difficulty=Severity.MEDIUM,
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
                title="📊 THE SCALING CRISIS",
                description="Your startup just went viral! Traffic increased 1000x. Your server is on fire. What's the solution?",
                difficulty=Severity.CRITICAL,
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
                title="🔐 THE SECURITY NIGHTMARE",
                description="You just realized your database password is 'password123' and it's in your GitHub repo. What do you do?",
                difficulty=Severity.ABSOLUTE_DISASTER,
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
                title="🚀 THE DEPLOYMENT DISASTER",
                description="You're about to deploy to production. You haven't tested it. Your manager is watching. What do you do?",
                difficulty=Severity.CRITICAL,
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
                title="📈 THE MONITORING MYSTERY",
                description="Your application is slow but you have no idea why. How do you find the culprit?",
                difficulty=Severity.MEDIUM,
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
                title="🔄 THE BACKUP BLUNDER",
                description="Your database just corrupted. When's the last time you tested your backup recovery?",
                difficulty=Severity.ABSOLUTE_DISASTER,
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
                title="🔗 THE CI/CD CONFUSION",
                description="You manually deploy code to production every time. Your teammates hate you. What's the modern way?",
                difficulty=Severity.MEDIUM,
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
    
    def display_title(self):
        """Display game title with ASCII art"""
        print("\n" + "="*70)
        print(" 🎮  DEVOPS QUEST: The Hilarious Journey to Production 🚀  🎮")
        print("="*70)
        print("\n📖 Learn DevOps concepts while saving your company from chaos!")
        print("   Answer questions correctly to increase production stability.\n")
    
    def get_player_name(self):
        """Get player name and role"""
        self.display_title()
        self.player_name = input("👤 What's your name, brave DevOps warrior? ").strip()
        print(f"\nWelcome, {self.player_name}! 🎉\n")
        print("Choose your starting role:")
        print("1) Junior Dev (Takes more damage, learns faster)")
        print("2) DevOps Warrior (Balanced)")
        print("3) Kubernetes Wizard (Takes less damage, harder challenges)")
        
        choice = input("\nYour choice (1-3): ").strip()
        role_map = {
            "1": (DevOpsRole.JUNIOR_DEV, 50),
            "2": (DevOpsRole.DEVOPS_WARRIOR, 100),
            "3": (DevOpsRole.KUBERNETES_WIZARD, 150),
        }
        
        if choice in role_map:
            self.role, self.health = role_map[choice]
            print(f"\n✨ You are now a {self.role.name}! Health: {self.health}HP\n")
        else:
            print("Invalid choice! Defaulting to DevOps Warrior.")
            self.role = DevOpsRole.DEVOPS_WARRIOR
            self.health = 100
    
    def display_status(self):
        """Display current game status"""
        health_bar = "❤️ " * (self.health // 20) + "🖤 " * (5 - self.health // 20)
        stability_bar = "✅ " * (self.production_stability // 10) + "⚠️ " * (10 - self.production_stability // 10)
        
        print("\n" + "-"*70)
        print(f"🎮 Status: {self.player_name} ({self.role.name})")
        print(f"   Health: {health_bar} ({self.health}HP)")
        print(f"   Production Stability: {stability_bar} ({self.production_stability}%)")
        print(f"   Score: {self.score} | Challenges: {self.challenges_completed}")
        print("-"*70 + "\n")
    
    def ask_challenge(self, challenge: Challenge):
        """Present a challenge to the player"""
        print(f"\n🎯 CHALLENGE: {challenge.title}")
        print(f"   Difficulty: {'🔥' * challenge.difficulty.value}")
        print(f"\n{challenge.description}\n")
        
        for option in challenge.options:
            print(f"   {option}")
        
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()
        
        if answer == challenge.correct_answer:
            self._correct_answer(challenge)
        elif answer in ["A", "B", "C", "D"]:
            self._incorrect_answer(challenge)
        else:
            print("❌ Invalid input! Skipping this challenge.")
    
    def _correct_answer(self, challenge: Challenge):
        """Handle correct answer"""
        points = challenge.difficulty.value * 10
        self.score += points
        self.production_stability = min(100, self.production_stability + (challenge.difficulty.value * 5))
        self.challenges_completed += 1
        
        print("\n✅ CORRECT! 🎉")
        print(f"   +{points} points!")
        print(f"   Production stability: +{challenge.difficulty.value * 5}%")
        print(f"\n{challenge.lesson}")
    
    def _incorrect_answer(self, challenge: Challenge):
        """Handle incorrect answer"""
        damage = challenge.difficulty.value * 10
        self.health -= damage
        self.production_stability = max(0, self.production_stability - (challenge.difficulty.value * 5))
        
        print(f"\n❌ OOPS! Wrong answer!")
        print(f"   -{damage} HP!")
        print(f"   Production stability: -{challenge.difficulty.value * 5}%")
        print(f"\n{challenge.lesson}")
        print(f"\n💡 The correct answer was: {challenge.correct_answer}")
    
    def play(self):
        """Main game loop"""
        self.get_player_name()
        
        challenge_pool = self.challenges.copy()
        
        while self.health > 0 and len(challenge_pool) > 0:
            self.display_status()
            
            # Random challenge
            challenge = random.choice(challenge_pool)
            challenge_pool.remove(challenge)
            
            self.ask_challenge(challenge)
            
            if self.challenges_completed < len(self.challenges):
                cont = input("\n🎮 Continue? (y/n): ").strip().lower()
                if cont != 'y':
                    break
        
        self.end_game()
    
    def end_game(self):
        """Display end game results"""
        print("\n" + "="*70)
        print("🎬 GAME OVER! 🎬")
        print("="*70 + "\n")
        
        self.display_status()
        
        if self.health <= 0:
            print("💔 Oh no! Your infrastructure crashed spectacularly!")
            print("   Your boss is updating their LinkedIn...")
        elif self.production_stability >= 80:
            print("🏆 LEGENDARY! You've mastered DevOps!")
            print("   Your infrastructure is bulletproof!")
        elif self.production_stability >= 60:
            print("🎖️ EXCELLENT! You're a DevOps professional!")
            print("   Your systems are stable and reliable!")
        elif self.production_stability >= 40:
            print("👍 GOOD! You understand DevOps basics!")
            print("   Keep learning and you'll be amazing!")
        else:
            print("😅 LEARNING! Keep practicing - you'll get there!")
        
        print(f"\n📊 Final Score: {self.score}")
        print(f"📈 Challenges Completed: {self.challenges_completed}/{len(self.challenges)}")
        print(f"🛡️ Production Stability: {self.production_stability}%")
        
        # Fun facts
        facts = [
            "💡 Did you know? Netflix's Chaos Monkey intentionally breaks things to test resilience!",
            "🐧 Did you know? Kubernetes means 'pilot' in Greek!",
            "🚀 Did you know? Amazon deploys to production every 11.7 seconds!",
            "📦 Did you know? Docker was named after the British children's show!",
        ]
        print(f"\n{random.choice(facts)}")
        print("\n" + "="*70)
        print("Thanks for playing! Keep your infrastructure running! 🚀")
        print("="*70 + "\n")

def main():
    """Entry point"""
    game = DevOpsGame()
    game.play()

if __name__ == "__main__":
    main()
