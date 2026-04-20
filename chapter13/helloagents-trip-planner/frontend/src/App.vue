<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup lang="ts">
</script>

<style>
#app {
  font-family: 'D-DIN', 'Arial', 'Verdana', sans-serif;
  background-color: #000000;
  min-height: 100vh;
}

/* Global text styling */
#app * {
  text-transform: uppercase;
}

#app h1, #app h2, #app h3, #app h4, #app h5, #app h6 {
  font-family: 'D-DIN-Bold', 'Arial', 'Verdana', sans-serif;
  letter-spacing: 0.96px;
}

#app p, #app span, #app div, #app label, #app input, #app textarea, #app select, #app button {
  letter-spacing: 1.17px;
}
</style>

