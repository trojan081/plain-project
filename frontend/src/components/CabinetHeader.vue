<template>
    <header class="cabinet-header">
        <router-link to="/" class="logo" @click="reloadPage">
            <img src="../assets/logo_no_back.png" alt="logo" class="logo"/>
        </router-link>
        <button @click="logout" class="logout-btn">Выйти</button>
    </header>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  import axios from 'axios'
  
  const router = useRouter()
  


    function cabinet() {
    window.location.reload()
    }

  async function logout() {
    await axios.post('/api/logout', {}, { withCredentials: true })
    router.push('/login')
  }
  </script>
  
  <style scoped>
  .cabinet-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: #ffffff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    padding: 1rem 2rem;
    display:flex;
    justify-content: space-between;
    align-items: center;
    z-index: 1000;
  }


  .cabinet-logo {
    font-weight: bold;
    font-size: 1.5rem;
    text-decoration: none;
    color: #012b85;
  }
  .cabinet-menu {
    display: flex;
    gap: 1.5rem;
  }
  .cabinet-menu-item {
    text-decoration: none;
    color: #333;
    font-size: 1rem;
    cursor: pointer;
    background: none;
    border: none;
  }
  .cabinet-menu-item:hover {
    color: #012b85;
  }

  .logout-btn {
  padding: 0.5rem 1rem;
  background: #f9f9f9;
  box-shadow: 0 0 10px rgba(37, 35, 35, 0.199);
  border: none;
  color: #000000;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 3%;
}
.logout-btn:hover {
  opacity: 0.8;
}

</style>
  