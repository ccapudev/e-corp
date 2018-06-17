import Vue from 'vue'
import Router from 'vue-router'
import container from '@/components/container'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'container',
      component: container
    }
  ]
})
