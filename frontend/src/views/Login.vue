<template>
      <div class="form-container">
        <form @submit.prevent="onLogin">
          <label>Логин или емейл</label>
          <input type="text" v-model="login" placeholder="Введите логин или емейл" required />
  
          <div class="password-label">
            <label>Пароль</label>
            <a href="#" class="restore">Восстановить</a>
          </div>
          <input type="password" v-model="password" placeholder="Введите пароль" required />
          <p v-if="errorMessage" class="error-msg">{{ errorMessage }}</p>        
          <button type="submit">Войти в панель управления</button>
  
          <p class="bottom-link">
            Нет аккаунта?
            <router-link to="/register">Зарегистрируйтесь</router-link>
          </p>
        </form>
      </div>
  </template>
  
  <script setup>
  import Header from '@/components/Header.vue'
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import axios from 'axios'
  
  const router = useRouter()
  const login = ref('')
  const password = ref('')
  const errorMessage = ref('')
  
  const onLogin = async () => {
    errorMessage.value = ''

    try {
      const response = await axios.post('/api/login', {
        email: login.value,
        password: password.value
      })
      console.log('Успешный логин', response.data)
      router.push('/cabinet')
    } catch (error) {
      if (error.response?.data?.detail) {
        errorMessage.value = error.response.data.detail
      } else {
        errorMessage.value = 'Произошла ошибка входа'
      }
      console.error('Ошибка логина', error)
    }
  }
  </script>
  
  <style scoped>
  .auth-page {
    background: #0e1015;
    min-height: 100vh;
    color: #fff;
  }
  
  .form-container {
    max-width: 30%;
    margin: 15% auto;
    background: #9ea5c446;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.3);
    max-width: 450px;
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
  }
  
  input {
    width: 100%;
    padding: 0.75vw;
    margin-bottom: 1.5vw;
    border: 1px solid #2a2d34;
    border-radius: 8px;
    background: #ffffff;
    color: #000000;
    font-size: 1rem;
  }

    input,
    button[type="submit"] {
    width: 100%;
    box-sizing: border-box;
    }
  
  button {
    width: 100%;
    padding: 0.8rem;
    background: #000000;
    border: none;
    color: #fff;
    border-radius: 8px;
    font-weight: bold;
    font-size: 1rem;
    cursor: pointer;
  }
  button:hover {
    background: #7083b1;
  }
  
  .restore {
    font-size: 0.85rem;
    color: #7083b1;
    text-decoration: none;
  }
  
  .password-label {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .bottom-link {
    text-align: center;
    margin-top: 1.5rem;
    font-size: 0.9rem;
  }
  .bottom-link a {
    color: #7083b1;
    text-decoration: none;
  }
  </style>
  