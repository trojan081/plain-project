<!-- frontend/src/components/CabinetSidebar.vue -->
<template>
    <div class="panel-sidebar">
      <!-- Мои данные -->
      <div class="segment">
        <h2 class="segment-title">
            <router-link to="/cabinet" class="unstyled-link">Мои данные</router-link>
          <button class="edit-link" @click="startEdit"> ред. </button>
        </h2>
  
        <ul v-if="!editing">
           <li>
            <span class="userdata">Телефон: </span> 
            <span class="userdata_content">{{ userInfo.phone }}</span>
          </li>
          <li>
            <span class="userdata">ФИО: </span> 
            <span class="userdata_content"> {{ userInfo.last_name }}&ensp;</span> 
            <span class="userdata_content"> {{ userInfo.first_name }}&ensp;</span> 
            <span class="userdata_content"> {{ userInfo.fathers_name }}&ensp; </span>
          </li>
 
          <li>
            <span class="userdata">Должность: </span> 
            <span class="userdata_content">{{ userInfo.position }}</span>
          </li>
        </ul>
  
        <form v-else @submit.prevent="saveInfo" class="edit-form">
          <div class="form-group" v-for="field in fields" :key="field.key">
            <label>
              <span class="userdata">{{ field.label }}:</span>
              <input v-model="form[field.key]" class="data_input_field"/>
            </label>
          </div>
          <div class="buttons">
            <button type="submit" class="save-btn">Сохранить</button>
            <button type="button" @click="startEdit" class="cancel-btn">Отмена</button>
          </div>
        </form>
      </div>
  
      <!-- Мои проекты -->
      <div class="segment">
        <h2 class="segment-title" @click="expanded.projects = !expanded.projects">
            <router-link to="/projects"  class="unstyled-link">Мои проекты</router-link>
          <span class="arrow">{{ expanded.projects ? '▼' : '▶' }}</span>
        </h2>
  
        <ul v-if="expanded.projects">
          <!-- если нет ни одного проекта -->
          <li v-if="projects.length === 0" class="empty_content">Пусто</li>
  
          <!-- иначе по группам -->
          <li
            v-for="(group, label) in groupedProjects"
            :key="label"
            class="group-label"
          >
            <div @click="toggleGroup(label)" class="group-header">
              <span class="arrow">{{ expanded.groups[label] ? '▼' : '▶' }}</span>
              {{ label }}
            </div>
            <ul v-if="expanded.groups[label]">
              <li
                v-for="proj in group"
                :key="proj.id"
                class="userdata_content"
              >
                <router-link :to="`/project/${proj.id}`">• {{ proj.name }}</router-link>
              </li>
            </ul>
          </li>
  
          <!-- иконка + добавить проект -->
          <li class="userdata_content add-project">
            <router-link to="/add_project" class="add_smth">
              <img src="@/assets/plus1.png" class="plus-icon" alt="+">
              <t>добавить проект</t></router-link>
            
          </li>
        </ul>
      </div>
  
      <!-- Мои шаблоны -->
      <div class="segment">
        <h2 class="segment-title">Мои шаблоны</h2>
        <ul>
          <li>Цветовая палитра</li>
          <li>Блоки</li>
          <li>Подписи</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, reactive, onMounted, computed } from 'vue'
  import axios from 'axios'
  
  const userInfo = ref({})
  const editing = ref(false)
  const form = reactive({})
  
  const projects = ref([])
  const statuses = ref([])
  
  const expanded = reactive({
    projects: true,
    groups: {}
  })
  
  const fields = [
    { key: 'first_name', label: 'Имя' },
    { key: 'last_name',  label: 'Фамилия' },
    { key: 'fathers_name', label: 'Отчество' },
    { key: 'phone',      label: 'Телефон' },
    { key: 'position',   label: 'Должность' },
  ]
  

  // переключаем режим редактирования
  function startEdit() {
  if (editing.value) {
    // если уже редактируем — тогда отменяем редактирование
    editing.value = false
  } else {
    // иначе начинаем редактирование
    Object.assign(form, userInfo.value)
    editing.value = true
  }
}

function cancelEdit() {
  editing.value = false
}
  
  function toggleGroup(label) {
    expanded.groups[label] = !expanded.groups[label]
  }
  
  function groupLabel(statusId) {
    const s = (statuses.value.find(x => x.id === statusId)?.status || '').toLowerCase()
    if (s.includes('работ')) return 'В работе'
    if (s.includes('соглас')) return 'На согласовании'
    if (s.includes('заверш')) return 'Завершены'
    return 'Прочие'
  }
  
  const groupedProjects = computed(() => {
    const out = {}
    for (const p of projects.value) {
      const lbl = groupLabel(p.project_status)
      ;(out[lbl] = out[lbl] || []).push(p)
    }
    return out
  })
  
  async function fetchUserInfo() {
    const { data } = await axios.get('api/user_info', { withCredentials: true })
    userInfo.value = data
  }
  
  async function saveInfo() {
    await axios.put('/api/user_info', form, { withCredentials: true })
    await fetchUserInfo()
    editing.value = false
  }
  
  async function fetchProjects() {
    const [st, pr] = await Promise.all([
      axios.get('/project_status',       { withCredentials: true }),
      axios.get('/project?only_my=true', { withCredentials: true })
    ])
    statuses.value = st.data
    projects.value = pr.data
    // сначала все группы раскрыты
    Object.keys(groupedProjects.value).forEach(l => (expanded.groups[l] = true))
  }
  
  
  onMounted(() => {
    fetchUserInfo()
    fetchProjects()
  })
  </script>
  
  <style scoped>
  @import '@/arch.css';
  
  .panel-sidebar {
    width: 240px;
    background: #fff;
    padding: 1rem;
    border: 1px solid #e4e4e4;
  }
  .segment {
    margin-bottom: 1vw;
    padding: 1vw;
    background: #f9f9f9;
    /* border: 1px solid #2f56914d; */
    border-radius: 24px;
    box-shadow: 0 0 10px rgba(37,35,35,0.2);
  }
  .segment-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 1.2vw;
    color: #012b85;
    font-weight: bold;
    cursor: pointer;
  }
  .segment ul {
    list-style: none;
    padding: 0;
    margin-left: 6%;
  }
  .userdata_content {
    color: #4d4d4dd0;
    margin: .3rem 0;
  }

  .empty_content {
    color: #4d4d4dd0;
    margin: 9%;
    font-style: italic;
  }

  .data_input_field {
    padding: 0.3rem;
    border: 1px solid #ccc;
    border-radius: 10px;
    width: 90%;
    font-size: 1rem;
    }

  .userdata {
    color: #012b8585;
    margin-right: .3rem;
  }
  .group-label + .group-label {
    margin-top: .6rem;
  }
  .arrow {
    margin-right: .5rem;
  }
  .add-project {
    margin-top: 0.5rem;
  }
  .plus-icon {
    width: 1rem;
    height: 1.05rem;
    vertical-align: middle;
    margin-right: 0.3rem;
  }
  .edit-link {
    padding: .2rem .5rem;
    background: #f9f9f9;
    border: none;
    box-shadow: 0 0 6px rgba(0,0,0,0.1);
    border-radius: 12px;
    cursor: pointer;
    }
    .edit-link:hover {
      background: #012b8527;
    }
  
  .data_input_field {
    margin-left: .5rem;
    margin-bottom: .6vw;
  }
  .buttons {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
  }
  .save-btn, .cancel-btn {
    padding: .3rem .8rem;
    border-radius: .8rem;
    background: #f9f9f9;
    border: none;
    cursor: pointer;
  }

  .save-btn, .cancel-btn {
    padding: 0.3rem 0.9rem;
    background: #f9f9f9;
    box-shadow: 0 0 10px rgba(37, 35, 35, 0.2);
    border: none;
    color: #000;
    border-radius: 15px;
    font-size: 1rem;
    cursor: pointer;
    }

  .save-btn:hover { background: #012b8527;; }
  .cancel-btn:hover { background: #012b8527;; }

  .add_smth {
    font-size: 1.124vw;
    color: #6792ca;
    /* font-weight: bold; */
  }
    .unstyled-link {
    color: inherit;
    text-decoration: none;
    }

    .add_smth {
      text-decoration: none;
    }

  </style>
  