<template>
  <div id="vMainContainer">
    <headerBulma></headerBulma>
    <section class="hero is-medium is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            Vulma css Framework
          </h1>
          <h2 class="subtitle">
            Full-flexbox
          </h2>
        </div>
      </div>
    </section>
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
