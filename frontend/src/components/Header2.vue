<template>
  <header>
    <div class="container">
        <router-link to="/">
      <div id="logo"><img src="/assets/logo_2.png" alt="logo" class="logo"/></div>
        </router-link>
      <button class="menu-toggle" @click="toggleMenu" :class="{active: isMenuOpen}">
        <span class="hamburger-icon"></span>
        <span class="hamburger-icon"></span>
        <span class="hamburger-icon"></span>
      </button>
      <nav :class="{ open: isMenuOpen }">
        <ul class="nav-links">
          <li><a href="#">О нас</a></li>
          <li><a href="#">Возможности</a></li>
          <router-link to="demo">
          <li><a href="#">Demo</a></li>
          </router-link>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue';

const isMenuOpen = ref(false);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: Arial, sans-serif;
}
.container {
    max-width: 5200px;
    margin: 0 3%;
    padding: 0 20px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
header {
    background-color: #000000;
    color: #ffffff;
    padding: 10px 0;
}
#logo {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
}
nav {
    /* Нет необходимости в изменениях здесь для этой проблемы */
}
.nav-links {
    list-style-type: none;
    margin: 0;
    padding: 0;
}
.nav-links li {
    display: inline-block;
    margin-left: 20px;
}
.nav-links li a {
    color: #ffffff;
    text-decoration: none;
    padding: 10px 15px;
    display: inline-block;
    transition: background-color 0.3s;
}
.nav-links li a:hover {
    background-color: #555;
}
.content {
    padding: 50px 0;
    text-align: center;
}
.logo {
    
    max-width: 150px; 
    width: 78%; 
    height: auto;
}
.menu-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 10px;
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 100;
}

.hamburger-icon {
  display: block;
  width: 25px;
  height: 3px;
  background-color: #ffffff;
  margin: 5px 0;
  transition: all 0.3s ease-in-out;
}

.menu-toggle.active .hamburger-icon:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}
.menu-toggle.active .hamburger-icon:nth-child(2) {
  opacity: 0;
}
.menu-toggle.active .hamburger-icon:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}

@media (max-width: 768px) {
  .menu-toggle {
    display: block;
  }
  .container {
    height: auto;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    position: relative;
  }
  #logo {
    margin-bottom: 0;
  }
  nav {
    position: fixed;
    top: 0;
    right: 0;
    width: 70vw;
    height: 100vh;
    background: rgba(0,0,0,0.95);
    display: flex;
    justify-content: center;
    align-items: center;
    transform: translateX(100%);
    transition: transform 0.35s cubic-bezier(.5, 0, .2, 1);
    z-index: 90;
  }
 nav.open {
    transform: translateX(0);
  }
  .nav-links {
    flex-direction: column;
    padding: 10px 0;
  }
  .nav-links li {
    display: block;
    margin: 0;
    transition: opacity 0.35s ease, transform 0.35s ease;
  }
  .nav-links li a {
    padding: 15px;
    display: block;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }
  .nav-links li:last-child a {
    border-bottom: none;
  }
  
}
</style>