<template>
    <div class="panel-layout">
      <div class="panel-sidebar">
        <h2>О нас</h2>
      </div>
      <div class="panel-content">
        <h1>О нашей компании</h1>
        <p>
          Здесь вы можете разместить информацию о миссии, истории и ценностях вашей компании.
        </p>
      </div>
    </div>
  </template>
  
  <script setup>
    // Здесь можно добавить логику, если потребуется
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
  