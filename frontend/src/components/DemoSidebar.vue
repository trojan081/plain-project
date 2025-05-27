<template>
  <div class="panel-sidebar">
    <div
      v-for="item in menu"
      :key="item.key"
      class="segment"
      @click="$emit('select', item.key)"
      :class="{ active: current === item.key }"
    >
      <h2 class="segment-title">
        {{ item.title }}
      </h2>
    </div>
  </div>
</template>

<script setup>
defineProps({
  current: String,
  menu: Array
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
  background: #f9f9f9;
  padding: 0.3rem 0.8rem;
  border-radius: 16px;
  border: 1px solid #2f56914d;
  font-size: 0.95rem;
  box-shadow: 0 0 10px rgba(37,35,35,0.2);
  cursor: pointer;
  transition: background 0.2s;
}

.segment:hover {
  background:#2f56911a;   
}

.segment.active {
  background: #012b8515;
}

.segment-title {
  font-size: 1.2vw;
  color: #012b85;
  font-weight: bold;
}

/* ====== Мобильная адаптация ====== */
@media (max-width: 768px) {
  .segment-title {
  font-size: 2.4vw;
}
}

/* ====== Широкие экраны (например 1440px+) ====== */
@media (min-width: 1440px) {
  .segment-title {
  font-size: 0.66vw;
  }
}
</style>
