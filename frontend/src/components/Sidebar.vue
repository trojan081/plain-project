<template>
    <div class="sidebar">
      <router-link to="/dashboard/projects" class="link">Мои проекты</router-link>
      <router-link to="/dashboard/organization" class="link">Моя организация</router-link>
      <button class="add-btn">Добавить проект</button>
    </div>
  </template>
  
  <style scoped>
  .sidebar {
    width: 240px;
    background-color: #f5f5f5;
    padding: 20px;
    border-right: 1px solid #ddd;
    min-height: 100vh;
  }
  .link {
    display: block;
    margin-bottom: 1rem;
    font-weight: bold;
  }
  .add-btn {
    margin-top: 2rem;
    background: royalblue;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    cursor: pointer;
  }
  </style>
  