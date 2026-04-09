function getTime() {
  return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function appendMessage(text, sender) {
  const container = document.getElementById('chatMessages');

  const wrapper = document.createElement('div');
  wrapper.classList.add('message', sender);

  const bubble = document.createElement('div');
  bubble.classList.add('bubble');
  bubble.innerHTML = sender === 'bot'
    ? text.replace(/</g, '&lt;').replace(/\n/g, '<br/>').replace(/`([^`]+)`/g, '<code>$1</code>')
    : text.replace(/</g, '&lt;');

  const time = document.createElement('div');
  time.classList.add('msg-time');
  time.textContent = getTime();

  wrapper.appendChild(bubble);
  wrapper.appendChild(time);
  container.appendChild(wrapper);
  container.scrollTop = container.scrollHeight;
}

function showTyping() {
  document.getElementById('typingIndicator').classList.add('visible');
}

function hideTyping() {
  document.getElementById('typingIndicator').classList.remove('visible');
}

async function sendMessage() {
  const input = document.getElementById('userInput');
  const text = input.value.trim();

  if (!text) {
    appendMessage("Please type something. Try 'help' to see available commands.", 'bot');
    return;
  }

  appendMessage(text, 'user');
  input.value = '';
  showTyping();

  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });

    const data = await res.json();
    const delay = Math.floor(Math.random() * 1000) + 500;
    await new Promise(resolve => setTimeout(resolve, delay));

    hideTyping();

    if (data.response === '__CLEAR__') {
      clearChat();
      return;
    }

    appendMessage(data.response, 'bot');
  } catch (err) {
    hideTyping();
    appendMessage('Connection error. Make sure the server is running.', 'bot');
  }
}

function askBot(question) {
  document.getElementById('userInput').value = question;
  sendMessage();
}

function clearChat() {
  const container = document.getElementById('chatMessages');
  container.innerHTML = '';
  appendMessage(
    "Chat cleared. I'm EduBot — ask me anything about courses, fees, or enrollment. Type `help` to start.",
    'bot'
  );
}