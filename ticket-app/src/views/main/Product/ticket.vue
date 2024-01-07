<template>
  <HeaderNav></HeaderNav>
  <div class="order">
    <ProductList></ProductList>
    <ProductPagination></ProductPagination>
  </div>
</template>

<script>

import HeaderNav from '@/components/HeaderNav.vue';
import ProductList from './ProductList.vue';
import ProductPagination from './ProductPagination.vue';
export default {
  components: {
    HeaderNav,
    ProductList,
    ProductPagination
  },
  data() {
    return {}
  },

}
</script>

<style scoped>
.order {
  width: 1340px;
  margin: 0 auto;
  padding-top: 15px;
}
</style>