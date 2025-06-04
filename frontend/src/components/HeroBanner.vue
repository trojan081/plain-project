<template>
  <section class="hero-banner">
    <div class="hero-content">
      <h1>
        Моментальные <span class="highlight">чертежи</span>
        и экономия
        в <span class="highlight purple">десятки</span> раз
      </h1>
      <p>
        Plain сделает Вашу разработку проектной документации быстрой,<br />
        легкой и эффективной. Воспользуйтесь нашим сервисом уже сегодня.<br />
        Поддержка стандартов ПП РФ № 87 и № 1013.<br />
      </p>
      <div class="buttons">
        <button class="primary">Начать сейчас</button>
        <button class="secondary">Подробнее</button>
      </div>
    </div>
    <div class="hero-image">
        <Lines1 />
      <!-- <img src='/assets/h4.png' alt="Illustration" /> -->
    </div>
  </section>
</template>

<script setup>
import Cube1 from '@/components/Cube1.vue';
import Cube2 from '@/components/Cube2.vue';
import Lines1 from './Lines1.vue';

// Importing the Cube1 component for the hero image
</script>   


<style scoped>
.hero-banner {
  display: flex;
  justify-content: center; 
  padding: 4rem 2rem;
  max-width: 1600px; 
  margin: 10% 12%; 
  gap: 2rem;
}

.hero-content {
  flex: 1 1 700px;
  max-width: 1600px;
}

.hero-content h1 {
  font-size: clamp(0.8rem, 4vw + 0.5rem, 2.8rem);
  font-weight: 800;
  color: #111;
  line-height: 1.2;
  margin-bottom: 1.2rem;
}


.highlight {
  color: #111;
}

.highlight.purple {
  color: #d61010;
}

.hero-content p {
  font-size: clamp(0.9rem, 1.3vw + 0.3rem, 1.1rem);
  color: #444;
  margin-bottom: 2rem;
}

.buttons {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.primary {
  background-color: #ffffff;
  color: rgb(0, 0, 0);
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: 0.3s;
  border: 1px solid #d6101079;
}

.primary:hover {
  background-color: #d610101f;
}

.secondary {
  background-color: white;
  color: #111;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-weight: 600;
  cursor: pointer;
  transition: 0.3s;
}

.secondary:hover {
  background-color: #f6f6f6;
}

.hero-image {
  flex: 1 1 400px;
  text-align: center;
}

.hero-image img {
  max-width: 100%;
  height: auto;
}
</style>
