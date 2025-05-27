<template>
    <header class="top-menu">
      <router-link to="/" class="logo" @click="reloadPage">
        <img src="../assets/logo_no_back.png" alt="logo" class="logo"/>
      </router-link>
      <nav class="menu" ref="menuContainer" @mouseenter="openDropdown" @mouseleave="closeDropdown">
        <!-- <span class="menu-text">Меню</span> -->
        <!-- <transition name="dropdown">
          <div class="dropdown-content" v-show="isDropdownOpen">
            <router-link to="/" class="dropdown-item" @click="closeDropdown">Главная</router-link>
            <router-link to="/register" class="dropdown-item" @click="closeDropdown">Регистрация</router-link>
                        <a href="#" class="dropdown-item" @click.prevent="handleCabinet">Вход</a>
            <router-link to="/about" class="dropdown-item" @click="closeDropdown">О нас</router-link>
            <router-link to="/contacts" class="dropdown-item" @click="closeDropdown">Контакты</router-link>
          </div>
        </transition> -->
        <span class="demo" @click="openDemo">Demo</span>
      </nav>
    </header>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  const isDropdownOpen = ref(false)
  
  function openDropdown() {
    isDropdownOpen.value = true
  }

  function openDemo() {
      router.push('/demo')
    }

  function reloadPage() {
  window.location.href = "/";
  }
  function closeDropdown() {
    isDropdownOpen.value = false
  }
  
  // Функция для проверки авторизации и перехода в кабинет
  function handleCabinet() {
    const isAuthenticated = false  // Замените на реальную логику проверки авторизации
    closeDropdown()
    if (isAuthenticated) {
      router.push('/cabinet')
    } else {
      router.push('/register')
    }
  }
  </script>
  
  <style scoped>
  .top-menu {
    position: fixed; 
    top: 0;
    left: 0;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #ffffff;
    color: #fff;
    /* height: 6%; */
    padding: 0.3rem 1rem;
    background-color: rgba(255, 255, 255, 0.0);
    z-index: 1000;   
  }


  
  /* .logo {
    scale: 1.2;
    padding-left: 1%;
  } */
  
  .menu {
    position: relative;
  }
  
  /* Надпись "Меню" */
  .menu-text {
    font-size: 1.2vw;
    color: #fff;
    cursor: pointer;
    user-select: none;
  }
  
  /* Выпадающий список, подстраивающийся под контент */
  .dropdown-content {
    position: absolute;
    top: 110%;
    right: 0;
    background-color: #000; /* фон совпадает с хедером */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    z-index: 999;
    overflow: hidden;
    border-radius: 9%;
    padding: 0.5rem 0;
    width: auto;
    white-space: nowrap;
  }
  
  /* Элементы выпадающего списка */
  .dropdown-item {
    display: block;
    padding: 0.5rem 1rem;
    color: #fff; /* белый текст */
    text-decoration: none;
    text-align: center;
    background-color: #000;
    cursor: pointer;
    font-size: 1.2vw;
  }
  
  .dropdown-item:hover {
    background-color: #333;
  }
  
  /* Плавное появление/скрытие выпадающего списка */
  .dropdown-enter-active,
  .dropdown-leave-active {
    transition: all 0.3s ease;
  }
  .dropdown-enter-from,
  .dropdown-leave-to {
    transform: translateY(-10px);
    opacity: 0;
  }
  .dropdown-enter-to,
  .dropdown-leave-from {
    transform: translateY(0);
    opacity: 1;
  }

.demo {
  cursor: pointer;
  color: rgba(0, 0, 0, 0.466);
  font-size: 1.2vw;
  padding: 1rem 3rem;
}
.demo:hover {
  background-color: #2f56911a;
  border-radius: 12px;
}

/* .logo img {
  height: 2.5rem;
  max-height: 10vw;
  width: auto;
  transition: transform 0.3s ease;
}
.logo img:hover {
  transform: scale(1.05);
} */

.demo {
  cursor: pointer;
  color: rgba(0, 0, 0, 0.6);
  font-size: 1.1rem;
  padding: 0.7rem 3.3rem;
  background: transparent;
  border: 1.5px solid transparent;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.demo:hover {
  background-color: #2f56911a;
  border-color: #2f569155;
}

.logo img {
  padding-left: 0.8rem;
  transform: scale(1);
  transform-origin: left center;
  transition: transform 0.3s ease, padding-left 0.3s ease;
  height: auto;
  display: block;
}

/* Hover эффект — немного увеличим логотип */
.logo img:hover {
  transform: scale(1.05);
}

/* ====== Мобильная адаптация ====== */
@media (max-width: 768px) {
  .logo img {
    padding-left: 0.1rem;
    transform: scale(0.85);
    scale: 1.8;
  }
}

/* ====== Широкие экраны (например 1440px+) ====== */
@media (min-width: 1440px) {
  .logo img {
    padding-left: 1.2rem;
    transform: scale(1.15);
    scale: 0.8;
  }
}
  </style>
  