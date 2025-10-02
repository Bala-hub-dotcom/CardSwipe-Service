import streamlit.components.v1 as components

def render_chat_popup():
    chat_html = """
    <style>
      .chat-toggle {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: #38bdf8;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        cursor: pointer;
        z-index: 9999;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      }
      .chat-window {
        position: fixed;
        bottom: 80px;
        right: 20px;
        width: 320px;
        max-height: 420px;
        background: #0b1220;
        color: #f4f7fb;
        border: 1px solid #334155;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        display: none;
        flex-direction: column;
        z-index: 9999;
        overflow: hidden;
      }
      .chat-window.active {
        display: flex;
      }
      .chat-header {
        background: #1e293b;
        padding: 0.8rem;
        font-weight: 600;
        text-align: center;
        border-bottom: 1px solid #334155;
        position: relative;
      }
      .chat-close {
        position: absolute;
        top: 6px;
        right: 10px;
        background: none;
        border: none;
        color: #94a3b8;
        font-size: 1.2rem;
        cursor: pointer;
      }
      .chat-body {
        padding: 1rem;
        font-size: 0.9rem;
        overflow-y: auto;
        flex-grow: 1;
      }
      .chat-input {
        border-top: 1px solid #334155;
        padding: 0.5rem;
        background: #1e293b;
      }
      .chat-input input {
        width: 100%;
        padding: 0.4rem;
        border-radius: 6px;
        border: none;
        font-family: inherit;
        font-size: 0.9rem;
      }
      .typing {
        font-style: italic;
        color: #94a3b8;
        animation: blink 1s steps(1) infinite;
      }
      @keyframes blink {
        0% { opacity: 0.2; }
        50% { opacity: 1; }
        100% { opacity: 0.2; }
      }
      .suggestions {
        margin-top: 0.5rem;
        font-size: 0.85rem;
        color: #94a3b8;
      }
      .suggestion-btn {
        display: block;
        background: #1e293b;
        color: #f4f7fb;
        border: 1px solid #334155;
        border-radius: 6px;
        padding: 0.4rem 0.6rem;
        margin: 0.3rem 0;
        cursor: pointer;
        font-size: 0.85rem;
        text-align: left;
        transition: background 0.3s ease;
      }
      .suggestion-btn:hover {
        background: #334155;
      }
    </style>

    <button class="chat-toggle" onclick="toggleChat()">💬 Chat</button>

    <div class="chat-window" id="chat-window">
      <div class="chat-header">
        Sri Gayathri Chat
        <button class="chat-close" onclick="toggleChat()">❌</button>
      </div>
      <div class="chat-body" id="chat-body">
        <p>👋 Welcome! Ask us anything about our service.</p>
        <div class="suggestions">
          <button class="suggestion-btn" onclick="handleSuggestion('how much cash can i get')">💰 How much cash can I get?</button>
          <button class="suggestion-btn" onclick="handleSuggestion('are you open at night')">🌙 Are you open at night?</button>
          <button class="suggestion-btn" onclick="handleSuggestion('which cards are accepted')">💳 Which cards are accepted?</button>
        </div>
      </div>
      <div class="chat-input">
        <input type="text" id="chat-input" placeholder="Type your question..." onkeydown="handleChat(event)">
      </div>
    </div>

    <script>
      function toggleChat() {
        document.getElementById("chat-window").classList.toggle("active");
      }

      const faq = {
        "is this service legal": "✅ Yes, 100% legitimate and licensed financial service.",
        "which cards are accepted": "💳 We accept Visa, MasterCard, American Express, and RuPay.",
        "do i still earn reward points": "🎁 Yes, you continue to earn your bank’s reward points on eligible transactions.",
        "any hidden charges": "❌ No hidden fees. Flat 2% service charge only.",
        "is gst applicable": "🚫 No, our service is 100% GST-free for maximum savings.",
        "can i use multiple cards in one transaction": "💳 Yes, you can combine multiple cards to reach your desired amount.",
        "do you provide receipts": "🧾 Yes, we provide a detailed receipt for every transaction.",
        "is my data secure": "🔒 Absolutely. We use bank-grade encryption and never store your card details.",
        "what documents are required": "🪪 A valid government-issued ID and your credit card are required for verification.",
        "available at night": "🕒 Yes, we operate 24/7 including weekends and public holidays.",
        "how much cash can i get": "💰 Minimum ₹1,000 and maximum ₹2,00,000, subject to your card limit.",
        "how long does the process take": "⏱ Usually less than 10 minutes once your card is verified.",
        "do you offer card-to-card transfers": "🔄 Yes, we can transfer funds directly between credit cards.",
        "can i pay utility bills through you": "📄 Yes, we support electricity, water, gas, and other utility payments with no extra charges.",
        "do you operate on holidays": "✅ Yes, we are open 365 days a year."
      };

      function handleSuggestion(query) {
        const body = document.getElementById("chat-body");
        body.innerHTML += `<p><strong>You:</strong> ${query}</p>`;
        body.innerHTML += `<p class="typing" id="typing">Bot is typing...</p>`;

        let bestMatch = null;
        let bestScore = 0;

        for (const q in faq) {
          const score = similarity(query, q);
          if (score > bestScore) {
            bestScore = score;
            bestMatch = q;
          }
        }

        setTimeout(() => {
          const typing = document.getElementById("typing");
          if (typing) typing.remove();
          if (bestScore >= 0.6) {
            body.innerHTML += `<p><strong>Bot:</strong> ${faq[bestMatch]}</p>`;
          } else {
            body.innerHTML += `<p><strong>Bot:</strong> 🤖 Sorry, I couldn't find a good match. Please call or WhatsApp us for help.</p>`;
          }
          body.scrollTop = body.scrollHeight;
        }, 800);
      }

      function handleChat(e) {
        if (e.key === "Enter") {
          const input = document.getElementById("chat-input");
          const query = input.value.trim().toLowerCase();
          if (!query) return;
          handleSuggestion(query);
          input.value = "";
        }
      }

      function similarity(a, b) {
        const wordsA = a.split(" ");
        const wordsB = b.split(" ");
        const matchCount = wordsA.filter(word => wordsB.includes(word)).length;
        return matchCount / Math.max(wordsA.length, wordsB.length);
      }
    </script>
    """

    components.html(chat_html, height=0, width=0)