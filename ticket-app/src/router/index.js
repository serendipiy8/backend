import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/main/Home.vue';
import Layout from '../views/Layout.vue';
// import Concert from '../views/main/Concert.vue'


const routes = [
  {
    path: '/',
    name: 'Layout',
    component: Layout,
    children: [{
      path: '',
      name: 'Home',
      component: Home
    },
    {
      path: 'concert',
      name: 'Concert',
      component: () => import("../views/main/Concert.vue"),
      meta: {
        requireAuth: true // 标记需要登录
      }
    }]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import("../views/main/Login.vue")
  }
];


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
