<template>
    <div class="user-profile">
      <CabinetHeader />
      <div class="panel-layout">
        <CabinetSidebar />
  
        <div class="panel-content">
          <div v-if="loading">Загрузка...</div>
          <div v-else-if="!userData">Пользователь не найден</div>
          <div v-else class="user-info">
            <div class="user-header">
              <img v-if="userData.photo_url" :src="userData.photo_url" alt="avatar" class="avatar" />
              <div>
                <h2>{{ fullName }}</h2>
                <p v-if="userData.position"><strong>Должность:</strong> {{ userData.position }}</p>
                <p v-if="userData.phone"><strong>Телефон:</strong> {{ userData.phone }}</p>
                <p v-if="userData.email"><strong>Email:</strong> {{ userData.email }}</p>
              </div>
            </div>
  
            <div class="user-projects">
              <h3>Проекты пользователя</h3>
              <ul>
                <li v-for="project in userProjects" :key="project.id">
                  {{ project.name }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  import CabinetHeader from '@/components/CabinetHeader.vue'
  import CabinetSidebar from '@/components/CabinetSidebar.vue'
  
  const route = useRoute()
  const loading = ref(true)
  const userData = ref(null)
  const userProjects = ref([])
  
  const fullName = computed(() => {
    if (!userData.value) return ''
    const { last_name, first_name, fathers_name } = userData.value
    return [last_name, first_name, fathers_name].filter(Boolean).join(' ')
  })
  
  onMounted(async () => {
    const slug = route.params.slug
    try {
      const { data } = await axios.get(`/api/user/${slug}`, { withCredentials: true })
      userData.value = data
      userProjects.value = data.projects
    } catch (err) {
      console.error('Ошибка загрузки профиля', err)
    } finally {
      loading.value = false
    }
  })
  </script>
  
  <style scoped>
  .user-header {
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  .avatar {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    object-fit: cover;
  }
  </style>
  