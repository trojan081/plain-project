
<template>
    <div v-show="isLoading" class="loading-screen">
      <img src="/assets/gear.jpg" alt="Loading..." class="loading-icon" />
    </div>
    
          <div>
            <div 
              class="header" 
              :style="{ filter: `blur(${blurValue}px)` }"
            >
              <div class="centered-title-container">
                <div class="main-title">PLAIN</div>
                <div class="subtitle">новое слово в проектировании</div>
              </div>
            </div>
            
            <!-- <Card /> -->
          <!-- <div class="triple-wrapper">
        <div class="center-column">
            <div class="gates-container" ref="gatesContainer">
              <div class="gate gate-left" ref="gateLeft" :style="{ backgroundImage: 'url(/assets/gate-1.jpg)' }"></div>
              <div class="gate gate-right" ref="gateRight" :style="{ backgroundImage: 'url(/assets/gate-2.jpg)' }"></div>
              <div class="gate-text" ref="gateText">
                <span>P </span>
                <span>L </span>
                <span class="colored-letter">A </span>
                <span class="colored-letter">I </span>
                <span>N</span>
              </div>
              <div class="text-after-gates" ref="contentAfterGates">
                <p>Новое слово в проектировании</p>
                
              </div>
            </div>
          </div>
        </div> -->
      </div>
        <!-- <div class="llmchat-container">
          <LLMChat />
        </div> -->
    <!-- <Lines1 /> -->
    <HeroBanner />
    <InnovationSection />
    <Cards />
    <!-- <hr class="hr-0" /> -->

          <!-- <div class="img-cube-container" ref="imgContainer">
            <img
              src="/assets/2.jpg"
              alt="Image 1"
              class="fade-in-1"
              :class="{ visible: isImgVisible }"
            />
            <img
              src="/assets/3.jpg"
              alt="Image 2"
              class="fade-in-2"
              :class="{ visible: isSecondImgVisible }"
            />
          </div> -->
      <Team />
      <div class="usage-block-wrapper">
        <div class="usage-background"></div>
        <div class="usage-block">
          <UsageBlock />
        </div>
      </div>
          
      

          
          <div class="triple-wrapper">
        <div class="center-column">
          <div class="text-1-container">
            <h2 class="text-h2">Дорожная карта</h2>
          </div>
          <!-- <RoadmapSection /> -->
          <RoadMap2 />
        <div class="start-section">
          <div class="start-content">
            <!-- <img class="demo-img" src="/assets/cad6.jpg"/> -->
            <p class="start-text">  
              Протестируйте наш продукт прямо сейчас — Просто загрузите файл проекта и получите автоматический расчёт объёмов работ. Это бесплатно.
            </p></div>
            <router-link to="/demo" class="start-button">
              Перейти к DEMO
            </router-link>
          
          

        </div>
        </div>
        </div>
        
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue'
  import { useI18n } from 'vue-i18n'
  import RoadmapSection from '@/components/RoadmapSection.vue'
  import RoadMap2 from '@/components/RoadMap2.vue'
  import Cube1 from '@/components/Cube1.vue'
  import Lines1 from '@/components/Lines1.vue'
  import LLMChat from '@/components/LLMChat.vue'
  import Card from '@/components/Card.vue'
  import InnovationSection from '@/components/InnovationSection.vue'
  import HeroBanner from '@/components/HeroBanner.vue'
  import Cards from '@/components/Cards.vue'
  import Team from '@/components/Team.vue'
  import UsageBlock from '@/components/UsageBlock.vue'

    const roadmapImages = [
      {
        href: '/assets/cad2.jpg',
        x: 351,
        y: 240,
        label: 'Обработка данных',
        labelX: 615,
        labelY: 294,
        width: 90,
        height: 90,
      },
      {
        href: '/assets/cad1.jpg',
        x: 420,
        y: 414,
        label: 'Объёмы работ',
        labelX: 660,
        labelY: 471,
        width: 90,
        height: 90,
      },
      // ...добавьте остальные картинки по аналогии
    ]
      const isLoading = ref(true);
      const { locale } = useI18n()
      const changeLocale = (lang) => {
        locale.value = lang
      }
      const showTitle = ref(false)
      const showSubtitle = ref(false)
      const showForm = ref(false)
      const company = ref('')
      const email = ref('')
      const message = ref('')
      const blurValue = ref(0)
      const isSectionVisible = ref(false)
      const isImgVisible = ref(false)
      const isSecondImgVisible = ref(false)
      const sloganText = ref('P L A I N'.split(''))
      const isSloganVisible = ref(false)
      const sloganContainer = ref(null)
      const imgContainer = ref(null)
      const gateText = ref(null)
      const gridItems = ref([]);
      const gridItemVisibility = ref([]);
  
      let startTouchY = 0;

  
      const gatesContainer = ref(null)
      const gateLeft = ref(null)
      const gateRight = ref(null)
      const contentAfterGates = ref(null)
      const gatesProgress = ref(0)
      const areGatesOpened = ref(false)
      let isOpening = false;
  
      const handleTouchStart = (e) => {
        const touch = e.touches[0];
      //  startTouchY = touch.clientY;
      };
  
      const handleTouchMove = (e) => {
        if (areGatesOpened.value) return; // Если ворота уже открыты, ничего не делаем
  
        const touch = e.touches[0];
        const diffY = touch.clientY - startTouchY;
  
        // Разрешаем прокрутку страницы после того, как ворота начали открываться
        if (gatesProgress.value >= 0.3) {
          document.body.style.overflow = "auto"; // Включаем стандартный скроллинг
          return;
        }
  
        // Открытие ворот
        gatesProgress.value += diffY * 0.01;
        if (gatesProgress.value < 0) gatesProgress.value = 0;
        if (gatesProgress.value > 1) {
          gatesProgress.value = 1;
          areGatesOpened.value = true;
          document.body.style.overflow = "auto"; // Разрешаем прокрутку после полного открытия
        }
  
        updateGatesTransform();
        startTouchY = touch.clientY;
      };
  
      const updateGatesTransform = () => {
        if (!gateLeft.value || !gateRight.value) return;
        gateLeft.value.style.transform = `translateX(${ -100 * gatesProgress.value }%)`;
        gateRight.value.style.transform = `translateX(${ 100 * gatesProgress.value }%)`;
      };
  
      const imgObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            isImgVisible.value = true
            setTimeout(() => {
              isSecondImgVisible.value = true
            }, 100)
            imgObserver.unobserve(entry.target)
          }
        })
      }, { threshold: 0.5 })
  
      const handleScroll = () => {
        const section = document.querySelector('.grid-item');
        if (!section) return;
        const rect = section.getBoundingClientRect();
        const offset = window.innerHeight * 0.8;
        isSectionVisible.value = rect.top < offset && rect.bottom > 0;
      };
     
      const handleWheel = (e) => {
        if (areGatesOpened.value || isOpening) return;
  
        e.preventDefault();
  
        if (!isOpening) {
          isOpening = true;
          setTimeout(() => {
            gatesProgress.value += e.deltaY * 0.01;
  
            if (gatesProgress.value < 0) gatesProgress.value = 0;
            if (gatesProgress.value > 1) {
              gatesProgress.value = 1;
              areGatesOpened.value = true;
              document.body.style.overflow = 'auto';
            }
  
            updateGatesTransform();
  
            isOpening = false;
          }, 330);
        }
      };
  
      onMounted(() => {
        setTimeout(() => {
          isLoading.value = false; //
            }, 900);
          
        setTimeout(() => (showTitle.value = true), 100);
        setTimeout(() => (showSubtitle.value = true), 300);
  
        // window.addEventListener('scroll', handleScroll);
        window.addEventListener('wheel', handleWheel, { passive: false });
        window.addEventListener('touchstart', handleTouchStart, { passive: false });
        window.addEventListener('touchmove', handleTouchMove, { passive: false });
  
        const gridItems = document.querySelectorAll('.grid-item');
        const observer = new IntersectionObserver((entries, observer) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.classList.add('visible');
              // Прекращаем наблюдение, чтобы элемент оставался видимым
              observer.unobserve(entry.target);
            }
          });
        }, { threshold: 0.8 }); // можно подобрать порог по вкусу
  
        gridItems.forEach(item => observer.observe(item));
  
  
        const video = document.querySelector("video");
        if (video) {
          video.addEventListener('loadedmetadata', () => {
            video.play().catch(() => {
              console.log("Автовоспроизведение заблокировано, включаем вручную...");
              video.muted = true;
              video.play();
            });
          });
        }

  
        updateGatesTransform();
  
        if (imgContainer.value) {
        imgObserver.observe(imgContainer.value)
          }
        });
  
        const userAgent = window.navigator.userAgent;
        const isiOS = /iPad|iPhone|iPod/.test(userAgent) && !window.MSStream;
        const isSafari = /^((?!chrome|android).)*safari/i.test(userAgent);
  
        if (isiOS || isSafari) {
          document.body.classList.add("ios");
        }
  
      onUnmounted(() => {
        window.removeEventListener('scroll', handleScroll);
        window.removeEventListener('wheel', handleWheel, { passive: false });
        window.removeEventListener('touchstart', handleTouchStart, { passive: false });
        window.removeEventListener('touchmove', handleTouchMove, { passive: false });
        document.body.style.overflow = 'auto'; // Возвращаем стандартное поведение прокрутки
      });
  </script>

<style scoped>

.start-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  border: 1px solid #2f56914d;
  box-shadow: 0 0 10px rgba(37,35,35,0.2);
  padding: 2.1rem;
  margin: 10%;
  border-radius: 72px;
}

.start-title {
  font-size: 2rem;
  color: #012b85;
  margin-bottom: 1rem;
  font-weight: 600;
}

.start-content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1.5rem;
}
.demo-img {
  width: 110px;
  min-width: 80px;
  max-width: 160px;
  border-radius: 18px;
  box-shadow: 0 2px 12px #0001;
  object-fit: cover;
}
.start-text {
  font-size: 1.2rem;
  color: #333;
  line-height: 1.6;
  text-align: center;
}


.start-button {
  display: inline-block;
  background-color: #dbe8f05e;
  color: #000000;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border: 1px solid #0066ff;
  border-radius: 12px;
  text-decoration: none;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s, transform 0.2s;
}

.start-button:hover {
  background-color: #e0e0e091;;
  transform: translateY(-2px);
}

/* Optional animation */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


@media (max-width: 768px) {
  .start-section {
    padding: 1.2rem 1rem;
    margin: 5% auto;
    border-radius: 32px;
    width: 80%;
    box-shadow: 0 2px 16px rgba(0, 0, 0, 0.1);
    gap: 1.5rem;
  }

  .start-content {
    flex-direction: column;
    text-align: center;
    gap: 1.2rem;
  }

  .start-text {
    font-size: 0.75rem;
    line-height: 1.5;
    /* padding: 0 0.4rem; */
  }

  .start-button {
    font-size: 0.81rem;
    padding: 0.6rem 1.2rem;
    width: 45%;
    max-width: 280px;
    text-align: center;
    border-radius: 18px;
  }

  .demo-img {
    width: 100%;
    max-width: 220px;
    border-radius: 14px;
  }
}
.oval-container-1, .oval-container-2 {
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
}
.oval-container-1:hover {
  box-shadow: 0 12px 48px 0 #81c7ff2c, 0 2px 8px #6e8bd924;
  background: linear-gradient(96deg, #1d6aa815  40%, #fafdff 50%);
}

.oval-container-2:hover {
  /* Зеркальная (reverse) тень — вверх, а не вниз + reverse gradient */
  box-shadow: 0 -12px 48px 0 #81c7ff2c, 0 -2px 8px #6e8bd924;
  background: linear-gradient(264deg, #1d6aa815 40%, #fafdff 50%);
}
.user { 
  text-align:right; 
  color:#3477f5 
}
.ai   { 
  text-align:left;  
  color:#333 
}
.llmchat-container {
  margin-top: 120px;
  margin-bottom: 0px;
}
.centered-title-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 100%;
  height: 300px;      /* регулируй по желанию */
  position: relative;
  z-index: 2;
  /* background-color: #3563b81c; */
  /* -webkit-mask-image: linear-gradient(to right, transparent 0%, rgb(0, 0, 0) 12%, black 88%, transparent 100%); */
  /* mask-image: linear-gradient(to right, transparent 0%, black 10%, black 90%, transparent 100%); */
}

.main-title {
  font-size: clamp(2.1rem, 5vw + 1.1rem, 4.2rem);
  font-weight: 900;
  color: #ffffff;
  text-shadow: 4px 2px 4px rgba(17, 17, 17, 0.888);
  margin-bottom: 0.7em;
  margin-top: 10%;
  letter-spacing: 0.35em;
  opacity: 0;
  transform: translateY(-40px) scale(0.98);
  animation: titleFadeIn 1.2s cubic-bezier(.56,0,.31,1) forwards;
  animation-delay: 0.3s;
}

.subtitle {
  font-size: clamp(1.2rem, 2.1vw + 0.9rem, 2.5rem);
  font-weight: 400;
  color: #ffffff;
  text-shadow: 2px 1px 4px rgb(17, 17, 17, 0.888);
  letter-spacing: 0.01em;
  opacity: 0;
  transform: translateY(40px) scale(0.97);
  animation: subtitleFadeIn 1.25s cubic-bezier(.56,0,.31,1) forwards;
  animation-delay: 1.2s;
}

/* Ключевые кадры анимации */
@keyframes titleFadeIn {
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes subtitleFadeIn {
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.usage-block-wrapper {
  position: relative;
  overflow: hidden;
}

/* фоновая картинка, которую размоем */
.usage-background {
  position: absolute;
  inset: 0;
  background: url('/assets/bg6.png') center/cover no-repeat;
  /* filter: blur(2220px); */
  z-index: 1;
}
/* .innovation-section {
  padding: 4rem 230px; 
  background: url('/assets/bg3.png') no-repeat center/cover;
  border-top: 1px solid #e9e9e9fd;
  border-bottom: 1px solid #e9e9e9fd;
  margin: 40px auto;
  box-shadow: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-top: 9%;
  padding-bottom: 15%;
  
} */

/* содержимое поверх */
.usage-block {
  position: relative;
  z-index: 2;
  padding-bottom: 13%;
  border-bottom: 1px solid #e9e9e9fd;
  background-color: rgba(255, 255, 255, 0.3); /* если нужно подсветлить */
  backdrop-filter: blur(224px); 
}

  </style>