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
  menu: Array,
});
</script>

<style scoped>
@import '@/arch.css';

/* Define your CSS variables if not already in arch.css or a global file */
:root {
  --primary-red: #d61010;
  --primary-red-hover: #d610101f;
  --text-color-dark: #111;
  --text-color-light: #FFFFFF;
  --background-light: #F8F8F8;
  --background-medium: #f6f6f6;
  --border-light: #EEEEEE;
  --border-gray: #ccc;
  --placeholder-color: #999; /* Adjusted for better visibility */
  --shadow-extra-light: rgba(0, 0, 0, 0.02);
  --shadow-light: rgba(0, 0, 0, 0.05);
  --shadow-medium: rgba(0, 0, 0, 0.1);

  /* New variables for font clamping values */
  --font-size-base: 1rem; /* Base font size */
  --font-size-sm: 0.8rem;  /* Smaller font size */
  --font-size-lg: 1.2rem; /* Larger font size */
}

.panel-sidebar {
  width: 240px;
  background: #fff;
  padding: 1rem;
  border: 1px solid #e4e4e4;
  display: flex; /* Added for better layout control */
  flex-direction: column; /* Added for better layout control */
  gap: 0.5rem; /* Spacing between segments */
}

.segment {
  /* margin-bottom: 1vw; */ /* Replaced by gap on .panel-sidebar */
  background: #f9f9f9;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  border: 1px solid #b4b4b4be;
  font-size: var(--font-size-base); /* Changed to variable, but clamp will override */
  box-shadow: 0 0 10px rgba(37, 35, 35, 0.2);
  cursor: pointer;
  transition: transform 0.3s ease, background 0.3s ease, box-shadow 0.3s ease; /* Added background and box-shadow to transition */
}

.segment:hover {
  transform: translateX(10px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  background: var(--background-medium); /* Add a subtle hover background */
}

.segment.active {
  background: #3f3c3c1f; /* Your original active background */
  box-shadow: 0 2px 8px rgba(0,0,0,0.1); /* Adjusted shadow for active */
}

.segment-title {
  font-size: clamp(0.8rem, 1.5vw, 1.1rem);
  color: #000000;
  font-weight: bold;
  text-align: left; /* Ensure text is left-aligned within the segment */
}

/* Remove media queries for font-size as clamp handles it */
/* @media (max-width: 768px) {
  .segment-title {
    font-size: 2.4vw;
  }
}
@media (min-width: 1440px) {
  .segment-title {
    font-size: 0.66vw;
  }
} */
</style>