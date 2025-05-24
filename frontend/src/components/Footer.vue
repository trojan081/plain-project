<!-- src/components/Footer.vue -->
<template>
    <footer class="footer">
      <p class="allrights">&copy; {{ new Date().getFullYear() }} Plain. Все права защищены.</p>
      <div class="footer_headers">
        <p class="docs" >Документы</p>
        <p class="docs" >Проект выполнен при поддержке Фонда Содействия Инновациям федерального проекта "Платформа университетского
          технологического предпринимательства"</p>
      </div>
      <div class="footer_content">
        <div>
          <a class="docs" href="http://localhost:3000/policy">Политика конфиденциальности</a>
          <a class="docs" href="http://localhost:3000/offer">Публичная оферта</a>
          <a class="docs" href="http://localhost:3000/main_agreement">Согласие на обработку ПД</a>
          <a class="docs" href="http://localhost:3000/agreement">Согласие на получение рассылок</a>
        
      </div>
        <div class="logos">
          <img class="fasie_logo" src="../assets/fasie_logo.png" alt="FASIE Logo">
          <img class="uni_platform_logo" src="../assets/uni_platform_logo.png" alt="UNI Logo">
        </div>
      </div>
      
    </footer>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  .footer {
    text-align: center;
    padding: 1rem;
    font-size: 0.9rem;
    color: #aaa;
    background-color: #1a1a1a;
    margin-top: auto;
  }
  </style>
  