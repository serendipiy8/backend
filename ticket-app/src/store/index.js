import { createStore } from 'vuex';
import userModule from './users';
import Vue from 'vue'
import Vuex from 'vuex'
import login from "./modules/login"

Vue.use(Vuex)


const store = createStore({
  modules: {
    // 注册 user 模块
    user: userModule
  }
});

export default new Vuex.Store({
  modules: {
    login
  }
})


