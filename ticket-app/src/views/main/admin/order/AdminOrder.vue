<template>
    <div class="order">
        <RefundList></RefundList>
        <RefundPagination></RefundPagination>
    </div>
</template>
  
<script>
import RefundPagination from './OrderPagination.vue';
import RefundList from './OrderList.vue';

export default {
    components: {
        RefundPagination,
        RefundList
    },
    data() {
        return {}
    },
}
</script>
  
<style>
.order {
    width: 1200px;
    margin: 0 auto;
    padding-top: 15px;
}
</style>