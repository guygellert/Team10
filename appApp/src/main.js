import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import Router from './router'
import router from './router'

Vue.config.productionTip = false

new Vue({
  vuetify,
  Router,
  router,
  render: h => h(App)
}).$mount('#app')
