import { createI18n } from 'vue-i18n'

const messages = {
  en: {
    headerTitle: "The Future",
    headerSubtitle: "is Now",
    content: {
      hiddenTitle: "Hidden Content",
      hiddenText: "This is the text that will be visible after the 'gates' open.",
      whatWeDo: "What do we do?",
      // Добавьте остальные переводы по аналогии
    }
  },
  ru: {
    headerTitle: "The Future",
    headerSubtitle: "is Now",
    content: {
      hiddenTitle: "",
      hiddenText: "Здесь находится текст, который будет виден после того, как «ворота» разъедутся.",
      whatWeDo: "Что мы делаем?",
      // Остальные русские переводы
    }
  }
}

export default createI18n({
  legacy: false,
  locale: 'ru',
  fallbackLocale: 'en',
  messages
})