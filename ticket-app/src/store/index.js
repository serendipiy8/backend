import { createStore } from 'vuex';
import userModule from './users';

const store = createStore({
  modules: {
    // 注册 user 模块
    user: userModule
  }
});

export default store;