<template>
  <div :class="['chat-wrap', messages.length ? 'has-messages' : '']">
    <div class="chat-messages" ref="messagesEnd">
      <div
        v-for="(msg, i) in messages"
        :key="i"
        :class="['chat-row', msg.role === 'user' ? 'right' : 'left']"
      >
        <div
          :class="[
            'chat-bubble',
            msg.role === 'user' ? 'bubble-user' : 'bubble-ai'
          ]"
        >
          <p>{{ msg.text }}</p>
        </div>
      </div>
    </div>
    <form class="chat-form" @submit.prevent="sendMessage">
      <input
        v-model="input"
        type="text"
        class="chat-input"
        placeholder="Спроси меня о чем-нибудь :)"
        autocomplete="off"
      />
      <button
        type="submit"
        class="chat-send"
        :disabled="!input.trim()"
        title="Отправить"
      >
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
          <path d="M3 21L21 12L3 3V10L17 12L3 14V21Z" fill="currentColor"/>
        </svg>
      </button>
    </form>
  </div>
</template>


<script setup>
import { ref, nextTick } from 'vue'

const input = ref('')
const messages = ref([])
const messagesEnd = ref(null)

async function sendMessage() {
  if (!input.value.trim()) return
  messages.value.push({ role: 'user', text: input.value })
  const question = input.value
  input.value = ''

  try {
    const res = await fetch('/api/llm_chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    })
    const { answer } = await res.json()
    messages.value.push({ role: 'ai', text: answer })
    await nextTick()
    // автоскролл вниз
    const el = messagesEnd.value
    if (el) el.scrollTop = el.scrollHeight
  } catch (e) {
    messages.value.push({ role: 'ai', text: 'Ошибка сервера, попробуйте позже.' })
  }
}
</script>

<style scoped>
.chat-wrap {
  width: 100%;
  max-width: 1020px;
  margin-top: 24%;
  margin-left: auto;
  margin-right: auto;
  background: #ffffff;
  border-radius: 36px;
  box-shadow: 0 8px 36px #3e6eab0a, 0 1px 5px #6e8bd91c;
  padding: 26px 18px 16px 18px;
  display: flex;
  flex-direction: column;
  min-height: 310px;
  height: 5vh;
  border: 1px solid #4b4b4b8e;
  box-shadow: 0 2px 12px #0c315f25, 0 1px 3px #6e8bd91c;
  transition: min-height 0.5s cubic-bezier(.6,0,.39,1), max-height 0.5s cubic-bezier(.6,0,.39,1);
  min-height: 80px;
  max-height: 430px;
  height: auto;
  overflow: hidden;
}

.chat-wrap.has-messages {
  min-height: 270px;
}

.chat-messages {
  flex: 1 1 100%;
  overflow-y: auto;
  padding-bottom: 4px;
  margin-bottom: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  scrollbar-width: thin;
  scrollbar-color: #b3cdfa #f7faff;
  transition: max-height 0.5s cubic-bezier(.6,0,.39,1);
  max-height: 270px;
}
.chat-row {
  display: flex;
  width: 100%;
}
.chat-row.left {
  justify-content: flex-start;
}
.chat-row.right {
  justify-content: flex-end;
}
.chat-bubble {
  max-width: 85%;
  padding: 12px 18px;
  border-radius: 17px 17px 17px 5px;
  margin-bottom: 2px;
  font-size: 1.1rem;
  line-height: 1.45;
  word-break: break-word;
  box-shadow: 0 2px 16px #81c7ff12;
  transition: background 0.18s;
  animation: bubbleIn .25s;
}
@keyframes bubbleIn {
  from {opacity: 0; transform: translateY(14px) scale(.97);}
  to   {opacity: 1; transform: translateY(0) scale(1);}
}

.bubble-user {
  background: linear-gradient(45deg, #3a118546 20%, #376cb196 100%);
  color: #fff;
  border-radius: 17px 17px 7px 17px;
  align-self: flex-end;
  box-shadow: 0 3px 18px #3584e610;
}
.bubble-ai {
  background: #fff;
  color: #213359;
  border: 1.5px solid #d6c4eb8e;
  align-self: flex-start;
}

.chat-form {
  display: flex;
  align-items: center;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 2px 12px #3584e606;
  padding: 7px 8px 7px 14px;
  gap: 12px;
  position: relative;
}

.chat-input {
  flex: 1 1 80%;
  border: none;
  background: transparent;
  outline: none;
  font-size: 1.13rem;
  color: #222;
  padding: 7px 6px;
  border-radius: 8px;
  border: 1px solid #c4d0eb8e;
}

.chat-input::placeholder {
  color: #9eb6d6;
  font-style: italic;
}

.chat-send {
  background: linear-gradient(90deg, #3286ef 70%, #49b7ff 100%);
  color: #fff;
  border: none;
  border-radius: 50%;
  width: 38px;
  height: 38px;
  font-size: 1.32rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.16s, transform 0.12s;
  box-shadow: 0 2px 10px #3584e626;
  cursor: pointer;
}
.chat-send:disabled {
  opacity: 0.45;
  cursor: not-allowed;
  filter: grayscale(0.2);
}
.chat-send:not(:disabled):hover {
  background: linear-gradient(90deg, #266ad7 80%, #38a0e7 100%);
  transform: scale(1.1);
}
</style>
