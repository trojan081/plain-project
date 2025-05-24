<template>

  <div class="roadmap-header-wrap">
  <div class="roadmap-block">

    <h2
      class="roadmap-title"
      :class="{ shown: showTitle }"
      @mouseenter="hoverTitle = true"
      @mouseleave="hoverTitle = false"
    >
    </h2>
  </div>
    <svg :viewBox="'0 0 630 1600'" width="3950" height="3000" class="road-svg">
      <defs>
        <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="12" result="coloredBlur"/>
          <feMerge>
            <feMergeNode in="coloredBlur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>
      <!-- Тень и дорога -->
      <path :d="roadPath" stroke="#222" stroke-width="44" fill="none" opacity="1.14" filter="url(#glow)" />
      <path :d="roadPath" stroke="#555657" stroke-width="32" fill="none" stroke-linecap="round" />
      <path :d="roadPath" stroke="#FFD600" stroke-width="3" fill="none" stroke-dasharray="18 30" stroke-linecap="round" opacity="0.97" />
      <!-- <path :d="segmentPath" stroke="#aabfe3" stroke-width="3" fill="none" stroke-dasharray="9 10" stroke-linecap="round" opacity="0.97" /> -->
      <!-- Этапы -->

      <g v-for="(p, idx) in points" :key="idx" class="roadmap-point-group">
        <!-- Внешнее мягкое свечение (пульсация) -->
        <circle
          :cx="p.x"
          :cy="p.y"
          :r="pointStyles.glowRadius"
          :class="['pulse-glow', {active: activeIndex === idx}]"
        />
        <!-- Чёткий контур (пульсация) -->
        <circle
          :cx="p.x"
          :cy="p.y"
          :r="pointStyles.outlineRadius"
          :class="['pulse-outline', {active: activeIndex === idx}]"
        />
        <!-- Основной кружок -->
        <circle
          :cx="p.x"
          :cy="p.y"
          :r="pointStyles.dotRadius"
          :fill="pointStyles.fill"
          :stroke="activeIndex === idx ? pointStyles.activeStroke : pointStyles.stroke"
          :stroke-width="pointStyles.strokeWidth"
          class="main-dot"
          :class="{active: activeIndex === idx}"
          @mouseenter="hover(idx)"
          @mouseleave="hover(null)"
        />
        <g v-for="(img, idx) in roadmapImages" :key="idx">
          <image
            :href="img.href"
            :x="img.x"
            :y="img.y"
            :width="img.width"
            :height="img.height"
            :class="{ 'img-hovered': hoveredImageIdx === idx }"
            @mouseenter="hoveredImageIdx = idx"
            @mouseleave="hoveredImageIdx = null"
          />
          <text
            v-if="hoveredImageIdx === idx"
            :x="img.labelX"
            :y="img.labelY"
            text-anchor="middle"
            class="image-label typewriter"
          >
            <tspan
              v-for="(char, i) in img.label.split('')"
              :key="i"
              :class="['typewriter-char', { visible: typewriterIdx >= i }]"
            >{{ char }}</tspan>
          </text>
        </g>
        <!-- Надпись -->
        <foreignObject
          :x="p.x + labelOffsets[idx].x"
          :y="p.y + labelOffsets[idx].y"
          class="fade-label"
          :width="labelWidths[idx]?.width || 'auto'"
          height="74"
        >
        <div
          class="point-label"
          :class="{active: activeIndex === idx}"
          ref="labelElements"
          @mouseenter="hover(idx)"
          @mouseleave="hover(null)"
        >
            <div class="label-title">{{ p.label }}</div>
            <div class="label-desc">{{ p.desc }}</div>
          </div>
        </foreignObject>
      </g>
    </svg>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';

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
        label: 'Расчёт объёмов',
        labelX: 660,
        labelY: 471,
        width: 90,
        height: 90,
      },
      {
        href: '/assets/cad3.jpg',
        x: 342,
        y: 573,
        label: 'Создание модели',
        labelX: 600,
        labelY: 630,
        width: 90,
        height: 90,
      },
      {
        href: '/assets/cad5.jpg',
        x: -222,
        y: 780,
        label: 'Генерация данных',
        labelX: -390,
        labelY: 831,
        width: 90,
        height: 90,
      },
      {
        href: '/assets/cad7.jpg',
        x: -240,
        y: 960,
        label: 'ВП',
        labelX: -282,
        labelY: 1011,
        width: 90,
        height: 90,
      },
      {
        href: '/assets/cad8.jpg',
        x: -120,
        y: 1110,
        label: 'ПЗМ',
        labelX: -180,
        labelY: 1170,
        width: 90,
        height: 90,
      },
    ]

const hoveredImageIdx = ref(null)
const typewriterIdx = ref(-1)
let typewriterTimer = null

watch(hoveredImageIdx, (val) => {
  clearInterval(typewriterTimer)
  typewriterIdx.value = -1
  if (val !== null) {
    typewriterTimer = setInterval(() => {
      typewriterIdx.value++
      if (typewriterIdx.value >= roadmapImages[val].label.length - 1) {
        clearInterval(typewriterTimer)
      }
    }, 15)
  }
})

const labelElements = ref([]);
const labelWidths = ref([]);
const image1Hovered = ref(false);
const image2Hovered = ref(false);
const image3Hovered = ref(false);
const image4Hovered = ref(false);
const image5Hovered = ref(false);
const image6Hovered = ref(false);
const roadPath = `
  M70,60
  L70,220
  Q70,320 190,320
  A60,60 0 0 1 200,600
  Q160,600 130,580
  Q50,533 10,600
  Q0,620 2,660
  L2,750
  Q5,800 -25,840
  Q-90,950 0,1030
  Q40,1060 80,1060
  L160,1060
  Q230,1060 230,1120
  L230,1410
  `
;
const segmentPath = `
  M200,290
  L200,210
  M200,210
  A60,60 0 0 1 220,720
  Q150,720 100,700
  L150,620
  `
;
const showTitle = ref(false)
const hoverTitle = ref(false)
onMounted(() => {
  labelWidths.value = labelElements.value.map(el => ({
    width: el.offsetWidth + 32 // Добавляем padding
  }));
  setTimeout(() => showTitle.value = true, 200)
});
const points = [
  { x: 70, y: 60, label: 'Старт', desc: 'IV кв. 2024' },
  { x: 2, y: 630, label: 'Тестирование', desc: 'II кв. 2025' },
  { x: 80, y: 1060, label: 'Запуск MVP', desc: 'III кв. 2025' },
  { x: 230, y: 1200, label: 'Доработка', desc: 'IV кв. 2025' },
  { x: 230, y: 1410, label: 'Final version', desc: 'I кв. 2026' }
];

const labelOffsets = [
  { x: 44, y: -45 },
  { x: -360, y: -51 },
  { x: 18, y: -171 },
  { x: 54, y: -45 },
  { x: -150, y: 60 }
];

// --- Стили точек — легко кастомизируются! ---
const pointStyles = {
  glowRadius: 51,
  outlineRadius: 27,
  dotRadius: 21,
  fill: '#fff',
  stroke: '#000000',
  activeStroke: '#0044ff77;',
  strokeWidth: 5
};

const activeIndex = ref(null);
const hover = idx => activeIndex.value = idx;
</script>

<style scoped>
.roadmap-block {
  border-radius: 2.2rem;
  margin-left: 18%;
  padding: 2.2rem 1rem 2rem 1rem;
  width: 1420px;
  overflow: auto;
  position: relative;
  /* background: linear-gradient(127deg, #222 0%, #191919 100%);
  box-shadow: 0 4px 48px #FFD60021; */
}
.road-svg {
  display: block;
  margin-left: 10%;
  width: 100%;
  max-width: 1900px;
  height: 900px;
  min-height: 650px;
  background: none;
}

/* ----------- ЭФФЕКТЫ ДЛЯ ТОЧЕК ----------- */
.pulse-glow {
  fill: #0044ff77;
  filter: blur(6px);
  opacity: 0.75;
  animation: pulse-glow 2.7s infinite;
  pointer-events: none;
  transition: opacity 0.25s;
}
.pulse-glow.active {
  opacity: 1;
  animation-duration: 1.3s;
}
@keyframes pulse-glow {
  0% { r: 40; opacity: 0.7; }
  50% { r: 54; opacity: 0.15; }
  100% { r: 40; opacity: 0.7; }
}
.pulse-outline {
  fill: none;
  stroke: #003cff;
  stroke-width: 6;
  opacity: 0.54;
  animation: pulse-outline 1.4s infinite cubic-bezier(.7,0,.29,1.05);
  pointer-events: none;
  transition: opacity 0.22s;
}
.pulse-outline.active {
  opacity: 1;
  stroke: #3b82f6;
}
@keyframes pulse-outline {
  0% { r: 29; opacity: 0.48; }
  80% { r: 39; opacity: 0.14; }
  100% { r: 29; opacity: 0.48; }
}

.main-dot {
  cursor: pointer;
  transition: fill 0.17s, stroke 0.22s, r 0.19s;
  filter: drop-shadow(0 1px 8px #FFD60022);
}
.main-dot.active,
.main-dot:hover {
  fill: rgb(238, 254, 255);
  stroke: #3b82f6;
  r: 24;
}

/* ----------- ЭФФЕКТЫ ДЛЯ НАДПИСЕЙ ----------- */
.fade-label {
  /* pointer-events: none; */
  overflow: visible;
  cursor: pointer;
}
.point-label {
  min-width: 240px;
  max-width: 300px;
  padding: 14px 18px 12px 15px;
  border-radius: 24px;
  background: #dbe8f05e;
  box-shadow: 0 8px 28px #2600ff17, 0 1px 4px #a5964921;
  color: #fff;
  font-size: 1.06rem;
  font-weight: 500;
  border: 2.3px solid #0066ff;
  opacity: 0.99;
  /* --- эффект свечения всегда --- */
  text-shadow: 0 1px 8px #FFD60033, 0 1px 2px #19191988;
  transition: 
    box-shadow 0.3s cubic-bezier(.7,0,.29,1.05),
    background 0.25s cubic-bezier(.7,0,.29,1.05),
    border 0.25s,
    transform 0.32s cubic-bezier(.73,-0.19,.41,1.25);
}
.point-label .label-title {
  font-weight: 800;
  color: #aa2929;
  font-size: 2.1rem;
  margin-bottom: 0.22em;
  letter-spacing: 0.03em;
  text-shadow: 0 1px 8px #FFD60033;
  filter: drop-shadow(0 1px 2px #fff2);
}
.point-label .label-desc {
  color: #000000;
  font-size: 1.5rem;
  opacity: 0.84;
  text-shadow: 0 1px 2px #FFD60018;
}
/* -- эффект наводки на кружок -- */
.point-label.active {
  background: #f0dbe65e;
  box-shadow: 0 10px 32px #0925c255, 0 1.5px 5px #d3121228;
  border: 2.8px solid rgb(83, 15, 160);
  transform: scale(1.08) translateY(-9px);
  opacity: 1;
  z-index: 3;
  transition: 
    box-shadow 0.19s cubic-bezier(.7,0,.29,1.05),
    background 0.19s,
    border 0.22s,
    transform 0.17s cubic-bezier(.53,0,.36,1.38);
}
.point-label.active .label-title {
  color: #ff0000;
  transition: color 0.22s, text-shadow 0.25s;
}
/* --- Мобильная адаптация --- */
@media (max-width: 600px) {
  .roadmap-block {
    width: 97vw;
    padding: 1.1rem 0.3rem 1.4rem 0.3rem;
    border-radius: 1.1rem;
  }
  .road-svg { max-width: 99vw; height: 540px; min-height: 320px; }
  .point-label { font-size: 0.93rem; max-width: 423px; }
  .point-label .label-title {
  font-size: 3.3rem;
}
  .point-label .label-desc {
  font-size: 1.5rem;
}
}
@media (max-width: 1200px) {
  .roadmap-block {
    max-width: 99vw;
    padding: 1.2rem 0.3rem 1.4rem 0.3rem;
    border-radius: 1.1rem;
  }
  .road-svg { width: 100vw; min-width: 270px; max-width: 99vw; height: 93vw; min-height: 420px; }
  .point-label { 
    font-size: 0.93rem; 
    max-width: 240px; 
    min-width: 240px;
  }  
  .point-label .label-title {
  font-size: 3.3rem;
}
  .point-label .label-desc {
  font-size: 2.4rem;
}
}
@media (max-width: 600px) {
  .roadmap-block {
    padding: 0.7rem 0.1rem 0.8rem 0.1rem;
    
  }
  .road-svg { min-height: 300px; }
  .point-label { 
    font-size: 0.77rem; 
    max-width: 498vw; 
    min-width: 390px;
  }
    .point-label .label-title {
  font-size: 3.3rem;
}
}

/* From Uiverse.io by Cornerstone-04 */ 
.cards {
  perspective: 500px;
}

.card {
  width: 300px;
  height: 250px;
  background: #cacaca4b;
  border: 2px solid #555555;
  border-radius: 4px;
  position: relative;
  transform-style: preserve-3d;
  will-change: transform;
  transition: transform 1.5s;
}

.card:hover {
  transform: translateZ(3px) rotateX(12deg) rotateY(1deg);
}

.card_title {
  color: #fff;
  position: absolute;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
  transition: transform .5s;
  font: 700 1.5rem monospace;
  text-shadow: -1px -1px 0 #000,  
    1px -1px 0 #000,
    -1px 1px 0 #000,
     1px 1px 0 #000;
}

.card:hover .card_title {
  transform: translateZ(50px);
}

.img-hovered {
  filter: drop-shadow(0 0 4px #b6ade05b) brightness(1.2);
  transition: filter 0.4s;
  border-radius: 24px;
}

.image-label {
  font-size: 1.8em;
  font-family: 'Montserrat', sans-serif;
  user-select: none;
  letter-spacing: 0.03em;
}
.typewriter-char {
  opacity: 0;
  transition: opacity 0.12s;
}
.typewriter-char.visible {
  opacity: 1;
}
.image-label.typewriter {
  font-size: 1.8em;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: 400; 
  letter-spacing: 0.01em;
  user-select: none;
  fill: #222;
}
</style>