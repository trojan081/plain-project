<template>
  <div class="demo-block">
    <h2 class="title">Описание программы</h2>
    <p class="main-text">
      Данная демо-страница позволяет получить моментальный расчёт объёмов работ - площадей покрытий и длин линейных объектов.
      Это пример демонстрации базового функционала продукта.
      <br /><br />
      Загрузка поддерживает только файлы формата <strong>*.dxf</strong>. <br />
      Все загруженные файлы удаляются сразу после обработки.
    </p>
  </div>
</template>

<script setup>
// простой статичный блок, без логики
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

.p {
  font-size: clamp(0.9rem, 1.2vw, 1.2rem);
  line-height: 1.6;
  color: #012b85;
  font-weight: bold;
}

.main-text {
  font-size: clamp(0.7rem, 1.2vw, 1.2rem);
  line-height: 1.6;
}
.title {
  font-size: clamp(1.0rem, 1.2vw, 1.2rem);
}
</style>

