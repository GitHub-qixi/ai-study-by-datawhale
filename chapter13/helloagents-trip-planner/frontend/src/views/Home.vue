<template>
  <div class="home-container">
    <!-- 背景摄影 -->
    <div class="hero-background">
      <div class="dark-overlay"></div>
    </div>

    <!-- 页面标题 - 全视口英雄区 -->
    <div class="hero-section full-viewport">
      <div class="hero-content">
        <h1 class="hero-title">智能旅行助手</h1>
        <p class="hero-subtitle">基于AI的个性化旅行规划,让每一次出行都完美无忧</p>
      </div>
      
      <!-- 滚动指示器 -->
      <div class="scroll-indicator">
        <div class="scroll-arrow"></div>
        <span class="scroll-text">向下滚动</span>
      </div>
    </div>

    <!-- 表单区域 -->
    <div class="form-section">
      <a-form
        :model="formData"
        layout="vertical"
        @finish="handleSubmit"
        class="space-form"
      >
        <!-- 第一步:目的地和日期 -->
        <div class="form-group">
          <div class="group-header">
            <span class="group-icon">📍</span>
            <span class="group-title">目的地与日期</span>
          </div>

          <a-row :gutter="24">
            <a-col :span="8">
              <a-form-item name="city" :rules="[{ required: true, message: '请输入目的地城市' }]">
                <template #label>
                  <span class="form-label">目的地城市</span>
                </template>
                <a-input
                  v-model:value="formData.city"
                  placeholder="例如: 北京"
                  size="large"
                  class="space-input"
                />
              </a-form-item>
            </a-col>
            <a-col :span="6">
              <a-form-item name="start_date" :rules="[{ required: true, message: '请选择开始日期' }]">
                <template #label>
                  <span class="form-label">开始日期</span>
                </template>
                <a-date-picker
                  v-model:value="formData.start_date"
                  style="width: 100%"
                  size="large"
                  class="space-input"
                  placeholder="选择日期"
                />
              </a-form-item>
            </a-col>
            <a-col :span="6">
              <a-form-item name="end_date" :rules="[{ required: true, message: '请选择结束日期' }]">
                <template #label>
                  <span class="form-label">结束日期</span>
                </template>
                <a-date-picker
                  v-model:value="formData.end_date"
                  style="width: 100%"
                  size="large"
                  class="space-input"
                  placeholder="选择日期"
                />
              </a-form-item>
            </a-col>
            <a-col :span="4">
              <a-form-item>
                <template #label>
                  <span class="form-label">旅行天数</span>
                </template>
                <div class="days-display">
                  <span class="days-value">{{ formData.travel_days }}</span>
                  <span class="days-unit">天</span>
                </div>
              </a-form-item>
            </a-col>
          </a-row>
        </div>

        <!-- 第二步:偏好设置 -->
        <div class="form-group">
          <div class="group-header">
            <span class="group-icon">⚙️</span>
            <span class="group-title">偏好设置</span>
          </div>

          <a-row :gutter="24">
            <a-col :span="8">
              <a-form-item name="transportation">
                <template #label>
                  <span class="form-label">交通方式</span>
                </template>
                <a-select v-model:value="formData.transportation" size="large" class="space-select">
                  <a-select-option value="公共交通">🚇 公共交通</a-select-option>
                  <a-select-option value="自驾">🚗 自驾</a-select-option>
                  <a-select-option value="步行">🚶 步行</a-select-option>
                  <a-select-option value="混合">🔀 混合</a-select-option>
                </a-select>
              </a-form-item>
            </a-col>
            <a-col :span="8">
              <a-form-item name="accommodation">
                <template #label>
                  <span class="form-label">住宿偏好</span>
                </template>
                <a-select v-model:value="formData.accommodation" size="large" class="space-select">
                  <a-select-option value="经济型酒店">💰 经济型酒店</a-select-option>
                  <a-select-option value="舒适型酒店">🏨 舒适型酒店</a-select-option>
                  <a-select-option value="豪华酒店">⭐ 豪华酒店</a-select-option>
                  <a-select-option value="民宿">🏡 民宿</a-select-option>
                </a-select>
              </a-form-item>
            </a-col>
            <a-col :span="8">
              <a-form-item name="preferences">
                <template #label>
                  <span class="form-label">旅行偏好</span>
                </template>
                <div class="preference-tags">
                  <a-checkbox-group v-model:value="formData.preferences" class="custom-checkbox-group">
                    <a-checkbox value="历史文化" class="preference-tag">🏛️ 历史文化</a-checkbox>
                    <a-checkbox value="自然风光" class="preference-tag">🏞️ 自然风光</a-checkbox>
                    <a-checkbox value="美食" class="preference-tag">🍜 美食</a-checkbox>
                    <a-checkbox value="购物" class="preference-tag">🛍️ 购物</a-checkbox>
                    <a-checkbox value="艺术" class="preference-tag">🎨 艺术</a-checkbox>
                    <a-checkbox value="休闲" class="preference-tag">☕ 休闲</a-checkbox>
                  </a-checkbox-group>
                </div>
              </a-form-item>
            </a-col>
          </a-row>
        </div>

        <!-- 第三步:额外要求 -->
        <div class="form-group">
          <div class="group-header">
            <span class="group-icon">💬</span>
            <span class="group-title">额外要求</span>
          </div>

          <a-form-item name="free_text_input">
            <a-textarea
              v-model:value="formData.free_text_input"
              placeholder="请输入您的额外要求,例如:想去看升旗、需要无障碍设施、对海鲜过敏等..."
              :rows="3"
              size="large"
              class="space-textarea"
            />
          </a-form-item>
        </div>

        <!-- 提交按钮 -->
        <a-form-item>
          <button
            type="submit"
            :disabled="loading"
            class="ghost-button submit-button"
          >
            <span v-if="!loading">开始规划我的旅行</span>
            <span v-else>正在生成中...</span>
          </button>
        </a-form-item>

        <!-- 加载进度条 -->
        <a-form-item v-if="loading">
          <div class="loading-container">
            <a-progress
              :percent="loadingProgress"
              status="active"
              :stroke-color="{
                '0%': '#f0f0fa',
                '100%': '#f0f0fa',
              }"
              :stroke-width="10"
            />
            <p class="loading-status">
              {{ loadingStatus }}
            </p>
          </div>
        </a-form-item>
      </a-form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, watch } from 'vue'
import { useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { generateTripPlan } from '@/services/api'
import type { TripFormData } from '@/types'
import type { Dayjs } from 'dayjs'

const router = useRouter()
const loading = ref(false)
const loadingProgress = ref(0)
const loadingStatus = ref('')

const formData = reactive<TripFormData & { start_date: Dayjs | null; end_date: Dayjs | null }>({
  city: '',
  start_date: null,
  end_date: null,
  travel_days: 1,
  transportation: '公共交通',
  accommodation: '经济型酒店',
  preferences: [],
  free_text_input: ''
})

// 监听日期变化,自动计算旅行天数
watch([() => formData.start_date, () => formData.end_date], ([start, end]) => {
  if (start && end) {
    const days = end.diff(start, 'day') + 1
    if (days > 0 && days <= 30) {
      formData.travel_days = days
    } else if (days > 30) {
      message.warning('旅行天数不能超过30天')
      formData.end_date = null
    } else {
      message.warning('结束日期不能早于开始日期')
      formData.end_date = null
    }
  }
})

const handleSubmit = async () => {
  if (!formData.start_date || !formData.end_date) {
    message.error('请选择日期')
    return
  }

  loading.value = true
  loadingProgress.value = 0
  loadingStatus.value = '正在初始化...'

  // 模拟进度更新
  const progressInterval = setInterval(() => {
    if (loadingProgress.value < 90) {
      loadingProgress.value += 10

      // 更新状态文本
      if (loadingProgress.value <= 30) {
        loadingStatus.value = '🔍 正在搜索景点...'
      } else if (loadingProgress.value <= 50) {
        loadingStatus.value = '🌤️ 正在查询天气...'
      } else if (loadingProgress.value <= 70) {
        loadingStatus.value = '🏨 正在推荐酒店...'
      } else {
        loadingStatus.value = '📋 正在生成行程计划...'
      }
    }
  }, 500)

  try {
    const requestData: TripFormData = {
      city: formData.city,
      start_date: formData.start_date.format('YYYY-MM-DD'),
      end_date: formData.end_date.format('YYYY-MM-DD'),
      travel_days: formData.travel_days,
      transportation: formData.transportation,
      accommodation: formData.accommodation,
      preferences: formData.preferences,
      free_text_input: formData.free_text_input
    }

    const response = await generateTripPlan(requestData)

    clearInterval(progressInterval)
    loadingProgress.value = 100
    loadingStatus.value = '✅ 完成!'

    if (response.success && response.data) {
      // 保存到sessionStorage
      sessionStorage.setItem('tripPlan', JSON.stringify(response.data))

      message.success('旅行计划生成成功!')

      // 短暂延迟后跳转
      setTimeout(() => {
        router.push('/result')
      }, 500)
    } else {
      message.error(response.message || '生成失败')
    }
  } catch (error: any) {
    clearInterval(progressInterval)
    message.error(error.message || '生成旅行计划失败,请稍后重试')
  } finally {
    setTimeout(() => {
      loading.value = false
      loadingProgress.value = 0
      loadingStatus.value = ''
    }, 1000)
  }
}
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  background-color: #000000;
  position: relative;
}

/* 背景摄影 */
.hero-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=1920&q=80');
  background-size: cover;
  background-position: center;
  z-index: 0;
}

.dark-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
}

/* 英雄区 */
.hero-section {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.hero-content {
  max-width: 1200px;
  padding: 0 20px;
}

.hero-title {
  font-family: 'D-DIN-Bold', 'Arial', sans-serif;
  font-size: 48px;
  font-weight: 700;
  color: #f0f0fa;
  text-transform: uppercase;
  letter-spacing: 0.96px;
  line-height: 1.0;
  margin-bottom: 20px;
}

.hero-subtitle {
  font-family: 'D-DIN', 'Arial', sans-serif;
  font-size: 16px;
  color: #f0f0fa;
  text-transform: uppercase;
  letter-spacing: 1.17px;
  line-height: 1.5;
  opacity: 0.9;
}

/* 滚动指示器 */
.scroll-indicator {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  animation: fadeInUp 1s ease-out 0.5s both;
}

.scroll-arrow {
  width: 24px;
  height: 24px;
  border-right: 2px solid rgba(240, 240, 250, 0.6);
  border-bottom: 2px solid rgba(240, 240, 250, 0.6);
  transform: rotate(45deg);
  animation: scrollBounce 2s infinite;
}

.scroll-text {
  font-family: 'D-DIN', 'Arial', sans-serif;
  font-size: 10px;
  color: rgba(240, 240, 250, 0.6);
  text-transform: uppercase;
  letter-spacing: 1px;
}

@keyframes scrollBounce {
  0%, 20%, 50%, 80%, 100% {
    transform: rotate(45deg) translateY(0);
  }
  40% {
    transform: rotate(45deg) translateY(-10px);
  }
  60% {
    transform: rotate(45deg) translateY(-5px);
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateX(-50%) translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }
}

/* 表单区域 */
.form-section {
  position: relative;
  z-index: 1;
  max-width: 1400px;
  margin: 0 auto;
  padding: 60px 20px;
}

.space-form {
  background: transparent;
}

/* 表单组 */
.form-group {
  margin-bottom: 48px;
  padding: 0;
}

.group-header {
  display: flex;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(240, 240, 250, 0.35);
}

.group-icon {
  font-size: 24px;
  margin-right: 12px;
}

.group-title {
  font-family: 'D-DIN-Bold', 'Arial', sans-serif;
  font-size: 18px;
  font-weight: 700;
  color: #f0f0fa;
  text-transform: uppercase;
  letter-spacing: 1.17px;
}

/* 表单标签 */
.form-label {
  font-size: 13px;
  font-weight: 700;
  color: #f0f0fa;
  text-transform: uppercase;
  letter-spacing: 1.17px;
  margin-bottom: 8px;
  display: block;
}

/* 天数显示 */
.days-display {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 40px;
  padding: 8px 16px;
  background: rgba(240, 240, 250, 0.1);
  border: 1px solid rgba(240, 240, 250, 0.35);
  border-radius: 4px;
  color: #f0f0fa;
}

.days-display .days-value {
  font-size: 24px;
  font-weight: 700;
  margin-right: 4px;
}

.days-display .days-unit {
  font-size: 14px;
}

/* 偏好标签 */
.preference-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.custom-checkbox-group {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  width: 100%;
}

.preference-tag :deep(.ant-checkbox-wrapper) {
  margin: 0 !important;
  padding: 8px 16px;
  border: 1px solid rgba(240, 240, 250, 0.35);
  border-radius: 4px;
  transition: all 0.3s ease;
  background: rgba(240, 240, 250, 0.1);
  font-size: 13px;
  color: #f0f0fa;
  text-transform: uppercase;
  letter-spacing: 1.17px;
}

.preference-tag :deep(.ant-checkbox-wrapper:hover) {
  border-color: #f0f0fa;
  background: rgba(240, 240, 250, 0.2);
}

.preference-tag :deep(.ant-checkbox-wrapper-checked) {
  border-color: #f0f0fa;
  background: rgba(240, 240, 250, 0.3);
  color: #f0f0fa;
}

/* 提交按钮 */
.submit-button {
  width: 100%;
  height: 56px;
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.17px;
}

.submit-button:hover:not(:disabled) {
  background: rgba(240, 240, 250, 0.2);
}

.submit-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* 加载容器 */
.loading-container {
  text-align: center;
  padding: 24px;
  background: rgba(240, 240, 250, 0.1);
  border: 1px dashed rgba(240, 240, 250, 0.35);
  border-radius: 4px;
}

.loading-status {
  margin-top: 16px;
  color: #f0f0fa;
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1.17px;
}

/* Ant Design 组件覆盖 */
:deep(.ant-input),
:deep(.ant-picker) {
  background: rgba(240, 240, 250, 0.1) !important;
  border: 1px solid rgba(240, 240, 250, 0.35) !important;
  color: #f0f0fa !important;
  border-radius: 4px !important;
  text-transform: uppercase !important;
  letter-spacing: 1.17px !important;
}

:deep(.ant-input::placeholder),
:deep(.ant-picker-input > input::placeholder) {
  color: rgba(240, 240, 250, 0.5) !important;
}

:deep(.ant-input:hover),
:deep(.ant-picker:hover) {
  border-color: #f0f0fa !important;
}

:deep(.ant-input:focus),
:deep(.ant-picker-focused) {
  border-color: #f0f0fa !important;
  box-shadow: 0 0 0 2px rgba(240, 240, 250, 0.1) !important;
}

:deep(.ant-select-selector) {
  background: rgba(240, 240, 250, 0.1) !important;
  border: 1px solid rgba(240, 240, 250, 0.35) !important;
  color: #f0f0fa !important;
  border-radius: 4px !important;
}

:deep(.ant-select-selection-item) {
  color: #f0f0fa !important;
  text-transform: uppercase !important;
  letter-spacing: 1.17px !important;
}

:deep(.ant-select-arrow) {
  color: #f0f0fa !important;
}

:deep(.ant-select-dropdown) {
  background: #000000 !important;
  border: 1px solid rgba(240, 240, 250, 0.35) !important;
}

:deep(.ant-select-item) {
  color: #f0f0fa !important;
  text-transform: uppercase !important;
  letter-spacing: 1.17px !important;
}

:deep(.ant-select-item-option-selected) {
  background: rgba(240, 240, 250, 0.2) !important;
}

:deep(.ant-textarea) {
  background: rgba(240, 240, 250, 0.1) !important;
  border: 1px solid rgba(240, 240, 250, 0.35) !important;
  color: #f0f0fa !important;
  border-radius: 4px !important;
}

:deep(.ant-textarea::placeholder) {
  color: rgba(240, 240, 250, 0.5) !important;
}

:deep(.ant-progress-bg) {
  background: #f0f0fa !important;
}

:deep(.ant-form-item-label > label) {
  color: #f0f0fa !important;
  text-transform: uppercase !important;
  letter-spacing: 1.17px !important;
}
</style>

