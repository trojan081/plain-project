<template>
  <CabinetHeader />
  <div class="panel-layout">
    <CabinetSidebar />
    <div class="panel-content">
      <div class="projects-page">
        <!-- Фильтры -->
        <div class="filters">
          <div class="dropdown-wrapper">
            <select v-model="filters.status_id" @change="fetchProjects" class="custom-select">
              <option :value="null">Все статусы</option>
              <option v-for="status in projectStatuses" :key="status.id" :value="status.id">
                {{ status.status }}
              </option>
            </select>
          </div>
          <div class="filter-buttons">
            <button
              :class="['filter-btn', { active: filters.only_my }]"
              @click="setFilter(true)"
            >
              Мои проекты
            </button>
            <button
              :class="['filter-btn', { active: !filters.only_my }]"
              @click="setFilter(false)"
            >
              Проекты организации
            </button>
          </div>
        </div>

        <!-- Список проектов -->
        <div v-if="loading">Загрузка...</div>
        <div v-else-if="projects.length === 0">Нет проектов</div>
        <div v-else class="projects-list">
          <div
            v-for="project in projects"
            :key="project.id"
            class="project-card"
          >
            <!-- Вся карточка -->
            <div class="card-container">
              <!-- Название вверху -->
              <div class="project-name">{{ project.name }}
              <router-link
                  class="open-btn"
                  :to="`/project/${project.id}`"
                  v-if="project.id"
                >
                  Открыть
                </router-link>
              </div>
              <!-- Заголовок с кнопкой и стрелкой -->
              <div class="project-header" @click="toggleExpand(project.id)">
                <p><strong>Статус:</strong> {{ getStatusName(project.project_status) }}</p>
                <span class="arrow">{{ expandedProjects.includes(project.id) ? '▼' : '▶' }}</span>
              </div>
              <!-- Детали -->
              <transition name="expand">
                <div
                  v-if="expandedProjects.includes(project.id)"
                  class="project-details"
                >
                  <p><strong>Локация: </strong> {{ project.location || '—' }}</p>
                  <p><strong>Создан: </strong> {{ formatDate(project.created_at) }}</p>
                  <p><strong>Площадь: </strong> {{ project.area || '—' }}</p>
                  <p><strong>Описание: </strong> {{ project.custom_status || '—' }}</p>
                  <div v-if="project.cad_drafter_name" class="drafter">
                    <p><strong>Проектировщик:</strong> <br> {{ project.cad_drafter_name }}</p>
                    <img
                      v-if="project.cad_drafter_avatar"
                      :src="project.cad_drafter_avatar"
                      alt="Photo"
                      class="avatar"
                    />
                  </div>
                </div>
              </transition>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import CabinetSidebar from '@/components/CabinetSidebar.vue'
import CabinetHeader from '@/components/CabinetHeader.vue'

const projects = ref([])
const projectStatuses = ref([])
const loading = ref(true)
const filters = ref({
  status_id: null,
  only_my: true
})

const expandedProjects = ref([])

function toggleExpand(projectId) {
  if (expandedProjects.value.includes(projectId)) {
    expandedProjects.value = expandedProjects.value.filter(id => id !== projectId)
  } else {
    expandedProjects.value.push(projectId)
  }
}

function setFilter(isMy) {
  filters.value.only_my = isMy
  fetchProjects()
}

function getStatusName(id) {
  const status = projectStatuses.value.find(s => s.id === id)
  return status?.status || '—'
}

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleDateString()
}

async function fetchStatuses() {
  try {
    const { data } = await axios.get('/api/project_status/', { withCredentials: true })
    if (Array.isArray(data)) {
      projectStatuses.value = data
    } else {
      console.error('Ожидался массив, но пришло:', data)
    }
  } catch (err) {
    console.error('Ошибка при получении статусов', err)
  }
}

async function fetchProjects() {
  loading.value = true
  const params = {}

  if (filters.value.status_id !== null) params.status_id = filters.value.status_id
  if (filters.value.only_my) params.only_my = true

  try {
    const { data } = await axios.get('/api/project/', {
      params,
      withCredentials: true
    })
    projects.value = data
  } catch (err) {
    console.error('Ошибка загрузки проектов', err)
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  await fetchStatuses()
  await fetchProjects()
})
</script>

<style scoped>

.projects-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  align-items: flex-start;
}

.project-card {
  border: 1px solid #ccc;
  border-radius: 16px;
  background: #ffffff;
  box-shadow: 0 0 10px rgba(37, 35, 35, 0.2);
  transition: box-shadow 0.3s;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.project-card:hover {
  box-shadow: 0 0 12px rgba(1, 43, 133, 0.3);
}

.card-container {
  display: flex;
  flex-direction: column;
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  padding: 0 1rem;
  /* background: #f4f4f4; */
  flex-shrink: 0;
}

.project-name {
  background: #f4f4f4;
  padding: 1rem;
  font-weight: bold;
  font-size: 1.08rem;
  border-top-left-radius: 16px;
  border-top-right-radius: 16px;
}

.project-details {
  padding: 1rem;
  border-top: 1px solid #ddd;
  flex-grow: 1; 
  max-height: 200px; 
  overflow-y: auto; 
}

.drafter {
  display: flex;
  align-items: center;
  margin-top: 1rem;
  padding-right: 1%;
}
.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  margin-right: 0.5rem;
  margin-left: 1.5rem;
}

.open-btn {
  align-self: flex-start;
  margin: 0.5rem 1rem 0 1rem;
  padding: 0.2rem 0.5rem;
  font-size: 0.8rem;
  height: auto;
  border: solid 1px #ccc;
  background-color: #ffffff;
  color: #000000;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.2s;
  text-decoration: none;
}
.open-btn:hover {
  background-color: rgba(55, 96, 185, 0.3);
}
.expand-enter-active,
.expand-leave-active {
  transition: all 0.3s ease;
  max-height: 200px; 
}

.arrow {
  margin-left: 0.5rem;
  font-size: 1.2rem;
}

.expand-enter-from,
.expand-leave-to {
  max-height: 0;
  opacity: 0;
  padding: 0 1rem;
}

.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.filter-buttons {
  display: flex;
  gap: 0.5rem;
}

.filter-btn {
  padding: 0.5rem 1rem;
  border-radius: 12px;
  border: 1px solid #ccc;
  background: #f4f4f4;
  cursor: pointer;
  transition: 0.2s;
}

.filter-btn.active {
  background: #012b85;
  color: #fff;
  font-weight: bold;
  border-color: #012b85;
}

.filter-btn:hover {
  background: #dce4f6;
}

.dropdown-wrapper {
  position: relative;
  display: inline-block;
}

.custom-select {
  appearance: none;
  background: #f4f4f4;
  border: 1px solid #ccc;
  border-radius: 12px;
  padding: 0.5rem 2.5rem 0.5rem 1rem;
  font-size: 0.95rem;
  cursor: pointer;
  color: #000;
  font-weight: 500;
}

.dropdown-wrapper::after {
  content: '▼';
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #666;
  pointer-events: none;
}

.custom-select:focus {
  border-color: #012b85;
  outline: none;
  box-shadow: 0 0 0 2px rgba(1, 43, 133, 0.2);
}

.view-link {
  display: inline-block;
  margin-top: 1rem;
  color: #012b85;
  font-weight: bold;
  text-decoration: underline;
  cursor: pointer;
}
</style>