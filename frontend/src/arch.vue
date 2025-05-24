
<template>
    <div class="scroll-compensator">
      <div>
        <div 
          class="header" 
          :style="{ 
            filter: `blur(${blurValue}px)`, 
            backgroundImage: 'url(/assets/h2.png)'
          }"
        >
          <h1 class="title-left" :class="{ visible: showTitle }">The Future</h1>
          <h2 class="title-right" :class="{ visible: showSubtitle }">is Now</h2>
        </div>
        <div class="gates-container" ref="gatesContainer">
          <div class="gate gate-left" ref="gateLeft"></div>
          <div class="gate gate-right" ref="gateRight"></div>
          <div class="gate-text" ref="gateText">P L A I N</div>
  
          <div class="content-after-gates" ref="contentAfterGates">
            <p>Новое слово в проектировании</p>
          </div>
        </div>
  
        <hr class="hr-0" />
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
          <p class="text-h1">Что мы делаем?</p>
        </div>
  
        <div class="content-row">
          <div class="text-v-2-Container">
            <p class="text-v-2">
              Внедряем новейшие технологии в процессы благоустройства
              современной городской среды
            </p>
          </div>
  
          <div class="video-container">
            <video loop autoplay muted playsinline class="background-video">
              <source src="./assets/videos/v1.mp4" type="video/mp4" />
              Ваш браузер не поддерживает видео.
            </video>
          </div>
        </div>
  
        <div class="content-row">
          <div class="video-container">
            <video loop autoplay muted playsinline class="background-video">
              <source src="./assets/videos/v3.mp4" type="video/mp4" />
              Ваш браузер не поддерживает видео.
            </video>
          </div>
  
          <div class="text-v-1-Container">
            <p class="text-v-1">
              Выводим качество и скорость выполнения проектов на новый уровень
            </p>
          </div>
        </div>
  
        <div class="content-row">
          <div class="text-v-1-Container">
            <p class="text-v-2">
              Даем возможность получить преимущества перед конкурентами
            </p>
          </div>
  
          <div class="video-container">
            <video loop autoplay muted playsinline class="background-video">
              <source src="./assets/videos/v5.mp4" type="video/mp4" />
              Ваш браузер не поддерживает видео.
            </video>
          </div>
        </div>
  
        <hr class="custom-hr" />
  
        <div class="text-2-container" ref="textContainer">
          <p class="text-h2">Зачем это нужно?</p>
        </div>
  
        <div class="columns-container" :class="{ 'visible': isSectionVisible }">
    <div class="left-column">
      <div
        v-for="(item, index) in l_column"
        :key="index"
        class="grid-item"
      >
        <img :src="item.imgSrc" />
        <p class="text_advantages"><b>{{ item.text }}</b></p>
      </div>
    </div>
  
    <div class="right-column">
      <div
        v-for="(item, index) in r_column"
        :key="index"
        class="grid-item"
      >
        <img :src="item.imgSrc" />
        <p class="text_advantages"><b>{{ item.text }}</b></p>
      </div>
    </div>
  </div>
  
        <hr class="custom-hr" />
  
        <div class="text-2-container" ref="textContainer">
          <p class="text-h2">Как начать?</p>
          <p class="text-common">Запишитесь на бесплатное тестирование, и вскоре мы с вами свяжемся :) Для этого напишите нам на электронную почту сообщение с пометкой "Тестирование": <span style="color:royalblue;">contact@plain-project.ru</span></p>
        </div>
      </div>
      <footer class="footer">
        <p>© 2025</p>
        <p>{{ $t('content.hiddenTitle') }}</p>
      </footer>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, onUnmounted } from 'vue';
  import { useI18n } from 'vue-i18n';
  export default {
    name: 'App',
    setup() {
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
      let startTouchY = 0;
      const l_column = ref([
      { imgSrc: './assets/k1.jpg', text: 'Скорость: забудьте про дедлайны' },
      { imgSrc: './assets/k2.jpg', text: 'Гибкость: исправляйте в один клик' },
      { imgSrc: './assets/kk33.jpg', text: 'Время: сосредоточьтесь на важном' }
      ])
      
      const r_column = ref([
      { imgSrc: './assets/kkkkk4.jpg', text: 'Автоматизация: делегируйте рутину' },
      { imgSrc: './assets/kkkk5.jpg', text: 'Технологии: точность чертежей до 99%' },
      { imgSrc: './assets/kk5.jpg', text: 'Расходы: сократите издержки'}
      ])
      const gatesContainer = ref(null)
      const gateLeft = ref(null)
      const gateRight = ref(null)
      const contentAfterGates = ref(null)
      const gatesProgress = ref(0)
      const areGatesOpened = ref(false)
      let isOpening = false;
  
      const handleTouchStart = (e) => {
        const touch = e.touches[0];
        // startTouchY = touch.clientY;
      };
  
      const handleTouchMove = (e) => {
        if (areGatesOpened.value) return;
        e.preventDefault();
        
        const touch = e.touches[0];
        const diffY = touch.clientY - startTouchY;
  
        gatesProgress.value += diffY * 0.01; //
        if (gatesProgress.value < 0) gatesProgress.value = 1;
        if (gatesProgress.value > 1) {
          gatesProgress.value = 1;
          areGatesOpened.value = true;
          document.body.style.overflow = 'auto';
        }
        
        updateGatesTransform(gatesProgress.value);
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
        const section = document.querySelector('.columns-container');
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
        setTimeout(() => (showTitle.value = true), 100);
        setTimeout(() => (showSubtitle.value = true), 300);
  
        window.addEventListener('scroll', handleScroll);
        window.addEventListener('wheel', handleWheel, { passive: false });
        window.addEventListener('touchstart', handleTouchStart, { passive: false });
        window.addEventListener('touchmove', handleTouchMove, { passive: false });
  
        updateGatesTransform();
  
        if (imgContainer.value) {
        imgObserver.observe(imgContainer.value)
          }
      });
  
      onUnmounted(() => {
        window.removeEventListener('scroll', handleScroll);
        window.removeEventListener('wheel', handleWheel, { passive: false });
        window.removeEventListener('touchstart', handleTouchStart, { passive: false });
        window.removeEventListener('touchmove', handleTouchMove, { passive: false });
        document.body.style.overflow = 'auto'; // Возвращаем стандартное поведение прокрутки
      });
  
      return {
        showTitle,
        showSubtitle,
        blurValue,
        isSectionVisible,
        isImgVisible,
        isSecondImgVisible,
        gateLeft,
        gateRight,
        contentAfterGates,
        imgContainer,
        r_column,
        l_column
      };
    },
  };
  </script>