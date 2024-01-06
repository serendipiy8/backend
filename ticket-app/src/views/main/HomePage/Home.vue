<template>
  <div>
    <HeaderNav></HeaderNav>
    <div class="index-warp">
      <div class="index-left">
        <HomeNav></HomeNav>
      </div>
      <div class="index-right">
        <HomeSwiper></HomeSwiper>
        <HomeShowList></HomeShowList>
      </div>
    </div>
  </div>
</template>

<script>

import HeaderNav from '@/components/HeaderNav.vue';
import HomeNav from './HomeNav.vue';
import HomeSwiper from './HomeSwiper.vue';
import HomeShowList from './HomeShowList.vue';

export default {
  components: {
    HeaderNav,
    HomeNav,
    HomeSwiper,
    HomeShowList
  },
  data() {
    return {
    }
  }
}
</script>

<style lang="less" scoped>
.index-warp {
  width: 1200px;
  margin: 0 auto;
  // overflow: hidden;
}

.index-left {
  width: 300px;
  float: left;
  text-align: left;

}
.index-right {
  margin-top: 15px;
  width: 900px;
  float: left;
}
</style>    