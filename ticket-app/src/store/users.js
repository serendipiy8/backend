const state = {
    isAuthenticated: false
  };
  
  const mutations = {
    setAuthentication(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    }
  };
  
  const actions = {
    login({ commit }) {
      // 处理登录逻辑，成功后将 isAuthenticated 设置为 true
      commit('setAuthentication', true);
    },
    logout({ commit }) {
      // 处理登出逻辑，将 isAuthenticated 设置为 false
      commit('setAuthentication', false);
    }
  };
  
  const getters = {
    isAuthenticated: state => state.isAuthenticated
  };
  
  export default {
    state,
    mutations,
    actions,
    getters
  };
  
