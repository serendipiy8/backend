import store from '../store'
import router from './index'


router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isAuthenticated;
  const requiresAuth = to.matched.some(record => record.meta.requireAuth);
  const Permissions = store.state.adminlogin.user.data.Permissions;
  const isAdminManagerRoute = to.name === 'AdminManager';

  if (requiresAuth && !isAuthenticated) {
    next({ name: 'Login' });
  } else if (to.meta.isLogin) {
    let token = store.state.loginModule.user.token;
    if (token) {
      next();
    } else {
      console.log('Token not found')
      next({ path: "/login" });
    }
  }
  else if (isAdminManagerRoute && Permissions != 5) {
    console.log('Permissions', store.state.adminlogin.user.data.Permissions);
    // console.log('Permissions', Permissions);
    console.log('AdminManager权限不足');
    next({ name: 'Admin' });
  } else {
    console.log('AdminManager权限足');
    next();
  }
});


