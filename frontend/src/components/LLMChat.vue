<template>
  <div class="llm-chat">
  <text class="title">AI-помощник Plain</text>
    <Cube1 />
  </div>
  <p class="llm_description">Мы активно внедряем искусственный интеллект в наш сервис. Воспользуйтесь нашим ИИ-ассистентом:</p>
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
          <p>
            {{ msg.text }}
            <span v-if="msg.role === 'ai' && isTyping" class="blinking-cursor">|</span>
          </p>
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
        :disabled="isSending" />
      <button
        type="submit"
        class="chat-send"
        :disabled="!input.trim() || isSending" title="Отправить"
      >
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
          <path d="M3 21L21 12L3 3V10L17 12L3 14V21Z" fill="currentColor"/>
        </svg>
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, nextTick, onMounted, onBeforeUnmount } from 'vue'
import Cube1 from './Cube1.vue' 

function handleWheelBlockPageScroll(e) {
  const el = messagesEnd.value
  if (!el) return

  const deltaY = e.deltaY
  const atTop = el.scrollTop === 0
  const atBottom = el.scrollTop + el.clientHeight >= el.scrollHeight - 1

  const scrollingDown = deltaY > 0
  const scrollingUp = deltaY < 0

  // Если прокручиваем вверх и уже вверху — останавливаем всплытие
  // Если прокручиваем вниз и уже внизу — тоже
  if ((scrollingUp && atTop) || (scrollingDown && atBottom)) {
    e.preventDefault()
    e.stopPropagation()
  }
}

onMounted(() => {
  const el = messagesEnd.value
  if (el) {
    el.addEventListener('wheel', handleWheelBlockPageScroll, { passive: false })
  }
})

onBeforeUnmount(() => {
  const el = messagesEnd.value
  if (el) {
    el.removeEventListener('wheel', handleWheelBlockPageScroll)
  }
})

const input = ref('')
const messages = ref([])
const messagesEnd = ref(null)
const isSending = ref(false)

// Функция для автопрокрутки
async function scrollToBottom() {
  await nextTick() // Ждем, пока DOM обновится
  const el = messagesEnd.value
  if (el) {
    el.scrollTop = el.scrollHeight
  }
}

async function sendMessage() {
  if (!input.value.trim() || isSending.value) return // Добавляем проверку isSending
  isSending.value = true // Устанавливаем состояние отправки в true

  const userMessage = { role: 'user', text: input.value }
  messages.value.push(userMessage)
  scrollToBottom() // Прокрутка после добавления сообщения пользователя

  const question = input.value
  input.value = '' // Очищаем поле ввода сразу

  // Добавляем пустое сообщение AI, чтобы начать получать токены
  const aiMessage = { role: 'ai', text: '' }
  messages.value.push(aiMessage)
  
  try {
    const res = await fetch('/api/llm_chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    })

    if (!res.ok) {
      const errorData = await res.json();
      throw new Error(errorData.error || 'Server error');
    }

    // Читаем поток
    const reader = res.body.getReader()
    const decoder = new TextDecoder()
    let buffer = '' // Буфер для неполных JSON-объектов

    while (true) {
      const { value, done } = await reader.read()
      if (done) break

      buffer += decoder.decode(value, { stream: true })
      
      // Обработка нескольких JSON-объектов, разделенных новой строкой
      const lines = buffer.split('\n')
      buffer = lines.pop() // Последняя строка может быть неполной

      for (const line of lines) {
        if (!line.trim()) continue
        try {
          const json_data = JSON.parse(line)
          const token = json_data.token || ''
          if (token) {
            // Добавляем состояние для отслеживания печати
            const isTyping = ref(true)
            
            // Печатаем текст по буквам с плавной анимацией
            for (const char of token) {
              aiMessage.text += char
              await nextTick()
              await new Promise(resolve => setTimeout(resolve, 25)) // Увеличиваем задержку для более заметного эффекта
              scrollToBottom()
            }
            
            isTyping.value = false
          }
        } catch (e) {
          console.error('Error parsing JSON chunk:', e, 'Chunk:', line)
        }
      }
    }

  } catch (e) {
    console.error('Fetch error:', e)
    // Если сообщение AI пустое, добавляем сообщение об ошибке, иначе модифицируем существующее
    if (aiMessage.text === '') {
        messages.value.pop() // Удаляем пустое AI сообщение
        messages.value.push({ role: 'ai', text: `Ошибка: ${e.message || 'Неизвестная ошибка сервера, попробуйте позже.'}` })
    } else {
        aiMessage.text += `\n\n(Ошибка: ${e.message || 'Неизвестная ошибка'})`
    }
    scrollToBottom()
  } finally {
    isSending.value = false // Сбрасываем состояние отправки
  }
}

</script>

<style scoped>
/* Ваш CSS остаётся без изменений */
.chat-wrap {
  width: 100%;
  max-width: 1020px;
  margin-top: 6%;
  margin-bottom: 12%;
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
  min-height: 120px;
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
  scrollbar-color: #dfdfdf #f7faff;
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
  background: linear-gradient(45deg, #00000046 20%, #777373a1 100%);
  color: #fff;
  border-radius: 17px 17px 7px 17px;
  align-self: flex-end;
  box-shadow: 0 3px 18px #a8a2a236;
}
.bubble-ai {
  background: #fff;
  color: #213359;
  border: 1.5px solid #5e2a2a38;
  align-self: flex-start;
}

.chat-form {
  display: flex;
  align-items: center;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 2px 12px #2761a806;
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
  border: 1px solid #cacaca8e;
}

.chat-input::placeholder {
  color: #c9c9c9;
  font-style: italic;
}

.chat-send {
  background: linear-gradient(90deg, #ff6f6f 70%, #e0c6c6 100%);
  color: #f8f8f8;
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
  background: linear-gradient(90deg, #d4e48b 70%, #e0c6c6 100%);
  transform: scale(1.1);
}

.title {
  text-align: center;
  font-size: clamp(0.8rem, 4vw + 0.5rem, 2.8rem);
  color: rgb(50,50,50);
  margin-top: 10rem;
  font-weight: bold;
}

.llm_description {
  margin-top: 40px;
  margin-left: auto;
  margin-right: auto;
}

.llm-chat {
  width: 100%;
  max-width: 1020px;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}
@media (max-width: 768px) {
  .chat-wrap {
    padding: 1rem;
    border-radius: 1.2rem;
  }

  .chat-bubble {
    font-size: 0.95rem;
    padding: 0.6rem 0.9rem;
    margin: 4%;
  }

  .chat-form {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
  }

  .chat-input {
    width: 90%;
    min-width: unset;
  }

  .chat-send {
    width: 100%;
    border-radius: 0.6rem;
    margin: 0 auto;
  }

  .title {
    font-size: 1.6rem;
    margin-top: 3rem;
  }

  .llm_description {
    font-size: 0.95rem;
    margin: 4%;
  }
}
</style>