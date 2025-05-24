// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import axios from 'axios'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Cabinet from '../views/Cabinet.vue'
import About from '../views/About.vue'
import Contacts from '../views/Contacts.vue'
import PrivacyPolicy from '../views/PrivacyPolicy.vue'
import OfferAgreement from '../views/OfferAgreement.vue'
import AdvertisementAgreement from '../views/AdvertisementAgreement.vue'
import MainAgreement from '../views/MainAgreement.vue'
import Projects from '../views/Projects.vue'
import AddProject from '../views/AddProject.vue'
import ProjectInfo from '../views/ProjectInfo.vue'
import UserProfile from '../views/UserProfile.vue'
import DemoPage from '../views/DemoPage.vue'

const routes = [
  { path: '/',            name: 'Home',               component: Home },
  { path: '/login',       name: 'Login',              component: Login },
  { path: '/register',    name: 'Register',           component: Register },
  { path: '/cabinet',     name: 'Cabinet',            component: Cabinet, meta: { requiresAuth: true }  },
  { path: '/about',       name: 'About',              component: About },
  { path: '/contacts',    name: 'Contacts',           component: Contacts },
  { path: '/policy',      name: 'PrivacyPolicy',      component: PrivacyPolicy },
  { path: '/offer',       name: 'OfferAgreement',     component: OfferAgreement },
  { path: '/agreement',   name: 'AdvertisementAgreement', component: AdvertisementAgreement },
  { path: '/main_agreement', name: 'MainAgreement',   component: MainAgreement },
  { path: '/projects',    name: 'Projects',           component: Projects, meta: { requiresAuth: true } },
  { path: '/add_project',    name: 'AddProject',      component: AddProject, meta: { requiresAuth: true } },
  { path: '/project/:id',    name: 'ProjectInfo',     component: ProjectInfo, meta: { requiresAuth: true } },
  { path: '/user/:slug',    name: 'UserProfile',        component: UserProfile, meta: { requiresAuth: true } }, 
  { path: '/demo', name: 'DemoPage', component: DemoPage},
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// Глобальный guard: перед заходом в Cabinet проверяем сессию на бэке
router.beforeEach(async (to, from, next) => {
  if (!to.meta.requiresAuth) {
    return next() // если маршрут не требует авторизации — пропускаем
  }

  try {
    await axios.get('/api/user_info', { withCredentials: true })
    next() // пользователь залогинен — пропускаем
  } catch (err) {
    next({ name: 'Login' }) // если не залогинен — редирект на /login
  }
})

export default router
