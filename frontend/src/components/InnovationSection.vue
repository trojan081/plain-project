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
        <p class="video-caption">Интегрируйте новейшие технологии в процессы благоустройства городской среды</p>
      </div>
      <div class="video-card">
        <video loop autoplay muted playsinline class="innovation-video">
          <source src="../assets/videos/v6.1.mp4" type="video/mp4" />
          Ваш браузер не поддерживает видео.
        </video>
        <p class="video-caption">Выведете скорость и качество разработки проектов на новый уровень</p>
      </div>
      <div class="video-card">
        <video loop autoplay muted playsinline class="innovation-video">
          <source src="../assets/videos/v5.mp4" type="video/mp4" />
          Ваш браузер не поддерживает видео.
        </video>
        <p class="video-caption">Даем возможность бизнесу получить преимущества перед конкурентами</p>
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

.innovation-section {
  padding: 4rem 230px; /* Добавляем 250px padding слева и справа */
  background: url('/assets/bg3.png') no-repeat center/cover;
  border-top: 1px solid #e9e9e9fd;
  border-bottom: 1px solid #e9e9e9fd;
  margin: 40px auto;
  box-shadow: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-top: 6%;
  padding-bottom: 9%;
  
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
  color: var(--secC); /* Используем переменную для согласованности */
}

.innovation-description {
  font-size: 1.25rem;
  color: #555;
  line-height: 1.6;
  max-width: 800px;
  margin: 0 auto;
}

.innovation-video-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.5rem;
  width: 100%; /* Занимает всю доступную ширину внутри родителя */
  max-width: 1600px; /* Или другую желаемую максимальную ширину */
  margin: 0 auto; /* Центрирует сетку видео по горизонтали */
  background-color: rgb(250, 250, 250);
}

.video-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: var(--mainC);
  border-radius:20px;
  box-shadow:
    inset 0 0 15px rgba(55, 84, 170, 0),
    inset 0 0 20px rgba(255, 255, 255, 0),
    7px 7px 15px rgba(55, 84, 170, 0.15),
    -7px -7px 20px rgba(255, 255, 255, 1),
    inset 0px 0px 4px rgba(255, 255, 255, 0.2);
  overflow: hidden; /* Важно для скругления углов видео */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  padding-bottom: 1.5rem; /* Увеличил отступ снизу для подписи */
  /* border: 1px solid; */
}

.video-card:hover {
  transform: translateY(-5px);
  /* Эффект нажатия (inverse neumorphism) или более выраженный эффект */
  box-shadow:
    inset 0 0 15px rgba(55, 84, 170, 0),
    inset 0 0 20px rgba(255, 255, 255, 0),
    7px 7px 15px rgba(171, 157, 196, 0.342),
    -7px -7px 20px rgba(255, 255, 255, 1),
    inset 0px 0px 4px rgba(255, 255, 255, 0.2);
  /* border: 0.5px solid #3f3f3f2d; */
}

.innovation-video {
  width: 100%;
  height: 220px;
  object-fit: cover;
  border-radius: 20px 20px 0 0; /* Скругляем только верхние углы, как в примере */
  /* Убираем нижнюю границу, если она не нужна с новым дизайном */
  border-bottom: none;
}

.video-caption {
  font-size: 1.1rem;
  color: #333;
  margin-top: 1.5rem; /* Увеличил отступ сверху для подписи */
  padding: 0 1rem;
  font-weight: 500;
}

/* Медиа-запросы для адаптивности */
@media (max-width: 768px) {
  .innovation-section {
    padding: 2.5rem 1rem;
  }

  .innovation-title {
    font-size: 2.5rem;
  }

  .innovation-description {
    font-size: 1rem;
  }

  .innovation-video-grid {
    grid-template-columns: 1fr;
  }

  .innovation-video {
    height: 180px;
  }
}

/* Стили из примера, которые не используются напрямую, но могут быть полезны */

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