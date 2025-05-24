<template>
  <div class="demo-block">
    <h2>Описание программы</h2>
    <p>
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
  font-size: 1.2vw;
  color: #012b85;
  font-weight: bold;
}
</style>

