// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import vContainer from './components/container.vue'

Vue.config.productionTip = false

require('./assets/vulma/main.scss')

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    vContainer,
  },
  render: h => h(App)
})
