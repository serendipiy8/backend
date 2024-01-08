import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/main/HomePage/Home.vue';
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
      },
      children: [
        {
          path: "open",
          name: "Open",
          component: () => import("../views/main/HomePage/sub/open.vue"),
        },
        {
          path: "golife",
          name: "Golife",
          component: () => import("../views/main/HomePage/sub/golife.vue"),
        },
        {
          path: "logo",
          name: "Logo",
          component: () => import("../views/main/HomePage/sub/logo.vue"),
        },
        {
          path: "heigh",
          name: "Heigh",
          component: () => import("../views/main/HomePage/sub/heigh.vue"),
        },
      ]
    },
    {
      path: 'information',
      name: 'Information',
      component: () => import("../views/main/Information.vue"),
      meta: {
        requireAuth: true // 标记需要登录
      }
    },
    {
      path: 'ticket',
      name: 'Ticket',
      component: () => import("../views/main/Product/ticket.vue"),
      meta: {
        requireAuth: true // 标记需要登录
      }
    }],
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import("../views/main/Login.vue")
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import("../views/main/admin/AdminHome.vue"),
    children: [{
      path: 'adminticket',
      name: 'AdminTicket',
      component: () => import("../views/main/admin/ticket/AdminTicket.vue")
    },
    {
      path: 'theater',
      name: 'Theater',
      component: () => import("../views/main/admin/theater/Theater.vue")
    },
    {
      path: 'adminrefund',
      name: 'AdminRefund',
      component: () => import("../views/main/admin/refund/AdminRefund.vue")
    },
    {
      path: 'adminorder',
      name: 'AdminOrder',
      component: () => import("../views/main/admin/order/AdminOrder.vue")
    },
    {
      path: 'adminmanager',
      name: 'AdminManager',
      component: () => import("../views/main/admin/manage/AdminManage.vue"),
      meta: {
        requireP: true // 标记需要级别
      }
    },
    {
      path: 'show',
      name: 'Show',
      component: () => import("../views/main/admin/show/AdminShow.vue"),
      meta: {
        requireP: true // 标记需要级别
      }
    },
    ]
  },
  {
    path: '/adlogin',
    name: 'adLogin',
    component: () => import("../views/main/admin/adLogin.vue")
  },
];


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
