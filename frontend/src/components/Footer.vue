<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-grid">
        <!-- Левая колонка -->
        <div class="footer-left">
          <div class="footer-header">Документы</div>
          <nav class="footer-links">
            <a href="http://localhost:3000/policy" class="footer-link">Политика конфиденциальности</a>
            <a href="http://localhost:3000/offer" class="footer-link">Публичная оферта</a>
            <a href="http://localhost:3000/main_agreement" class="footer-link">Согласие на обработку ПД</a>
            <a href="http://localhost:3000/agreement" class="footer-link">Согласие на получение рассылок</a>
          </nav>
          <div class="footer-contacts">
            Наши контакты: <a href="mailto:support@plain-project.ru" class="footer-link">support@plain-project.ru</a>
          </div>
        </div>
        <!-- Правая колонка -->
        <div class="footer-right">
          <div class="footer-desc">
            Проект выполнен при поддержке Фонда Содействия Инновациям федерального проекта "Платформа университетского
            технологического предпринимательства"
          </div>
          <div class="footer-logos">
            <img class="fasie_logo" src="../assets/fasie_logo.png" alt="FASIE Logo" />
            <img class="uni_platform_logo" src="../assets/uni_platform_logo.png" alt="UNI Logo" />
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; {{ new Date().getFullYear() }} Plain. Все права защищены.
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: #181d21;
  color: #e6e6e6;
  width: auto;
  margin-top: auto;
  box-sizing: border-box;
  padding-top: 2rem;
}
.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2vw 1.2rem 2vw;
  box-sizing: border-box;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem 2rem;
  align-items: flex-start;
}

.footer-left {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1em;
  text-align: left;
}

.footer-header {
  font-weight: 700;
  font-size: 1.11em;
  margin-bottom: 0.2em;
  color: #ffffff;
  letter-spacing: 0.01em;
  text-align: center;
}

.footer-links {
  display: flex;
  flex-direction: column;
  gap: 0.4em;
}

.footer-link {
  color: #e6e6e6;
  text-decoration: none;
  font-size: 1em;
  transition: color 0.2s;
  word-break: break-word;
}
.footer-link:hover {
  color: #ff6a3e;
  text-decoration: underline;
}
.footer-contacts {
  margin-top: 0.8em;
  color: #aaa;
  font-size: 0.97em;
}

.footer-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 1.2em;
  min-width: 210px;
}

.footer-desc {
  color: #cacaca;
  font-size: 1em;
  text-align: center;
  line-height: 1.4;
  max-width: 420px;
}

.footer-logos {
  display: grid;
  grid-template-columns: repeat(2, auto);
  align-items: center;
  gap: 1.1em;
  margin-top: 0.4em;
  margin-right: 24%;
}

.fasie_logo,
.uni_platform_logo {
  height: clamp(28px, 6vw, 48px);
  max-width: 110px;
  object-fit: contain;
  background: #fff;
  border-radius: 7px;
  padding: 0.1em 0.4em;
  box-shadow: 0 2px 14px #0002;
}

/* Линия и копирайт */
.footer-bottom {
  width: 100%;
  text-align: center;
  color: #a5a5a5;
  font-size: 0.96em;
  margin-top: 2.2em;
  padding-top: 1em;
  border-top: 1px solid #222;
  letter-spacing: 0.01em;
}

/* Мобильная и планшетная версия */
@media (max-width: 900px) {
  .footer-container {
    padding: 0 1vw 1rem 1vw;
  }
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 2em 0;
  }
  .footer-left,
  .footer-right {
    align-items: left !important;
    text-align: left !important;
    min-width: unset;
    max-width: 98vw;
  }
  .footer-desc {
    margin: 0 auto;
    text-align: center !important;
    max-width: 99vw;
  }
  .footer-logos {
    justify-content: center;
    margin-bottom: 1em;
    margin-right: 35%;
  }
  .footer-bottom {
    margin-top: 1em;
    font-size: 0.93em;
  }
}
@media (max-width: 600px) {
  .footer-container {
    padding: 0 0.2em 0.8em 0.2em;
  }
  .footer-links {
    font-size: 0.98em;
  }
  .footer-bottom {
    font-size: 0.9em;
  }
  .footer-header {
    font-size: 1em;
    text-align: center;
  }
}
</style>
