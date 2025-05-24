<template>
  <CabinetHeader />
  <div class="panel-layout">
    <CabinetSidebar />
    <div class="panel-content">
      <div class="segment centered-form">
        <h2 class="segment-title">Новый проект</h2>

        <form @submit.prevent="createProject" class="project-form">
          <div class="form-row" v-for="field in fields" :key="field.key">
            <label class="field-label">{{ field.label }}</label>

            <template v-if="field.key === 'project_status'">
              <select v-model="form.project_status" class="input-field" disabled>
                <option
                  v-for="status in projectStatuses"
                  :key="status.id"
                  :value="status.id"
                >
                  {{ status.status }}
                </option>
              </select>
            </template>

            <template v-else>
              <input
                v-model="form[field.key]"
                :required="field.required"
                class="input-field"
              />
            </template>
          </div>

          <div class="buttons">
            <button type="submit" class="save-btn">Сохранить</button>
            <button type="button" @click="cancel" class="cancel-btn">Отмена</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import CabinetSidebar from '@/components/CabinetSidebar.vue'
import CabinetHeader from '@/components/CabinetHeader.vue'

const router = useRouter()

const form = ref({
  name: '',
  project_status: '',
  location: '',
  area: '',
  regulation_document: '',
  custom_status: '',
  org_id: null,
  project_manager: null
})

const fields = [
  { key: 'name', label: 'Название проекта', type: 'text', required: true },
  { key: 'project_status', label: 'Статус проекта', type: 'select', required: true },
  { key: 'location', label: 'Локация', type: 'text' },
  { key: 'area', label: 'Площадь', type: 'text' },
  { key: 'regulation_document', label: 'Перечень ПП', type: 'text' },
  { key: 'custom_status', label: 'Описание', type: 'text' },
]

const projectStatuses = ref([])

async function fetchStatuses() {
  try {
    const { data } = await axios.get('/api/project_status/', { withCredentials: true })
    projectStatuses.value = Array.isArray(data) ? data : []

    // Устанавливаем статус "Создан" по умолчанию
    const createdStatus = projectStatuses.value.find(
      s => s.status?.toLowerCase() === 'создан'
    )
    if (createdStatus) {
      form.value.project_status = createdStatus.id
    }
  } catch (err) {
    console.error('Ошибка при загрузке статусов', err)
  }
}

async function createProject() {
  try {
    const { data } = await axios.post('/api/project/', form.value, { withCredentials: true })
    router.push(`/project/${data.id}`)
  } catch (err) {
    console.error('Ошибка создания проекта', err)
  }
}

function cancel() {
  router.push('/projects')
}

onMounted(() => {
  fetchStatuses()
})
</script>

<style scoped>
.segment {
  padding: 1.5rem;
  background: #f9f9f9;
  border-radius: 24px;
  box-shadow: 0 0 10px rgba(37, 35, 35, 0.2);
  margin-bottom: 2rem;
  width: 42%;
}

.centered-form {
  margin: 0 auto;
}

.segment-title {
  font-size: 1.2rem;
  margin-bottom: 2.1rem;
  color: #000000;
  font-weight: bold;
  text-align: center;
}

.project-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-row {
  display: grid;
  grid-template-columns: 40% 1fr;
  align-items: center;
  gap: 1rem;
}

.field-label {
  color: #000000;
  font-weight: 500;
  white-space: nowrap;
  text-align: left;
}

.input-field {
  padding: 0.6rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  width: 100%;
  display: block;
  box-sizing: border-box;
}

.buttons {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
  justify-content: center;
}

.save-btn,
.cancel-btn {
  padding: 0.4rem 1.2rem;
  border-radius: 14px;
  background: #f9f9f9;
  border: none;
  cursor: pointer;
  box-shadow: 0 0 10px rgba(37, 35, 35, 0.2);
  font-weight: bold;
}

.save-btn:hover,
.cancel-btn:hover {
  background: #012b8527;
}
</style>
