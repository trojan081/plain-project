<template>
  <div class="app-wrapper">
    <CabinetHeader v-if="isCabinetRoute" />
    <!-- <DemoHeader v-else-if="isDemoPageRoute" /> -->
    <Header v-else />
    <router-view />
    <Footer />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import CabinetHeader from './components/CabinetHeader.vue'
import DemoHeader from './components/DemoHeader.vue'
import CabinetSidebar from './components/CabinetSidebar.vue'

const route = useRoute()

const isCabinetRoute = computed(() => {
  return route.path.startsWith('/cabinet')
})

const isDemoPageRoute = computed(() => {
  return route.path.startsWith('/demo')
})
</script>

<style scoped>
.app-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  max-width: 1800px;
  justify-content: center;
  margin: 0 auto;
  border: 1px solid #e0e0e0;
  border-radius: 30px;
  overflow: hidden;
  background-color: #ffffff;
}

.page-content {
  flex: 1;
}

/* ====== Мобильная адаптация ====== */
@media (max-width: 768px) {
  .logo img {
    padding-left: 0.1rem;
    transform: scale(0.85);
    scale: 1.8;
  }
}

/* ====== Широкие экраны (например 1440px+) ====== */
@media (min-width: 1440px) {
  .logo img {
    padding-left: 1.2rem;
    transform: scale(1.15);
    scale: 0.8;
  }
}
</style>
