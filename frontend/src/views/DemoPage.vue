<template>
<Header/>
            <div 
              class="header" 
              :style="{ filter: `blur(${blurValue}px)` }"
            >
            </div>
            
          <div class="triple-wrapper"></div>
            <div v-if="loading">Загрузка...</div>
            <div v-else class="panel-layout">
              <DemoSidebar :menu="menu" :current="tab" @select="tab = $event" />
            <div class="panel-content">

          <div class="mt-8">
        <component :is="currentTabComponent" />
      </div>
    </div>
  </div>
  
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import DemoSidebar from '@/components/DemoSidebar.vue'
import DemoBlock from '@/components/DemoBlock.vue'
import DescriptionBlock from '@/components/DescriptionBlock.vue'
import InstructionBlock from '@/components/InstructionBlock.vue'
import DemoHeader from '@/components/DemoHeader.vue'
import RoadmapSection from '@/components/RoadmapSection.vue'
import Header from '@/components/Header.vue'


const router = useRouter()
const loading = ref(true)
const userInfo = ref({})
const user = ref(null)
const fileInput = ref(null)

const tab = ref('demo')
const menu = [
  { key: 'demo', title: 'DEMO' },
  { key: 'desc', title: 'Описание' },
  { key: 'guide', title: 'Инструкция' },
]


async function handleFileUpload(e) {
  const file = e.target.files[0]
  if (!file) return

  const formData = new FormData()
  formData.append('file', file)
  await axios.post('/user_info/photo', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
    withCredentials: true
  })
  await fetchUserInfo()
}

async function fetchUserInfo() {
  try {
    const { data } = await axios.get('/user_info', { withCredentials: true })
    userInfo.value = data
  } catch {
    userInfo.value = {}
  }
}

onMounted(async () => {
  try {
    const resp = await axios.get('/cabinet', { withCredentials: true })
    user.value = resp.data
    await fetchUserInfo()
  } catch (err) {
    if (err.response?.status === 401) router.push({ name: 'Login' })
  } finally {
    loading.value = false
  }
})

const currentTabComponent = computed(() => {
  switch (tab.value) {
    case 'desc': return DescriptionBlock
    case 'guide': return InstructionBlock
    default: return DemoBlock
  }
})
</script>

<style scoped>

.panel-layout {
  display: flex;
  min-height: 100vh;
  margin-top: 4%;
  border: 1px solid #e4e4e4;
}

.panel-content {
  flex: 1;
  padding: 72px 36px 0 36px;
  max-width: 900px;
  margin: 0 auto;
}
</style>