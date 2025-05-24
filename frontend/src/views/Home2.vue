<template>
  <section class="hero">
    <div class="hero-content">
      <h1 class="hero-title">Автоматизация проектирования</h1>
      <p class="hero-subtitle">
        Plain помогает рассчитывать объёмы работ <br /> и ускоряет выполнение проектов в разы.
      </p>
      <router-link to="/demo" class="cta-button">Попробовать бесплатно</router-link>
    </div>
    <div class="hero-media">
      <video autoplay muted loop playsinline>
        <source src="./assets/videos/v1_.mp4" type="video/mp4"/>
        Ваш браузер не поддерживает видео.
      </video>
    </div>
  </section>

  <section class="features">
    <div class="feature">
      <h2>Скорость</h2>
      <p>Проектируйте быстрее — расчёты занимают секунды, а не недели.</p>
    </div>
    <div class="feature">
      <h2>Надёжность</h2>
      <p>Исключите человеческий фактор — доверяйте алгоритмам.</p>
    </div>
    <div class="feature">
      <h2>Экономия</h2>
      <p>Сократите затраты на рутину и фокусируйтесь на важном.</p>
    </div>
  </section>

  <section class="how-to-start">
    <h2>Как начать?</h2>
    <p>
      Просто загрузите файл проекта и получите автоматический расчёт объёмов работ. Это бесплатно.
    </p>
    <router-link to="/demo" class="start-button">Загрузить проект</router-link>
  </section>
</template>

<style scoped>
/* Общие */
* {
  box-sizing: border-box;
}
section {
  padding: 4rem 2rem;
}

/* Hero блок */
.hero {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  background: linear-gradient(135deg, #4a0185, #0099ff);
  color: white;
  padding: 4rem 2rem;
  border-radius: 24px;
  margin: 2rem auto;
  max-width: 1200px;
  gap: 2rem;
}

.hero-content {
  flex: 1;
  min-width: 280px;
}
.hero-title {
  font-size: 2.8rem;
  font-weight: 700;
  margin-bottom: 1rem;
}
.hero-subtitle {
  font-size: 1.2rem;
  line-height: 1.6;
  margin-bottom: 2rem;
}
.cta-button {
  background: white;
  color: #012b85;
  padding: 0.8rem 1.6rem;
  border-radius: 8px;
  font-weight: bold;
  text-decoration: none;
  transition: all 0.2s ease;
}
.cta-button:hover {
  background: #e4e4e4;
}

/* Видео */
.hero-media {
  flex: 1;
  min-width: 280px;
}
.hero-media video {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

/* Блок с фичами */
.features {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  gap: 2rem;
  background: #f5f7fa;
  border-radius: 20px;
  max-width: 1100px;
  margin: auto;
  padding: 3rem 1rem;
}
.feature {
  flex: 1;
  min-width: 280px;
  text-align: center;
}
.feature h2 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: #012b85;
}
.feature p {
  font-size: 1rem;
  color: #555;
}

/* Как начать */
.how-to-start {
  text-align: center;
  max-width: 800px;
  margin: 4rem auto;
}
.how-to-start h2 {
  font-size: 2rem;
  color: #012b85;
  margin-bottom: 1rem;
}
.how-to-start p {
  font-size: 1.1rem;
  color: #444;
  margin-bottom: 2rem;
}
.start-button {
  background: #012b85;
  color: white;
  padding: 0.9rem 1.6rem;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: bold;
  text-decoration: none;
  transition: all 0.3s ease;
}
.start-button:hover {
  background: #0146d9;
}
</style>
