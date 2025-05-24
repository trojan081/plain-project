<template>
  <div class="form-container">
    <form @submit.prevent="onRegister">
      <label>Ваш email</label>
      <input type="email" v-model="email" placeholder="Введите email" required />

      <label>Пароль</label>
      <input type="password" v-model="password" placeholder="Введите пароль" required />

      <p v-if="errorMessage" class="error-msg">{{ errorMessage }}</p>
      <button type="submit">Зарегистрироваться</button>

      <div class="checkbox">
        <input type="checkbox" id="privacy" v-model="agreed" required />
        <label for="privacy">
          Я ознакомлен(а) с
          <router-link to="/policy">Политикой</router-link>,
          <router-link to="/offer">Офертой</router-link> и даю
          <router-link to="/main_agreement">Согласие</router-link> на обработку персональных данных
        </label>
      </div>
      <div class="checkbox">
        <input type="checkbox" id="subscribe" v-model="subscribed" />
        <label for="subscribe">
          Я даю <router-link to="/agreement">согласие</router-link> на получение информационных рассылок
        </label>
      </div>
      <p class="bottom-link">
        Уже есть аккаунт?
        <router-link to="/login">Войдите</router-link>
      </p>
    </form>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const email = ref('')
const password = ref('')
const agreed = ref(false)
const subscribed = ref(false)
const errorMessage = ref('')

onMounted(async () => {
  try {
    await axios.get('api/cabinet', { withCredentials: true })
    router.push({ name: 'Cabinet' })
  } catch {
    // 401 или другая ошибка — остаёмся на регистрации
  }
})
async function onRegister() {
  errorMessage.value = ''

  try {
    const response = await axios.post('/api/register', {
      email: email.value,
      password: password.value,
      agreed_offer:    agreed.value,
      agreed_personal: agreed.value,
      agreed_policy:   agreed.value,
      agreed_advertisement: subscribed.value
    })
    console.log('Успешная регистрация!', response.data)
    router.push('/cabinet')
  } catch (error) {
    if (error.response?.status === 400) {
      if (error.response.data.detail.includes('already exists')) {
    errorMessage.value = 'Пользователь с таким email уже зарегистрирован'
  } else {
    errorMessage.value = 'Не удалось зарегистрироваться'
  }
  console.error(error)
}
  }
}

</script>

<style scoped>
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
  max-height: 45px;
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
  margin-bottom: 1rem;
}
button:hover {
  background: #7083b1;
}

.checkbox {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0.5rem;
  align-items: start;
  margin-bottom: 1rem;
  font-size: 0.85rem;
}

.checkbox a {
  color: #7083b1;
  text-decoration: none;
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
