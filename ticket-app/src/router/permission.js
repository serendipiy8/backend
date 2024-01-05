import store from '../store'
import router from './index'


router.beforeEach((to, from, next) => {
  // 判断用户是否已登录
  const isAuthenticated = store.getters.isAuthenticated;

  // 判断是否需要登录，这里假设需要登录的路由有一个 meta 字段 requireAuth
  const requiresAuth = to.matched.some(record => record.meta.requireAuth);

  if (requiresAuth && !isAuthenticated) {
    // 如果需要登录且用户未登录，则跳转到登录页面
    next({ name: 'Login' });
  } else if (to.meta.isLogin) {
    // 如果是登录页面
    let token = store.state.loginModule.user.token;
    if (token) {
      next();
    } else {
      console.log('Token not found')
      next({
        path: "/login"
      });
    }
  } else {
    // 允许访问目标页面
    next();
  }
});

