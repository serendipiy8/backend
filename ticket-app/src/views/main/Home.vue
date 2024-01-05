<template>
  <div>
    <HeaderNav></HeaderNav>
    <router-view>
        
    </router-view>
  </div>
</template>

<script>

import HeaderNav from '@/components/HeaderNav.vue';

export default {
  components: {
    HeaderNav
  },
  data(){
    return{
      loggedIn: false,
    }
  }
}
</script>

<style>

</style>    