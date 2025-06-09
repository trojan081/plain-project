<template>
  <section class="innovation-section">
    <div class="innovation-content">
      <h2 class="innovation-title">Модернизируй <span class="highlight-text">бизнес-процессы</span></h2>
    </div>
    <div class="innovation-video-grid">
      <div class="video-card">
        <video loop autoplay muted playsinline class="innovation-video">
          <source src="../assets/videos/v6.2.mp4" type="video/mp4" />
          Ваш браузер не поддерживает видео.
        </video>
        <p class="video-caption">Интегрируй новейшие технологии в процессы благоустройства городской среды</p>
      </div>
      <div class="video-card">
        <video loop autoplay muted playsinline class="innovation-video">
          <source src="../assets/videos/v6.1.mp4" type="video/mp4" />
          Ваш браузер не поддерживает видео.
        </video>
        <p class="video-caption">Выводи скорость и качество разработки проектов на новый уровень</p>
      </div>
      <div class="video-card">
        <video loop autoplay muted playsinline class="innovation-video">
          <source src="../assets/videos/v5.mp4" type="video/mp4" />
          Ваш браузер не поддерживает видео.
        </video>
        <p class="video-caption">Получай преимущества перед конкурентами </p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue';

onMounted(() => {
  const videos = document.querySelectorAll('.innovation-video');
  videos.forEach(video => {
    video.addEventListener('loadedmetadata', () => {
      video.play().catch(error => {
        console.warn("Автовоспроизведение видео заблокировано:", error);
        video.muted = true;
        video.play();
      });
    });
  });
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Muli:300,400,700,900');

:root {
  --mainC: #f1f3f6; /* Светлый фон для нейморфизма */
  --secC: #007bff; /* Акцентный цвет, как в вашем highlight-text */
  --shadowLight: rgba(255, 255, 255, 1);
  --shadowDark: rgba(55, 84, 170, 0.15);
  --shadowInsetLight: rgba(255, 255, 255, 0.2);
  --shadowInsetDark: rgba(55, 84, 170, 0); /* Устанавливаем 0 для отсутствия изначального inset-shadow */
}

/* Общие стили для секции */
.innovation-section {
  padding: 4rem 230px;
  background: url('/assets/bg3.png') no-repeat center/cover;
  border-top: 1px solid #e9e9e9fd;
  border-bottom: 1px solid #e9e9e9fd;
  margin: 40px auto;
  box-shadow: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-top: 9%;
  padding-bottom: 15%;
}

.innovation-content {
  margin-bottom: 3rem;
  width: 100%;
  max-width: 1600px;
}

.innovation-title {
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  font-size: clamp(0.8rem, 4vw + 0.5rem, 2.8rem);
  font-weight: 600;
  color: #333;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.highlight-text {
  color: var(--secC);
}

.innovation-description {
  font-size: 1.25rem;
  color: #555;
  line-height: 1.6;
  max-width: 800px;
  margin: 0 auto;
}

/* Стили для сетки видео */
.innovation-video-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.5rem;
  width: 100%;
  max-width: 1600px;
  margin: 0 auto;
  background-color: rgb(250, 250, 250);
}

.video-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: var(--mainC);
  border-radius: 20px;
  box-shadow:
    inset 0 0 15px rgba(55, 84, 170, 0),
    inset 0 0 20px rgba(255, 255, 255, 0),
    7px 7px 15px rgba(55, 84, 170, 0.15),
    -7px -7px 20px rgba(255, 255, 255, 1),
    inset 0px 0px 4px rgba(255, 255, 255, 0.2);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  padding-bottom: 1.5rem;
}

.video-card:hover {
  transform: translateY(-5px);
  box-shadow:
    inset 0 0 15px rgba(55, 84, 170, 0),
    inset 0 0 20px rgba(255, 255, 255, 0),
    7px 7px 15px rgba(171, 157, 196, 0.342),
    -7px -7px 20px rgba(255, 255, 255, 1),
    inset 0px 0px 4px rgba(255, 255, 255, 0.2);
}

.innovation-video {
  width: 100%;
  height: 220px;
  object-fit: cover;
  border-radius: 20px 20px 0 0;
  border-bottom: none;
}

.video-caption {
  font-size: 1.1rem;
  color: #333;
  margin-top: 1.5rem;
  padding: 0 1rem;
  font-weight: 500;
}

/* Медиа-запросы для адаптивности */
@media (max-width: 1024px) { /* Добавляем точку останова для планшетов */
  .innovation-section {
    padding: 3rem 50px; /* Уменьшаем горизонтальный padding */
    padding-top: 5%;
    padding-bottom: 10%;
  }

  .innovation-video-grid {
    gap: 2rem; /* Немного уменьшаем расстояние между видео */
  }

  .innovation-video {
    height: 200px; /* Немного уменьшаем высоту видео */
  }

  .video-caption {
    font-size: 1rem; /* Чуть уменьшаем шрифт подписей */
  }
}

@media (max-width: 768px) { /* Существующие стили для мобильных устройств */
  .innovation-section {
    padding: 2.5rem 1rem; /* Уменьшаем padding еще больше */
    margin: 20px auto; /* Уменьшаем внешний отступ */
    padding-top: 7%; /* Адаптируем верхний отступ */
    padding-bottom: 12%; /* Адаптируем нижний отступ */
  }

  .innovation-title {
    font-size: clamp(1.5rem, 8vw, 2.5rem); /* Увеличиваем базовый размер шрифта для мобильных, сохраняя адаптивность */
    margin-bottom: 1.5rem; /* Немного увеличиваем отступ заголовка */
  }

  .innovation-description {
    font-size: 0.95rem; /* Чуть уменьшаем шрифт описания */
  }

  .innovation-video-grid {
    grid-template-columns: 1fr; /* Видео располагаются в один столбец */
    gap: 1.5rem; /* Уменьшаем отступ между видео */
  }

  .innovation-video {
    height: 200px; /* Увеличиваем высоту видео для лучшего просмотра на мобильных */
  }

  .video-caption {
    font-size: 0.95rem; /* Чуть уменьшаем шрифт подписей для мобильных */
  }

  .video-card {
    padding-bottom: 1rem; /* Уменьшаем отступ снизу для подписи */
  }
}

@media (max-width: 480px) { /* Дополнительная точка останова для очень маленьких экранов */
  .innovation-section {
    padding: 2rem 0.5rem; 
    margin: 15px auto;
    padding-top: 8%;
    padding-bottom: 14%;
  }

  .innovation-title {
    font-size: clamp(0.8rem, 4vw + 0.5rem, 2.8rem);  
  }

  .innovation-video {
    height: 180px; 
  }
}


html, body {
  background: var(--mainC);
  font-family: 'Muli', sans-serif;
  color: rgba(51, 51, 51, 1);
}

.text h1 {
  font-size: 1.5em;
  font-weight: 600;
}
.text p {
  margin-top: 2em;
  line-height: 1.45em;
}
</style>