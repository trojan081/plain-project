<template>
  <div class="container">
    <DemoSidebar :menu="menu" :current="tab" @select="tab = $event" />
    <div class="content">
      <div v-if="loading" class="loading">Загрузка...</div>
      <component :is="currentTabComponent" />
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

const router = useRouter()
const loading = ref(true)
const userInfo = ref({})
const user = ref(null)
const tab = ref('demo')
const menu = [
  { key: 'demo', title: 'Demo' },
  { key: 'desc', title: 'Описание' },
  { key: 'guide', title: 'Инструкция' },
]

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
.container {
  display: flex;
  min-height: 100vh;
  background-color: #fff;
  font-family: 'Arial', sans-serif;
}

.content {
  flex: 1;
  padding: 2rem;
  max-width: 800px;
  margin: 4% auto;
  text-align: left;
}

.loading {
  text-align: center;
  font-size: 1.5rem;
  color: #E53935;
}
</style>