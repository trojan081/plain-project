<template>
  <div class="loading">
    <div class="loading-wide">
      <div class="l1 color"></div>
      <div class="l2 color"></div>
      <div class="e1 color animation-effect-light"></div>
      <div class="e2 color animation-effect-light-d"></div>
      <div class="e3 animation-effect-rot">X</div>
      <div class="e4 color animation-effect-light"></div>
      <div class="e5 color animation-effect-light-d"></div>
      <div class="e6 animation-effect-scale">∑</div>
      <!-- <div class="e7 color"></div> -->
      <!-- <div class="e8 color"></div> -->
    </div>
  </div>
</template>

<style scoped>
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
}

.loading-wide {
  width: 150px;
  height: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

/* Цвета под CAD-стиль */
.color {
  background-color: #4b4e6d; /* тёмно-синий */
}

.l1 {
  width: 15px;
  height: 65px;
  position: absolute;
  animation: move-h 5.2s infinite cubic-bezier(0.65, 0.05, 0.36, 1);
  background-color: #d6101079; /* фиолетовый */
}

.l2 {
  width: 15px;
  height: 60px;
  position: absolute;
  transform: rotate(90deg);
  animation: move-v 5.2s infinite cubic-bezier(0.65, 0.05, 0.36, 1);
  background-color: #1f1f1f; /* чёрный */
}

@keyframes move-h {
  0% { top: 0; opacity: 0; }
  25% { opacity: 1; }
  50% { top: 30%; opacity: 1; }
  75% { opacity: 1; }
  100% { top: 100%; opacity: 0; }
}

@keyframes move-v {
  0% { left: 0; opacity: 0; }
  25% { opacity: 1; }
  50% { left: 45%; opacity: 1; }
  75% { opacity: 1; }
  100% { left: 100%; opacity: 0; }
}

.animation-effect-light {
  animation: effect 5.2s 5.1s infinite linear;
}

.animation-effect-light-d {
  animation: effect 5.3s 5.2s infinite linear;
}

.animation-effect-rot {
  animation: rot 5.8s infinite cubic-bezier(0.65, 0.05, 0.36, 1);
}

.animation-effect-scale {
  animation: scale 5.8s infinite cubic-bezier(0.65, 0.05, 0.36, 1);
}

@keyframes effect {
  0%, 100% { opacity: 0; }
  50% { opacity: 1; }
}

@keyframes rot {
  0% { transform: rotate(0deg); }
  50% { transform: rotate(180deg); }
  100% { transform: rotate(360deg); }
}

@keyframes scale {
  0% { scale: 1; }
  50% { scale: 1.5; }
  100% { scale: 1; }
}

.e1 {
  width: 1px;
  height: 40px;
  opacity: 0.3;
  position: absolute;
  top: 0;
  left: 8%;
  background-color: #6667ab; /* светло-фиолетовый */
}

.e2 {
  width: 60px;
  height: 1px;
  opacity: 0.8;
  position: absolute;
  top: 8%;
  left: 0;
  background-color: #2d2f44;
}

.e3 {
  position: absolute;
  top: 10%;
  left: 12%;
  font-family: "Courier New", Courier, monospace;
  font-weight: 900;
  font-size: 18px;
  color: #929292;
}

.e4 {
  width: 1px;
  height: 40px;
  opacity: 0.9;
  position: absolute;
  top: 90%;
  right: 10%;
  background-color: #333;
}

.e5 {
  width: 40px;
  height: 1px;
  opacity: 0.4;
  position: absolute;
  top: 100%;
  right: 0;
  background-color: #4b4e6d;
}

.e6 {
  position: absolute;
  top: 100%;
  right: 0;
  font-family: "Courier New", Courier, monospace;
  font-size: 26px;
  color: #b1b1b1;
}

.e7 {
  width: 1px;
  height: 20px;
  position: absolute;
  bottom: 0;
  left: 0;
  transform: rotate(45deg);
  animation: height 1.6s infinite cubic-bezier(0.65, 0.05, 0.36, 1);
  background-color: #222;
}

@keyframes height {
  0% { bottom: 0%; left: 0%; height: 0px; }
  25% { height: 80px; }
  50% { bottom: 100%; left: 100%; height: 80px; }
  75% { height: 0px; }
  100% { bottom: 0%; left: 0%; height: 0px; }
}

.e8 {
  width: 20px;
  height: 1px;
  position: absolute;
  bottom: 50%;
  left: 0;
  animation: width 5.5s infinite cubic-bezier(0.65, 0.05, 0.36, 1);
  background-color: #6a5acd;
}

@keyframes width {
  0% { left: 0%; width: 0px; }
  50% { left: 100%; width: 90px; }
  100% { left: 0%; width: 0px; }
}
</style>
