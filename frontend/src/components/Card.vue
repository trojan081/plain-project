<template>
  <div class="container">
    <div class="box" v-for="(item, index) in suitableForItems" :key="index">
      <img :src="item.imgSrc" alt="Подходит" class="suitable-for-img" />
      <div class="text">
        <h1>{{ item.title }}</h1>
        <ul class="suitable_for_list">
          <li v-for="(desc, i) in item.description" :key="i">{{ desc }}</li>
        </ul>
      </div>
    </div>

    <!-- Optional References -->
    <div class="cs-ref">
      <a
        class="cs-dribbble"
        href="https://dribbble.com/shots/9300772-Neumorphism-UI-Card"
        target="_blank"
        title="Dribbble shot"
      >
        <div id="svgDribbble"></div>
      </a>
      <a
        class="cs-twitter"
        target="_blank"
        href="https://twitter.com/CosWiSe"
        title="Twitter"
      >
        <div id="svgTwitter"></div>
      </a>
    </div>
  </div>
</template>

<script setup>

import img1 from '/assets/for_whom_1_2.jpg'
import img2 from '/assets/for_whom_2_3.jpg'
import img3 from '/assets/for_whom_3.jpg'
import img4 from '/assets/for_whom_4.jpg'

const suitableForItems = [
  {
    imgSrc: img1,
    title: 'Инженерам генплана',
    description: ['Скорость разработки ПД', 'Простота изменений', 'Минимизация ошибок']
  },
  {
    imgSrc: img2,
    title: 'Владельцам бизнеса',
    description: ['Оптимизация процессов', 'Новейшие технологии ИИ', 'Преимущества на рынке']
  },
  {
    imgSrc: img3,
    title: 'Руководителям',
    description: ['Расчёт KPI команды', 'Соблюдение сроков', 'Полный контроль задач']
  },
  {
    imgSrc: img4,
    title: 'Фрилансерам',
    description: ['Больше заказов', 'Высокая эффективность', 'Надёжность и репутация']
  }
]

</script>


<style scoped>
/* Импорт шрифта вынести в index.html или App.vue, но можно оставить тут: */
@import url('https://fonts.googleapis.com/css?family=Muli:300,400,700,900');

/* Цвета из SCSS */
:root {
  --mainC: #f1f3f6;
  --secC: #9dabc0;
  --svgC: rgba(146, 156, 208, 0.8);
  --sz: 300px;
}

/* Базовые стили */
html, body {
  background: var(--mainC);
  font-family: 'Muli', sans-serif;
  color: rgba(51, 51, 51, 1);
}

.container {
  width: 100%;
  height: 97vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: var(--sz);
  height: calc(var(--sz) * 1.4);
  background: var(--mainC);
  border-radius: 20px;
  box-shadow:
    inset 0 0 15px rgba(55, 84, 170, 0),
    inset 0 0 20px rgba(255, 255, 255, 0),
    7px 7px 15px rgba(55, 84, 170, 0.15),
    -7px -7px 20px rgba(255, 255, 255, 1),
    inset 0px 0px 4px rgba(255, 255, 255, 0.2);
}

.text {
  width: 80%;
  height: auto;
}
.text h1 {
  font-size: 1.5em;
  font-weight: 600;
}
.text p {
  margin-top: 2em;
  line-height: 1.45em;
}

.btn {
  margin-top: 2em;
  margin-bottom: 2em;
  display: flex;
  flex-direction: column;
}
.cta {
  width: 100px;
  height: 33px;
  text-decoration: none;
  background: var(--secC);
  color: #fff;
  padding: 10px 63px;
  border-radius: 25px;
  font-weight: 600;
  box-shadow: 0px 10px 15px rgba(55, 84, 170, 0.25);
  display: inline-block;
  text-align: center;
  line-height: 33px;
}

.tooltip {
  position: relative;
  display: inline-block;
}

.tooltip .tooltiptext {
  display: flex;
  justify-content: center;
  align-items: center;
  visibility: hidden;
  width: 120px;
  background-color: #333;
  color: #fff;
  text-align: center;
  border-radius: 25px;
  padding: 5px 0 6px 0;
  position: absolute;
  top: -40px;
  left: calc(50% - 60px);
  z-index: 1;
  font-size: 0.7em;
  opacity: 0;
  box-sizing: border-box;
  transition: opacity 399ms ease;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}

/* SVG refs (можешь вставить SVG или убрать если не нужны) */
.cs-ref {
  display: flex;
  gap: 1em;
  position: absolute;
  bottom: 2vw;
  right: 2vw;
}
#svgDribbble,
#svgTwitter {
  width: 24px;
  height: 24px;
  background: var(--svgC);
  border-radius: 50%;
  opacity: 0.3;
}

.box {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 320px;
  padding: 1.5rem;
  margin: 1rem;
  background: var(--mainC);
  border-radius: 20px;
  box-shadow:
    inset 0 0 15px rgba(55, 84, 170, 0),
    inset 0 0 20px rgba(255, 255, 255, 0),
    7px 7px 15px rgba(55, 84, 170, 0.15),
    -7px -7px 20px rgba(255, 255, 255, 1),
    inset 0px 0px 4px rgba(255, 255, 255, 0.2);
  text-align: center;
}

.suitable-for-img {
  width: 74%;
  border-radius: 12px;
  margin-bottom: 1rem;
  object-fit: cover;
  max-height: 200px;
}

.suitable_for_list {
  padding-left: 1.2em;
  text-align: left;
  margin-top: 1em;
}

</style>
