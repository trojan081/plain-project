<template>
  <div class="demo-block">
    <h2 class="title">Инструкция</h2>
    <ol class="main-text">
      <li>Все штриховки необходимо залить по сетке 50м * 50м. <br/> Для удобства используйте координатную сетку топографической съёмки.</li>
      <li>Все штриховки должны быть залиты с помощью "внутренней точки" и быть ассоциативными.</li>
      <li>Сохраните файл в формате <strong>*.dxf</strong>.</li>
      <li>Перейдите во вкладку DEMO и загрузите файл через форму.</li>
      <li>Нажмите кнопку <strong>СТАРТ</strong> и дождитесь результата.</li>
    </ol>

    <video controls width="480" class="demo-video">
      <source src="../assets/videos/demo_1.0.mp4" type="video/mp4" />
      Ваш браузер не поддерживает видео.
    </video>
  </div>
</template>

<script setup>
// тоже просто статичный компонент
</script>
<style scoped>
.demo-block {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  border: 1px solid #2f56914d;
  padding: 2.1rem;
  border-radius: 36px;
  box-shadow: 0 0 10px rgba(37,35,35,0.2);
}

.demo-video {
  width: 100%;
  height: auto;
  border-radius: 16px;
  box-shadow: 0 0 10px rgba(37,35,35,0.2);
}

.main-text {
  font-size: clamp(0.8rem, 1.2vw, 1.2rem);
  line-height: 1.6;
}
.title {
  font-size: clamp(1.0rem, 1.2vw, 1.2rem);
}
</style>
