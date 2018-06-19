<template>
  <div id="vMainContainer">
    <headerBulma></headerBulma>
    <slot></slot>
  </div>
</template>
<script>
import headerBulma from './header.vue'
export default {
  name: 'container',
  components: {
    headerBulma
  }
}
</script>
