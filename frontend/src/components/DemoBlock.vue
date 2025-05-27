<template>
  <div class="demo-block">
    <!-- Блок загрузки -->
    <div class="demo-section">
      <h2 class="demo-title">Загрузить файл</h2>

      <label class="custom-upload-btn">
        Выбрать файл
        <input type="file" accept=".dxf,.dwg" @change="onFileChange" class="input_file_hidden" />
      </label>

      <p class="selected-file-name" v-if="file">Выбран: {{ file.name }}</p>

      <h2 class="demo-title">Начать расчёт</h2>
      <button :disabled="!file || loading" @click="handleRun" class="demo-button">
        СТАРТ
      </button>
    </div>

    <!-- Окно вывода -->
    <div class="demo-output-window">
      <h3 class="result_button">Результат</h3>
      <div class="output-box">
        <pre v-if="loading">Загрузка...</pre>
        <pre v-else-if="result">{{ result }}</pre>
        <p v-else class="output-placeholder">Здесь появится результат</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const file = ref(null)
const result = ref('')
const loading = ref(false)

function onFileChange(e) {
  result.value = ''
  file.value = e.target.files[0]
}

async function handleRun() {
  if (!file.value) return
  loading.value = true
  result.value = ''
  const formData = new FormData()
  formData.append('file', file.value)
  try {
    const { data } = await axios.post('/api/demo/upload', formData)
    result.value = data.result
  } catch (e) {
    result.value = 'Ошибка: ' + (e.response?.data?.detail || e.message)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.demo-block {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  border: 1px solid #2f56914d;
  box-shadow: 0 0 10px rgba(37,35,35,0.2);
  padding: 2.1rem;
  border-radius: 36px;
}

.demo-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.demo-section {
  margin-bottom: 1rem;
}

.demo-button {
  padding: 0.6rem 1.2rem;
  background-color: #012b85;
  color: white;
  border: none;
  border-radius: 0.6rem;
  font-size: 1rem;
  cursor: pointer;
}
.demo-button:hover {
  background-color: #012b8591;
}

.demo-button:disabled {
  background-color: #012b8521;
  cursor: not-allowed;
}

.demo-output-window {
  background: #f9f9f9;
  padding: 1.2rem;
  border-radius: 1rem;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.05);
}

.output-box {
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 0.6rem;
  padding: 1rem;
  max-height: 300px;
  overflow: auto;
  font-family: monospace;
  font-size: 0.95rem;
  white-space: pre-wrap;
}

.output-placeholder {
  color: #999;
  font-style: italic;
}

.input_file {
  margin: 1rem 0;
  padding: 0.5rem;
  border-radius: 0.6rem;
  font-size: 1rem;
}
.input_file_hidden {
  display: none;
}

.custom-upload-btn {
  display: inline-block;
  background-color: #012b85;
  color: white;
  padding: 0.6rem 1.2rem;
  font-size: 1rem;
  border: none;
  border-radius: 0.6rem;
  cursor: pointer;
  margin-bottom: 0.5rem;
  transition: background-color 0.2s;
}

.custom-upload-btn:hover {
  background-color: #012b8591;
}

.selected-file-name {
  margin-top: 0.3rem;
  font-size: 0.95rem;
  color: #333;
}

/* ====== Мобильная адаптация ====== */
@media (max-width: 768px) {
.demo-title {
  font-size: 0.81rem;
}
/* .h3 {
  font-size: 0.6rem;
} */
.custom-upload-btn {
  font-size: 0.66rem;
}
.demo-button {
  font-size: 0.66rem;
}
.result_button {
  font-size: 0.81rem;
}
.output-placeholder {
  font-size: 0.66rem;
}
}

/* ====== Широкие экраны (например 1440px+) ====== */
@media (min-width: 1440px) {
.demo-title {
  font-size: 0.9rem;
}
.result_button {
  font-size: 0.54rem;
}
}
</style>
