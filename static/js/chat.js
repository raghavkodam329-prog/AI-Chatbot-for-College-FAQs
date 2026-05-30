document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chatForm');
    const userInput = document.getElementById('userInput');
    const chatMessages = document.getElementById('chatMessages');
    const suggestionBtns = document.querySelectorAll('.suggestion-btn');

    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        sendMessage(userInput.value);
    });

    suggestionBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            sendMessage(this.textContent);
        });
    });

    function linkify(text) {
        // Regular expression to match URLs
        const urlPattern = /(https?:\/\/[^\s]+)/g;
        return text.replace(urlPattern, function(url) {
            return `<a href="${url}" target="_blank" rel="noopener noreferrer" style="color: #007bff; text-decoration: underline;">${url}</a>`;
        });
    }

    function sendMessage(message) {
        if (!message.trim()) return;
        
        addMessage(message, 'user');
        userInput.value = '';
        
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            addMessage(data.response, 'bot');
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    function addMessage(text, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;
        
        const p = document.createElement('p');
        p.innerHTML = linkify(text.replace(/\n/g, '<br>'));
        messageDiv.appendChild(p);
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
