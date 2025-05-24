<template>
  <div class="p-6 space-y-8">
    <!-- 1. Общая информация о проекте -->
    <section>
      <h2 class="text-2xl font-semibold mb-4">Информация о проекте</h2>
      <div class="grid grid-cols-2 gap-4">
        <div><strong>Версия:</strong> {{ project.version }}</div>
        <div><strong>Локация:</strong> {{ project.location }}</div>
        <div><strong>Площадь:</strong> {{ project.area }} м²</div>
        <div><strong>Документ:</strong> {{ project.regulation }}</div>
        <div class="col-span-2">
          <strong>Описание:</strong>
          <p class="mt-1">{{ project.description }}</p>
        </div>
        <div><strong>Проектировщик:</strong> {{ project.designer.name }}</div>
      </div>
    </section>

    <!-- 2. Блок согласований -->
    <section>
      <h2 class="text-2xl font-semibold mb-4">Согласования</h2>
      <table class="min-w-full border">
        <thead>
          <tr class="bg-gray-100">
            <th class="p-2 text-left">Регулятор</th>
            <th class="p-2 text-left">Статус</th>
            <th class="p-2 text-left">Дата</th>
            <th class="p-2 text-left">Файл</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in approvals" :key="item.id" class="border-t">
            <td class="p-2">{{ item.regulator }}</td>
            <td class="p-2">{{ item.status }}</td>
            <td class="p-2">{{ formatDate(item.date) }}</td>
            <td class="p-2">
              <a :href="item.fileUrl" target="_blank" class="text-blue-600 underline">Скачать</a>
            </td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- 3. Конструкции дорожных одежд -->
    <section>
      <h2 class="text-2xl font-semibold mb-4">Конструкции дорожных одежд (КДО)</h2>
      <div v-for="cdo in cdoList" :key="cdo.id" class="mb-4 p-4 border rounded-lg">
        <div><strong>Тип:</strong> {{ cdo.type }}</div>
        <div><strong>Дата изменения:</strong> {{ formatDate(cdo.modifiedAt) }}</div>
        <div class="mt-2">
          <strong>Описание конструкции:</strong>
          <p class="whitespace-pre-wrap">{{ describeCDO(cdo.spec) }}</p>
        </div>
      </div>
    </section>

    <!-- 4. Жизненный цикл проекта -->
    <section>
      <h2 class="text-2xl font-semibold mb-4">Жизненный цикл проекта</h2>
      <table class="min-w-full border">
        <thead>
          <tr class="bg-gray-100">
            <th class="p-2 text-left">Версия</th>
            <th class="p-2 text-left">Дата</th>
            <th class="p-2 text-left">Автор</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="event in lifecycle" :key="event.id" class="border-t">
            <td class="p-2">{{ event.version }}</td>
            <td class="p-2">{{ formatDate(event.date) }}</td>
            <td class="p-2">{{ event.user.name }}</td>
          </tr>
        </tbody>
        <tfoot>
          <tr class="bg-gray-50 font-semibold">
            <td class="p-2" colspan="3">Всего итераций: {{ lifecycle.length }}</td>
          </tr>
        </tfoot>
      </table>
    </section>

    <!-- 5. Графическая статистика -->
    <section>
      <h2 class="text-2xl font-semibold mb-4">Статистика изменений</h2>
      <BarChart :chart-data="chartData" :chart-options="chartOptions" />
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend)

// Оборачиваем Bar в компонент
const BarChart = {
  extends: Bar,
  props: ['chartData', 'chartOptions'],
  mounted() {
    this.renderChart(this.chartData, this.chartOptions)
  },
  watch: {
    chartData() {
      this.renderChart(this.chartData, this.chartOptions)
    }
  }
}

const project = ref({})
const approvals = ref([])
const cdoList = ref([])
const lifecycle = ref([])

onMounted(async () => {
  const projectId = /* получаем из route, напр. useRoute().params.id */ 1
  const { data } = await axios.get(`/api/projects/${projectId}`)
  project.value = data.project
  approvals.value = data.approvals
  cdoList.value = data.cdo
  lifecycle.value = data.lifecycle
})

// Форматирование даты
const formatDate = (iso) => new Date(iso).toLocaleDateString('ru-RU')

// Преобразуем JSON-спецификацию CDO в человекочитаемый текст
const describeCDO = (spec) => {
  // spec — это объект или массив из JSONB
  // Пример простой трансформации:
  if (Array.isArray(spec.layers)) {
    return spec.layers.map(l => 
      `Слой ${l.layer_number}: ${l.material}, толщина ${l.thickness}`
    ).join('\n')
  }
  return JSON.stringify(spec, null, 2)
}

// Данные для графика: количество изменений по авторам
const chartData = computed(() => {
  const counts = {}
  lifecycle.value.forEach(ev => {
    const name = ev.user.name
    counts[name] = (counts[name] || 0) + 1
  })
  return {
    labels: Object.keys(counts),
    datasets: [{
      label: 'Изменения',
      data: Object.values(counts),
      backgroundColor: '#3b82f6' // можно убрать цвет, Chart.js подберет по умолчанию
    }]
  }
})
const chartOptions = {
  responsive: true,
  plugins: {
    legend: { display: false }
  }
}
</script>

<style scoped>
/* любые дополнительные стили */
</style>
