import Vue from 'vue'
import VueRouter from 'vue-router'
import estate from '../views/estate.vue'
import area from '../views/area.vue'
import price from '../views/price.vue'
import house from '../views/house.vue'
import orientation from '../views/orientation.vue'
import way from '../views/way.vue'
import recommands from '../views/recommands.vue'
import prediction from '../views/prediction.vue'
import qianduan from '../views/qianduan.vue'
Vue.use(VueRouter)
const routes = [
  {
    path: '/estate',
    name: 'estate',
    component: estate
  },
  {
    path: '/qianduan',
    name: 'qianduan',
    component: qianduan
  },
  {
    path: '/area',
    name: 'area',
    component: area
  },
  {
    path: '/price',
    name: 'price',
    component: price
  },
  {
    path: '/house',
    name: 'house',
    component: house
  },
  {
    path: '/house',
    name: 'house',
    component: house
  },
  {
    path: '/orientation',
    name: 'orientation',
    component: orientation
  },
  {
    path: '/way',
    name: 'way',
    component: way
  },
  {
    path: '/recommands',
    name: 'recommands',
    component: recommands
  },
  {
    path: '/prediction',
    name: 'prediction',
    component: prediction
  },
]
const router = new VueRouter({
  routes
})
export default router
