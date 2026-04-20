目前chapter13\helloagents-trip-planner\frontend下的前端页面显示符合.lingma\rules\travel_helper_design.md该文档规范，但是页面响应组件没有：
    1，下滑动页面没有滑动提示，导致我开始进来都不知道该如何操作
    2，无论是点击目的地城市还是开始日期，还有下面其他所有下拉框，响应出来的组件都不符合文档风格
    3，生成的旅游计划页面中更加完全不符合文档要求

## 实施计划 (Implementation Plan)

### 第一阶段：问题分析与审计
- [成功] **分析滚动提示缺失问题**：检查 Home.vue 和 Result.vue 的滚动行为，确认是否缺少视觉引导（如滚动箭头、提示文字或动画）
- [成功] **审计下拉框组件样式**：检查 Ant Design Vue 的 `a-select`、`a-date-picker`、`a-dropdown` 等组件的下拉面板样式，识别不符合 SpaceX 规范的部分（背景色、边框、圆角、阴影、文字样式）
- [成功] **审计 Result.vue 页面布局**：全面检查 Result.vue 的所有卡片、折叠面板、列表项，识别仍存在的渐变背景、圆角、阴影等非规范元素

### 第二阶段：添加滚动提示功能
- [成功] **在 Home.vue 英雄区底部添加滚动指示器**：
  - 文件：`chapter13/helloagents-trip-planner/frontend/src/views/Home.vue`
  - 实现：在 `.hero-section` 底部添加一个向下箭头的动画图标（使用 CSS 动画）
  - 样式：光谱白 `#f0f0fa`，半透明，上下浮动动画
  - 位置：绝对定位，距离底部 30px，居中
- [成功] **在 Result.vue 添加滚动引导**：
  - 文件：`chapter13/helloagents-trip-planner/frontend/src/views/Result.vue`
  - 实现：如果内容超过视口高度，在首屏底部显示轻微的文字提示"↓ 向下滚动查看详情"
  - 样式：10px D-DIN, uppercase, letter-spacing 1px, 光谱白，透明度 0.6

### 第三阶段：修复下拉框组件样式
- [成功] **全局覆盖 Ant Design Vue 下拉面板样式**：
  - 文件：`chapter13/helloagents-trip-planner/frontend/src/styles/spacex-design.css`
  - 目标类名：`.ant-select-dropdown`, `.ant-picker-dropdown`, `.ant-dropdown-menu`
  - 修改内容：
    - 背景色改为纯黑 `#000000`
    - 边框改为 `1px solid rgba(240, 240, 250, 0.35)`
    - 移除所有圆角（border-radius: 0）
    - 移除所有阴影（box-shadow: none）
    - 选项文字改为光谱白 `#f0f0fa`，uppercase，letter-spacing 1.17px
    - 悬停状态背景改为 `rgba(240, 240, 250, 0.1)`
    - 选中状态背景改为 `rgba(240, 240, 250, 0.2)`
- [成功] **修复日期选择器面板**：
  - 文件：同上
  - 目标类名：`.ant-picker-panel`, `.ant-picker-header`, `.ant-picker-cell`
  - 修改内容：
    - 面板背景改为纯黑
    - 头部边框改为光谱白细线
    - 日期单元格文字改为光谱白，uppercase
    - 今日标记、选中日期改为光谱白背景 + 黑色文字
    - 悬停日期单元格背景改为 `rgba(240, 240, 250, 0.1)`
- [成功] **修复复选框组样式**：
  - 文件：`Home.vue` scoped styles
  - 目标：偏好标签的复选框展开后的表现
  - 确保勾选状态的视觉反馈符合幽灵按钮风格

### 第四阶段：重构 Result.vue 页面以完全符合规范
- [成功] **移除所有残留的渐变背景**：
  - 文件：`chapter13/helloagents-trip-planner/frontend/src/views/Result.vue`
  - 搜索并替换所有 `linear-gradient` 为纯色 `rgba(240, 240, 250, 0.1)` 或透明
  - 涉及区域：预算总计、天气卡片、酒店卡片、每日行程头部等
- [成功] **统一所有卡片的极简风格**：
  - 确保所有 `a-card` 组件：
    - 背景透明或 `rgba(240, 240, 250, 0.05)`
    - 边框 `1px solid rgba(240, 240, 250, 0.35)`
    - 无圆角或极小圆角（4px）
    - 无阴影
- [成功] **修复折叠面板样式**：
  - 确保 `a-collapse` 的每个 panel：
    - 头部背景为 `rgba(240, 240, 250, 0.1)`
    - 边框为光谱白细线
    - 标题文字 uppercase + letter-spacing
    - 内容区背景透明
- [成功] **修复景点图片徽章和价格标签**：
  - 徽章：改为方形（非圆形），背景 `rgba(240, 240, 250, 0.9)`，黑色文字
  - 价格标签：同样改为方形，无边框，纯文字展示
- [成功] **修复天气卡片**：
  - 移除所有彩色背景（如 `#e0f7fa`）
  - 改为透明背景 + 光谱白边框
  - 所有文字改为光谱白，uppercase
- [成功] **修复侧边导航菜单**：
  - 确保子菜单展开后的样式也符合规范
  - 选中项仅用左边框高亮，无背景色变化

### 第五阶段：增强用户体验细节
- [成功] **添加平滑滚动行为**：
  - 文件：`spacex-design.css`
  - 在全局样式中添加 `html { scroll-behavior: smooth; }`
- [成功] **优化表单字段的焦点状态**：
  - 确保输入框聚焦时边框亮度提升，有清晰的视觉反馈
  - 添加微妙的过渡动画（0.3s ease）
- [成功] **添加加载状态的视觉优化**：
  - 进度条改为极简线条样式，无渐变
  - 状态文字使用 uppercase + letter-spacing

### 额外修复：天气栏目规范修正
- [成功] **修复 Result.vue 天气栏目样式**：
  - 文件：`chapter13/helloagents-trip-planner/frontend/src/views/Result.vue`
  - 外层卡片 `.weather-section-card`：
    - 背景改为透明
    - 边框 `1px solid rgba(240, 240, 250, 0.35)`
    - 移除圆角（border-radius: 0）
    - 移除阴影
    - 头部标题 uppercase + letter-spacing
  - 内层天气卡片 `.weather-card`：
    - 背景改为透明（原来是 `rgba(240, 240, 250, 0.1)`）
    - 移除圆角（border-radius: 0，原来是 4px）
    - 悬停效果改为更微妙的透明度变化