<template>
    <!-- Loading Screen -->
    <div v-show="isLoading" class="loading-screen">
      <img src="/assets/gear.jpg" alt="Loading..." class="loading-icon" />
    </div>
  

          <div>
            <div 
              class="header" 
              :style="{ filter: `blur(${blurValue}px)` }"
            >
              <h1 class="title-left" :class="{ visible: showTitle }">The Future</h1>
              <h2 class="title-right" :class="{ visible: showSubtitle }">is Now</h2>
              
            </div>
            
          <div class="triple-wrapper">
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
        </div>
      </div>
        <div class="llmchat-container">
          <LLMChat />
        </div>
    <hr class="hr-0" />
      <div class="triple-wrapper">
        <div class="center-column">

          <div class="img-cube-container" ref="imgContainer">
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
          </div>
      
<div class="text-1-container" ref="textContainer">
            <p class="text-h1">Мы создаем инновации</p>
          </div>
      
          <div class="oval-container-1">
            <div class="content-row">
              <div class="text-v-2-Container">
                <p class="text-v-2">
                  Внедряем новейшие технологии в процессы благоустройства современной городской среды
                </p>
              </div>
              <div class="video-container">
                <video loop autoplay muted playsinline class="background-video">
                  <source src="../assets/videos/v1.mp4" type="video/mp4" />
                  Ваш браузер не поддерживает видео.
                </video>
              </div>
            </div>
          </div>

      
          <div class="oval-container-2">
            <div class="content-row">
              <div class="video-container">
                <video loop autoplay muted playsinline class="background-video">
                  <source src="../assets/videos/v3.mp4" type="video/mp4" />
                  Ваш браузер не поддерживает видео.
                </video>
              </div>
        
              <div class="text-v-1-Container">
                <p class="text-v-1">
                  Выводим качество и скорость<br> выполнения проектов на новый уровень
                </p>
              </div>
            </div>
          </div>  
      
          <div class="oval-container-1">
            <div class="content-row">
              <div class="text-v-1-Container">
                <p class="text-v-2">
                  Даем возможность получить <br> преимущества перед конкурентами
                </p>
              </div>
        
              <div class="video-container">
                <video loop autoplay muted playsinline class="background-video">
                  <source src="../assets/videos/v5.mp4" type="video/mp4" />
                  Ваш браузер не поддерживает видео.
                </video>
              </div>
            </div>
          </div>
      
          <div class="text-2-container" ref="textContainer">
            <p class="text-h2">Зачем это нужно?</p>
          </div>
      
          <div class="grid-container">
            <div class="grid-row">
              <div class="grid-item" 
                   v-for="(item, index) in l_column" 
                   :key="'row2-' + index"
                   :class="{ visible: isSectionVisible }">
                <div class="card">
                  <div class="card-face card-front">
                    <img :src="item.imgSrc" alt="Image" />
                    <p class="text_advantages"><b>{{ item.text_1 }}</b>{{ item.text_2 }}</p>
                  </div>
                  <div class="card-face card-back">
                    <h3>{{ item.adv_header }}</h3>
                    <div class="adv-row">
                      <img src="../assets/dislike.jpg" alt="Image_dislike" class="like_dislike"/>
                      <p class="text_advantages">{{item.adv_1}}<b>{{item.adv_1_1}}</b></p>
                    </div>
                    <div class="adv-row">
                      <img src="../assets/like.jpg" alt="Image_dislike" class="like_dislike"/>
                      <p class="text_advantages">{{item.adv_2}}<b>{{item.adv_2_2}}</b></p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- Вторая строка карточек -->
            <div class="grid-row">
              <div class="grid-item" 
                   v-for="(item, index) in r_column" 
                   :key="'row2-' + index"
                   :class="{ visible: isSectionVisible }">
                <div class="card">
                  <div class="card-face card-front">
                    <img :src="item.imgSrc" alt="Image" />
                    <p class="text_advantages"><b>{{ item.text_1 }}</b>{{ item.text_2 }}</p>
                  </div>
                  <div class="card-face card-back">
                    <h3>{{ item.adv_header }}</h3>
                    <div class="adv-row">
                      <img src="../assets/dislike.jpg" alt="Image_dislike" class="like_dislike"/>
                      <p class="text_advantages">{{item.adv_1}}<b>{{item.adv_1_1}}</b></p>
                    </div>
                    <div class="adv-row">
                      <img src="../assets/like.jpg" alt="Image_dislike" class="like_dislike"/>
                      <p class="text_advantages">{{item.adv_2}}<b>{{item.adv_2_2}}</b></p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
      
          <div class="text-1-container">
            <p class="text-h1">Кому подойдёт?</p>
          </div>
          <div class="suitable-for-section">
            <div class="suitable-for-container">
              <div class="suitable-for-item" 
                   v-for="(item, index) in suitableForItems" 
                   :key="index">
                <img :src="item.imgSrc" alt="Подходит" class="suitable-for-img" />
                <h3 class="suitable-for-title">{{ item.title }}</h3>
                <div class="suitable-for-description">
                  <ul class="suitable_for_list">
                    <li v-for="(desc, i) in item.description" :key="i">{{ desc }}</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
        </div>
          <hr class="custom-hr" /> 
          
          <div class="triple-wrapper">
        <div class="center-column">
          <div class="text-1-container">
            <h2 class="text-h2">Дорожная карта</h2>
          </div>
          <RoadmapSection />
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
  import Cube1 from '@/components/Cube1.vue'
  import Lines1 from '@/components/Lines1.vue'
  import LLMChat from '@/components/LLMChat.vue'


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
      const l_column = ref([
      { 
      imgSrc: './webp/k1.webp', 
      text_1: 'Скорость:', 
      text_2: ' забудьте про дедлайны', 
      adv_header: 'Мы сократили время разработки проектной документации в десятки раз',
      adv_1: 'Время разработки ПД:',
      adv_1_1: '  2-4 недели',
      adv_2: 'С помощью Plain:',
      adv_2_2: ' 30 минут'
    },
    { 
      imgSrc: './webp/k2.webp', 
      text_1: 'Гибкость:', 
      text_2: ' исправляйте в один клик', 
      adv_header: 'Надоело переделывать чертежи из-за очередных изменений в проекте?',
      adv_1: 'Корректировка чертежей вручную',
      adv_2: 'Plain: исправит всё автоматически'
    },
    { 
      imgSrc: './webp/kkkkk4.webp', 
      text_1: 'Автоматизация:', 
      text_2: ' делегируйте рутину',
      adv_header: 'Мы научили алгоритмы выполнять ежедневные задачи за Вас',
      adv_1: 'Чрезмерная многозадачность',
      adv_2: 'Передайте часть задач Plain'
    },
      ])
      
      const r_column = ref([
      { 
      imgSrc: './webp/kk33.webp', 
      text_1: 'Время:', 
      text_2: ' сосредоточьтесь на важном',
      adv_header: 'Освободили для Вас наиболее ценный ресурс - Ваше время',
      adv_1: 'Участвовать во всех процессах',
      adv_2: 'Эффективно управлять процессами'
    },
      { 
      imgSrc: './webp/kkkk5.webp', 
      text_1: 'Технологии:', 
      text_2: ' точность чертежей до 99%',
      adv_header: 'Исключили "внезапные" ошибки в чертежах и расчетах',
      adv_1: 'Проверять за проектировщиками',
      adv_2: 'Использовать новые технологии'
    },
      {
      imgSrc: './webp/kk5.webp', 
      text_1: 'Расходы:', 
      text_2: ' сократите издержки',
      adv_header: 'Сохраняем Ваши средства благодаря эффективному управлению ресурсами',
      adv_1: 'Оплачивать долгие проекты',
      adv_2: 'Экономить с помощью Plain'
    }
      ])

  
      const suitableForItems = ref([
          { 
            imgSrc: '/assets/for_whom_1_2.jpg', 
            title: 'Инженерам генплана', 
            description: ['Скорость разработки ПД',
                          'Простота изменений',
                          'Минимизация ошибок'
            ] 
          },
          { 
            imgSrc: '/assets/for_whom_2_3.jpg', 
            title: 'Владельцам бизнеса', 
            description: ['Оптимизация процессов',
                          'Новейшие технологии ИИ',
                          'Преимущества на рынке'
            ] 
          },
          { 
            imgSrc: '/assets/for_whom_3.jpg', 
            title: 'Руководителям', 
            description: ['Расчёт KPI команды',
                          'Соблюдение сроков',
                          'Полный контроль задач',
                          
            ] 
          },
          { 
            imgSrc: '/assets/for_whom_4.jpg', 
            title: 'Фрилансерам', 
            description: ['Больше заказов',
                          'Высокая эффективность',
                          'Надёжность и репутация'
            ] 
          },
        ]);
  
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
.innovation-hero {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 2.8rem;
  margin: 54px 0 64px 0;
  background: linear-gradient(105deg, #f7faff 70%, #e0edff 100%);
  border-radius: 40px;
  box-shadow: 0 6px 48px #9ab5ff25, 0 2px 8px #8bbfff12;
  padding: 2.8rem 3.5rem 2.2rem 2.9rem;
  animation: heroAppear 1.2s cubic-bezier(.61,0,.18,1.04);
  overflow: hidden;
}

@keyframes heroAppear {
  from {
    opacity: 0;
    transform: translateY(56px) scale(0.97);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.split-innovation-block {
  display: flex;
  align-items: center;
  background: #fafdff;
  border-radius: 38px;
  box-shadow: 0 7px 38px #0086ff18, 0 2px 8px #8bbfff09;
  margin: 68px 0 58px 0;
  padding: 2.7rem 2.3rem 2.2rem 1.4rem;
  position: relative;
  min-height: 270px;
  overflow: hidden;
}

.split-innovation-stripe {
  width: 9px;
  min-width: 9px;
  height: 78%;
  background: linear-gradient(145deg, #5ae0fd 20%, #2196f3 92%);
  border-radius: 12px;
  margin-right: 32px;
  margin-left: 8px;
  box-shadow: 0 0 18px #2196f330;
  animation: stripeAppear 1.2s cubic-bezier(.6,0,.39,1.34);
}
@keyframes stripeAppear {
  from { height: 0; opacity: 0.1;}
  to   { height: 78%; opacity: 1;}
}

.split-innovation-content {
  flex: 1 1 56%;
  z-index: 2;
}

.split-innovation-header {
  display: flex;
  align-items: center;
  gap: 1.4rem;
  margin-bottom: 0.5em;
}

.innovation-icon {
  filter: drop-shadow(0 0 10px #2196f322);
  transition: filter 0.17s;
}

.split-innovation-title {
  font-size: 2.2rem;
  font-weight: 900;
  color: #0e3b66;
  letter-spacing: 0.01em;
  position: relative;
  display: inline-block;
}

.glow-text {
  color: #2196f3;
  text-shadow: 0 2px 18px #5ae0fd33, 0 1px 2px #8bbfff66;
  font-weight: 900;
  position: relative;
}

.split-innovation-desc {
  font-size: 1.19rem;
  color: #376893;
  font-weight: 500;
  line-height: 1.53;
  margin-bottom: 0;
  margin-top: 0.2em;
  border-left: 4px solid #00b4fc35;
  background: #f6fbffed;
  padding: 1em 1.8em 1em 1.2em;
  border-radius: 13px;
  box-shadow: 0 2px 18px #83c3ff1c;
  transition: background 0.22s, box-shadow 0.28s;
  max-width: 520px;
}

.split-innovation-video-wrap {
  flex: 0 0 320px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 3.1rem;
  background: linear-gradient(135deg, #eaf6ff 65%, #c9eaff 100%);
  border-radius: 2.2rem;
  padding: 13px 13px 13px 13px;
  box-shadow: 0 8px 40px #0094ff16;
  min-width: 130px;
  max-width: 410px;
}

.split-innovation-video {
  display: block;
  border-radius: 1.4rem;
  box-shadow: 0 3px 18px #2196f319;
  width: 292px;
  max-width: 38vw;
  min-width: 120px;
  min-height: 85px;
  background: #000;
}

@media (max-width: 900px) {
  .split-innovation-block {
    flex-direction: column;
    align-items: stretch;
    padding: 1.5rem 0.6rem 1.3rem 0.7rem;
    gap: 1.6rem;
    min-height: 0;
  }
  .split-innovation-stripe {
    height: 6px;
    min-width: 30vw;
    width: 100vw;
    border-radius: 10px;
    margin-bottom: 22px;
    margin-left: 0;
    margin-right: 0;
    animation: stripeAppearX 1.2s cubic-bezier(.6,0,.39,1.34);
  }
  @keyframes stripeAppearX {
    from { width: 0; opacity: 0.1;}
    to   { width: 100vw; opacity: 1;}
  }
  .split-innovation-header { gap: 0.8rem; }
  .split-innovation-video-wrap { margin-left: 0; }
  .split-innovation-video { width: 98vw; max-width: 100vw; }
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
  </style>