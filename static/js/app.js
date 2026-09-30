class DevOpsQuestGame {
    constructor() {
        this.state = 'start'; // start, challenge, end
        this.playerName = '';
        this.role = 'DEVOPS_WARRIOR';
        this.init();
    }

    init() {
        this.render();
    }

    render() {
        const app = document.getElementById('app');
        app.innerHTML = `
            <div class="container">
                <div class="header">
                    <h1>🎮 DEVOPS QUEST 🚀</h1>
                    <p>The Hilarious Journey to Production</p>
                </div>
                <div class="content" id="content">
                    ${this.getContent()}
                </div>
            </div>
        `;
        this.attachEventListeners();
    }

    getContent() {
        if (this.state === 'start') {
            return this.getStartScreen();
        } else if (this.state === 'challenge') {
            return this.getChallengeScreen();
        } else if (this.state === 'end') {
            return this.getEndScreen();
        }
    }

    getStartScreen() {
        return `
            <div class="start-screen">
                <h2>Welcome, DevOps Warrior! 🎉</h2>
                <p style="margin-bottom: 30px; color: #666; font-size: 1.1em;">
                    Learn DevOps concepts while saving your company from chaos!
                </p>
                
                <form id="startForm">
                    <div class="form-group">
                        <label for="playerName">👤 What's your name?</label>
                        <input type="text" id="playerName" name="playerName" placeholder="Enter your name" required>
                    </div>
                    
                    <div class="form-group">
                        <label>🎮 Choose your starting role:</label>
                        <div class="role-options">
                            <div class="role-option">
                                <input type="radio" name="role" value="JUNIOR_DEV" id="role1">
                                <label for="role1">Junior Dev</label>
                                <p style="font-size: 0.9em; color: #666; margin-top: 5px;">Takes more damage, learns faster (50 HP)</p>
                            </div>
                            <div class="role-option">
                                <input type="radio" name="role" value="DEVOPS_WARRIOR" id="role2" checked>
                                <label for="role2">DevOps Warrior</label>
                                <p style="font-size: 0.9em; color: #666; margin-top: 5px;">Balanced stats (100 HP)</p>
                            </div>
                            <div class="role-option">
                                <input type="radio" name="role" value="KUBERNETES_WIZARD" id="role3">
                                <label for="role3">Kubernetes Wizard</label>
                                <p style="font-size: 0.9em; color: #666; margin-top: 5px;">Takes less damage, harder challenges (150 HP)</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="button-group">
                        <button type="submit" class="btn-primary" style="width: 100%; padding: 15px;">Start Game 🚀</button>
                    </div>
                </form>
            </div>
        `;
    }

    getChallengeScreen() {
        return `
            <div class="challenge-screen" id="challengeScreen" style="display: block;">
                <div class="status-bar" id="statusBar"></div>
                <div class="lesson-box" id="lessonBox"></div>
                <div class="result-box" id="resultBox"></div>
                <div id="challengeContent" style="display: none;">
                    <h2 class="challenge-title" id="challengeTitle"></h2>
                    <div class="difficulty-badge" id="difficultyBadge"></div>
                    <p class="challenge-description" id="challengeDescription"></p>
                    <div class="options-container" id="optionsContainer"></div>
                    <div class="button-group">
                        <button class="btn-primary" id="submitBtn" disabled>Submit Answer</button>
                    </div>
                </div>
                <div id="loadingContainer" style="text-align: center; padding: 40px;">
                    <div class="loading"></div>
                    <p>Loading challenge...</p>
                </div>
            </div>
        `;
    }

    getEndScreen() {
        return `
            <div class="end-screen" id="endScreen">
                <div id="endContent"></div>
            </div>
        `;
    }

    attachEventListeners() {
        if (this.state === 'start') {
            const form = document.getElementById('startForm');
            form.addEventListener('submit', (e) => this.handleStartGame(e));
            
            // Update role selection styling
            const roleOptions = document.querySelectorAll('.role-option');
            roleOptions.forEach(option => {
                const radio = option.querySelector('input[type="radio"]');
                option.addEventListener('click', () => {
                    roleOptions.forEach(o => o.classList.remove('selected'));
                    option.classList.add('selected');
                    radio.checked = true;
                });
                if (radio.checked) {
                    option.classList.add('selected');
                }
            });
        } else if (this.state === 'challenge') {
            this.loadChallenge();
        } else if (this.state === 'end') {
            // End screen already loaded
        }
    }

    async handleStartGame(e) {
        e.preventDefault();
        const playerName = document.getElementById('playerName').value;
        const role = document.querySelector('input[name="role"]:checked').value;
        
        try {
            const response = await fetch('/api/start-game', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ player_name: playerName, role: role })
            });
            
            if (response.ok) {
                this.playerName = playerName;
                this.role = role;
                this.state = 'challenge';
                this.render();
            }
        } catch (error) {
            alert('Error starting game: ' + error);
        }
    }

    async loadChallenge() {
        try {
            const statusResponse = await fetch('/api/game-status');
            const status = await statusResponse.json();
            this.updateStatusBar(status);
            
            const challengeResponse = await fetch('/api/next-challenge');
            
            if (!challengeResponse.ok) {
                // No more challenges
                this.endGame();
                return;
            }
            
            const challenge = await challengeResponse.json();
            this.displayChallenge(challenge);
        } catch (error) {
            alert('Error loading challenge: ' + error);
        }
    }

    updateStatusBar(status) {
        const statusBar = document.getElementById('statusBar');
        const healthPercent = Math.max(0, Math.min(100, (status.health / 150) * 100));
        
        statusBar.innerHTML = `
            <div class="status-item">
                <span class="status-label">❤️ Health</span>
                <div class="status-value">
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: ${healthPercent}%">${status.health}</div>
                    </div>
                </div>
                <span class="status-number">${status.health} HP</span>
            </div>
            <div class="status-item">
                <span class="status-label">✅ Production Stability</span>
                <div class="status-value">
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: ${status.production_stability}%">${status.production_stability}%</div>
                    </div>
                </div>
                <span class="status-number">${status.production_stability}%</span>
            </div>
            <div class="status-item">
                <span class="status-label">🎮 Score</span>
                <span class="status-number">${status.score}</span>
            </div>
            <div class="status-item">
                <span class="status-label">📊 Challenges</span>
                <span class="status-number">${status.challenges_completed}/${status.total_challenges}</span>
            </div>
        `;
    }

    displayChallenge(challenge) {
        document.getElementById('loadingContainer').style.display = 'none';
        document.getElementById('challengeContent').style.display = 'block';
        
        document.getElementById('challengeTitle').textContent = challenge.title;
        document.getElementById('difficultyBadge').textContent = '🔥'.repeat({
            'LOW': 1,
            'MEDIUM': 2,
            'CRITICAL': 3,
            'ABSOLUTE_DISASTER': 4
        }[challenge.difficulty] || 1) + ' ' + challenge.difficulty;
        document.getElementById('challengeDescription').textContent = challenge.description;
        
        const optionsContainer = document.getElementById('optionsContainer');
        optionsContainer.innerHTML = challenge.options.map((option, index) => `
            <div class="option">
                <input type="radio" name="answer" value="${['A', 'B', 'C', 'D'][index]}" id="option${index}">
                <label for="option${index}" style="cursor: pointer;">${option}</label>
            </div>
        `).join('');
        
        const options = document.querySelectorAll('.option');
        options.forEach(option => {
            option.addEventListener('click', () => {
                options.forEach(o => o.classList.remove('selected'));
                option.classList.add('selected');
                const radio = option.querySelector('input[type="radio"]');
                radio.checked = true;
                document.getElementById('submitBtn').disabled = false;
            });
        });
        
        document.getElementById('submitBtn').addEventListener('click', () => this.submitAnswer());
    }

    async submitAnswer() {
        const answer = document.querySelector('input[name="answer"]:checked').value;
        
        try {
            const response = await fetch('/api/submit-answer', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ answer: answer })
            });
            
            if (response.ok) {
                const result = await response.json();
                this.displayResult(result);
            }
        } catch (error) {
            alert('Error submitting answer: ' + error);
        }
    }

    displayResult(result) {
        const lessonBox = document.getElementById('lessonBox');
        const resultBox = document.getElementById('resultBox');
        const submitBtn = document.getElementById('submitBtn');
        const optionsContainer = document.getElementById('optionsContainer');
        
        // Show lesson
        lessonBox.textContent = result.lesson;
        lessonBox.classList.add('show');
        if (!result.is_correct) {
            lessonBox.classList.add('wrong');
        } else {
            lessonBox.classList.remove('wrong');
        }
        
        // Show result
        resultBox.classList.add('show');
        if (result.is_correct) {
            resultBox.classList.add('correct');
            resultBox.classList.remove('wrong');
            resultBox.innerHTML = `
                <div class="result-message">✅ CORRECT! 🎉</div>
                <div>+${(result.score - result.score + 10)} points!</div>
            `;
        } else {
            resultBox.classList.add('wrong');
            resultBox.classList.remove('correct');
            resultBox.innerHTML = `
                <div class="result-message">❌ Wrong Answer!</div>
                <div>The correct answer was: <strong>${result.correct_answer}</strong></div>
            `;
        }
        
        // Disable options and submit button
        optionsContainer.querySelectorAll('input').forEach(input => input.disabled = true);
        submitBtn.disabled = true;
        submitBtn.textContent = 'Loading next challenge...';
        
        // Update status
        const statusResponse = fetch('/api/game-status');
        statusResponse.then(res => res.json()).then(status => {
            this.updateStatusBar(status);
        });
        
        // Load next challenge after delay
        setTimeout(() => {
            document.getElementById('loadingContainer').style.display = 'block';
            document.getElementById('challengeContent').style.display = 'none';
            lessonBox.classList.remove('show');
            resultBox.classList.remove('show');
            document.getElementById('submitBtn').textContent = 'Submit Answer';
            this.loadChallenge();
        }, 2000);
    }

    async endGame() {
        this.state = 'end';
        
        try {
            const response = await fetch('/api/end-game', { method: 'POST' });
            if (response.ok) {
                const results = await response.json();
                this.displayEndScreen(results);
            }
        } catch (error) {
            alert('Error ending game: ' + error);
        }
    }

    displayEndScreen(results) {
        const endContent = document.getElementById('endContent');
        endContent.innerHTML = `
            <div class="rank-display">${results.rank}</div>
            <p class="rank-message">${results.message}</p>
            
            <div class="stats-grid">
                <div class="stat-box">
                    <div class="stat-label">Final Score</div>
                    <div class="stat-value">${results.final_score}</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Health</div>
                    <div class="stat-value">${results.final_health} HP</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Stability</div>
                    <div class="stat-value">${results.final_stability}%</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">Challenges</div>
                    <div class="stat-value">${results.challenges_completed}/${results.total_challenges}</div>
                </div>
            </div>
            
            <div class="fun-fact">${results.fun_fact}</div>
            
            <div class="button-group">
                <button class="btn-primary" onclick="location.reload()">Play Again 🎮</button>
            </div>
        `;
    }
}

// Initialize game when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new DevOpsQuestGame();
});
