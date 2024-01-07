<template>
    <div><adminHeaderNav></adminHeaderNav>
    <router-view>
        
    </router-view>
    </div>
  </template>
  
  <script>
  
  import adminHeaderNav from '@/components/admin/adminHeaderNav.vue';
  export default {
    components: {
      adminHeaderNav
    },
    data() {
      return {}
    },
  }
  </script>
  
  <style>
  
  </style>