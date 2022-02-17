import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
      unit:"",
      capacity:0,
      interests:[{"text":'רפואי',"value":'רפואי'},{"text":'בעלי חיים',"value":'בעלי חיים'}],
      datesPick:[]
  },
  mutations: {
      changeUnit(state,name){
          state.unit = name
      }
  },
  actions: {
  },
  modules: {
  }
})
