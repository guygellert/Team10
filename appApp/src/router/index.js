import Vue from 'vue'
import VueRouter from 'vue-router'
import associtaionPage from '../views/associationsPage'
import educationKatzin from '../views/EductaionKatzin'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: educationKatzin
  },
  {
    path: '/about',
    name: 'About',
    component:associtaionPage 
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
