// import { createStore } from 'vuex';
// import userModule from './users';
// import Vue from 'vue'
// import Vuex from 'vuex'
// import login from "./modules/login"



// const store = createStore({
//   modules: {
//     // 注册 user 模块
//     user: userModule,
//     login: loginModule
//   }
// });

// // export default new Vuex.Store({
// //   modules: {
// //     login
// //   }
// // })


// Vue.use(Vuex)
// export default store;

import { createStore } from 'vuex';
import userModule from './modules/users';
import loginModule from "./modules/login";
import { createApp } from 'vue';
import Vuex from 'vuex';

const app = createApp();

app.use(Vuex);

const store = createStore({
  modules: {
    user: userModule,
    login: loginModule,
  }
});

app.use(store);

export default app;


