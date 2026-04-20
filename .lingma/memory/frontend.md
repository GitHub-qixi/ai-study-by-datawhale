

```markdown|CODE_EDIT_BLOCK|d:/Code/ai-study-by-datawhale/.lingma/memory/frontend.md

## 实施计划 (Implementation Plan)

### 第一阶段：设计系统分析与准备
- [ ] **分析设计规范**：阅读 .lingma\rules\travel_helper_design.md 深入理解 SpaceX 设计系统的核心原则（纯黑背景、D-DIN字体、全大写+字间距、幽灵按钮、零阴影零卡片）
- [ ] **审计现有代码**：检查 `Home.vue`、`Result.vue`、`App.vue` 当前使用的颜色、字体、圆角、阴影等样式属性
- [ ] **识别冲突点**：列出当前设计与 SpaceX 规范的差异（如渐变背景、圆角卡片、阴影效果等）

### 第二阶段：全局样式配置
- [ ] **修改 App.vue**：
  - 将页面背景改为纯黑 `#000000`
  - 移除 Header/Footer 的传统布局，改为透明覆盖式导航
  - 设置全局字体为 D-DIN（需确认字体文件是否存在或引入 CDN）
  - 应用全局 uppercase + letter-spacing 规则
- [ ] **创建全局 CSS 变量**：在 `main.ts` 或独立 CSS 文件中定义：
  - `--space-black: #000000`
  - `--spectral-white: #f0f0fa`
  - `--ghost-bg: rgba(240, 240, 250, 0.1)`
  - `--ghost-border: rgba(240, 240, 250, 0.35)`
  - `--dark-overlay: rgba(0, 0, 0, 0.5)`

### 第三阶段：Home.vue 重构
- [ ] **移除装饰元素**：删除 `.bg-decoration` 中的浮动圆形动画
- [ ] **改造页面标题区**：
  - 将 `.page-header` 改为全视口高度 (`100vh`) 的摄影背景
  - 标题 "智能旅行助手" 改为 48px D-DIN-Bold，uppercase，letter-spacing 0.96px
  - 副标题改为 16px D-DIN，uppercase，letter-spacing 1.17px
  - 添加暗色渐变遮罩 `rgba(0, 0, 0, 0.5)` 确保文字可读性
- [ ] **重构表单卡片**：
  - 移除 `.form-card` 的白色背景、圆角、阴影
  - 表单字段直接叠加在摄影背景上，无容器包裹
  - 输入框边框改为 `1px solid rgba(240, 240, 250, 0.35)`
  - 输入框背景改为 `rgba(240, 240, 250, 0.1)`
  - 所有标签文本改为 uppercase + letter-spacing
- [ ] **改造提交按钮**：
  - 使用幽灵按钮样式：`background: rgba(240, 240, 250, 0.1)`，`border: 1px solid rgba(240, 240, 250, 0.35)`
  - 圆角改为 32px
  - 文字改为 uppercase + letter-spacing 1.17px
  - 悬停时背景亮度提升
- [ ] **调整加载进度条**：
  - 进度条颜色改为光谱白 `#f0f0fa`
  - 状态文本改为 uppercase

### 第四阶段：Result.vue 重构
- [ ] **移除侧边导航的传统菜单样式**：
  - 将 `.side-nav` 改为透明覆盖式
  - 菜单项改为 uppercase + letter-spacing
  - 选中状态改为光谱白高亮，无渐变背景
- [ ] **改造顶部信息区**：
  - 移除 `.overview-card` 和 `.budget-card` 的白色背景、圆角、阴影
  - 预算网格项改为无边框，仅用文字层级区分
  - 预算总计改为光谱白文字，无渐变背景
- [ ] **重构地图卡片**：
  - 移除 `.map-card` 的卡片样式
  - 地图直接嵌入全视口区域
- [ ] **改造每日行程折叠面板**：
  - 移除 `.ant-collapse` 的圆角、边框、背景色
  - 标题改为 uppercase + letter-spacing
  - 内容区无背景，直接显示在黑色画布上
- [ ] **重构景点卡片**：
  - 移除 `.attraction-card` 的所有卡片样式（背景、圆角、阴影）
  - 景点图片保持全宽，但移除圆角
  - 景点编号徽章改为简单的 uppercase 文字标签
  - 价格标签改为光谱白文字，无背景色
- [ ] **改造天气卡片**：
  - 移除 `.weather-card` 的渐变背景和圆角
  - 天气信息以纯文本形式展示，uppercase
- [ ] **调整导出按钮**：
  - 改为幽灵按钮样式

### 第五阶段：组件样式统一
- [ ] **重写 Ant Design Vue 组件样式覆盖**：
  - 所有 `a-button` 默认使用幽灵按钮样式
  - 所有 `a-input`、`a-select`、`a-textarea` 改为透明背景 + 光谱白边框
  - 所有 `a-card` 移除背景、圆角、阴影
  - 所有 `a-collapse` 改为极简线条分隔
  - 所有 `a-menu` 改为透明背景，选中项为光谱白下划线
- [ ] **统一文字层级**：
  - 标题：48px D-DIN-Bold, uppercase, letter-spacing 0.96px
  - 正文：16px D-DIN, uppercase, letter-spacing 1.17px
  - 微标签：10px D-DIN, uppercase, letter-spacing 1px
  - 所有文字颜色为 `#f0f0fa`

### 第六阶段：响应式适配
- [ ] **移动端适配**：
  - 摄影背景保持全视口高度
  - 文字大小按比例缩小（48px → 32px）
  - 幽灵按钮保持可触摸区域（最小 44x44px）
  - 导航改为汉堡菜单

### 第七阶段：测试与验收
- [ ] **视觉一致性检查**：对比 SpaceX 官网，确保颜色、字体、间距、圆角完全一致
- [ ] **功能测试**：验证表单提交、地图加载、导出功能正常工作
- [ ] **跨浏览器测试**：Chrome、Firefox、Safari 下样式一致性
- [ ] **性能检查**：确保摄影背景加载优化（懒加载、压缩）
- [ ] **无障碍检查**：确保文字与背景对比度符合 WCAG 标准（至少 4.5:1）

### 第八阶段：文档同步
- [ ] **更新设计文档**：记录实际实现的细节与规范的偏差（如有）
- [ ] **标记完成状态**：将所有 `[ ]` 改为 `[成功]`
```