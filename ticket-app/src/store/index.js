import { createStore } from 'vuex';
import userModule from './modules/users';
import loginModule from "./modules/login"
import Vue from 'vue'
import Vuex from "vuex"



const store = createStore({
  modules: {
    // 注册 user 模块
    user: userModule,
    login: loginModule
  }
});


export default store;