import Vue from 'vue'
import VueRouter from 'vue-router'
import associtaionPage from '../views/associationsPage'
import educationKatzin from '../views/EductaionKatzin'
import ShibutzPage from '../views/ShibutzPage'
import home from '../views/Home'
import chooseassociations from '../views/ChooseAssociations'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: home
  },
  {
    path: '/ChooseAssociations',
    name: 'ChooseAssociations',
    component: chooseassociations
  },
  {
    path: '/EductaionKatzin',
    name: 'EductaionKatzin',
    component: educationKatzin
  },
  {
    path: '/about',
    name: 'About',
    component:associtaionPage 
  },
  {
    path: '/shibuz',
    name: 'shibuz',
    component:ShibutzPage 
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
