import container from './container.vue'
import Vue from 'vue'

export default function(){
  let componentes = {}
  Vue.component(container.name, container)
  // componentes[container.name] = container
  return componentes
}
