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
}

.page-content {
  flex: 1;
}
</style>
