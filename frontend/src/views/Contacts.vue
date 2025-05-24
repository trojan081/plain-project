<template>
    <div class="panel-layout">
      <div class="panel-sidebar">
        <h2>Контакты</h2>
      </div>
      <div class="panel-content">
        <h1>Контактная информация</h1>
        <p>
          Здесь вы можете указать адрес, телефон, e-mail и другие контактные данные.
        </p>
      </div>
    </div>
  </template>
  
  <script setup>
    // Можно добавить дополнительные данные или методы для обработки форм обратной связи
  </script>
  
  <style scoped>
  .panel-layout {
    display: flex;
    min-height: 100vh;
  }
  
  .panel-sidebar {
    width: 240px;
    background-color: #f0f0f0;
    padding: 1rem;
  }
  
  .panel-content {
    flex: 1;
    padding: 2rem;
  }
  </style>
  