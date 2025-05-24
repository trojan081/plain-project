<!-- frontend/src/views/Cabinet.vue -->
<template>
  <div v-if="loading">Загрузка...</div>
  <div v-else class="panel-layout">
    <!-- Сайдбар с «Мои данные», «Мои проекты», «Мои шаблоны» -->
    <CabinetSidebar />

    <!-- Основная часть: приветствие, фото и место для контента -->
    <div class="panel-content">
      <div class="photo-container">
        <div class="welcome-photo-row">
          <h1 class="welcome-text">Добро пожаловать, {{ welcomeName }}</h1>
          <div class="profile-photo-wrapper" @click="triggerPhotoUpload">
            <template v-if="userInfo.photo_url">
              <img :src="fullPhotoUrl" alt="Фото профиля" class="profile-photo" />
            </template>
            <template v-else>
              <div class="profile-placeholder">
                <span class="camera-icon">📷</span>
              </div>
            </template>
            <input
              type="file"
              ref="fileInput"
              @change="handleFileUpload"
              class="hidden-file-input"
            />
          </div>
        </div>
      </div>

      <!-- Здесь будут рендериться дочерние маршруты, например Project.vue -->
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import CabinetSidebar from '@/components/CabinetSidebar.vue'

const router = useRouter()
const loading = ref(true)
const userInfo = ref({})
const user = ref(null)
const fileInput = ref(null)

const welcomeName = computed(() => userInfo.value.first_name || user.value.email)
const fullPhotoUrl = computed(() =>
  userInfo.value.photo_url
    ? `http://localhost:5000${userInfo.value.photo_url}`
    : null
)

function triggerPhotoUpload() {
  fileInput.value?.click()
}

async function handleFileUpload(e) {
  const file = e.target.files[0]
  if (!file) return

  const formData = new FormData()
  formData.append('file', file)
  await axios.post('/api/user_info/photo', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
    withCredentials: true
  })
  await fetchUserInfo()
}

async function fetchUserInfo() {
  try {
    const { data } = await axios.get('/api/user_info', { withCredentials: true })
    userInfo.value = data
  } catch {
    userInfo.value = {}
  }
}

onMounted(async () => {
  try {
    const resp = await axios.get('/api/cabinet', { withCredentials: true })
    user.value = resp.data
    await fetchUserInfo()
  } catch (err) {
    if (err.response?.status === 401) router.push({ name: 'Login' })
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
@import '@/arch.css';

.panel-layout {
  display: flex;
  min-height: 100vh;
  margin-top: 4%;
  border: 1px solid #e4e4e4;
}

.panel-content {
  flex: 1;
  padding: 2rem;
}

.welcome-photo-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.photo-container {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  padding-bottom: 2rem;
}

.profile-photo-wrapper {
  position: relative;
  width: 90px;
  height: 90px;
  cursor: pointer;
}

.profile-photo {
  width: 96px;
  height: 96px;
  object-fit: cover;
  border-radius: 50%;
  border: 2px solid #000;
}

.profile-placeholder {
  width: 90px;
  height: 90px;
  background: #f0f0f0;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  color: #999;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.hidden-file-input {
  display: none;
}

.welcome-text {
  font-size: 1.8rem;
  color: #000;
  margin: 0;
}

.welcome-photo-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

</style>
