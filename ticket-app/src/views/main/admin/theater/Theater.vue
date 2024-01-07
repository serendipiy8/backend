<template>
    <div class="order">
        <ThraterHeader></ThraterHeader>
        <TheaterList></TheaterList>
        <TheaterPagination></TheaterPagination>
    </div>
</template>
  
<script>
import TheaterPagination from './TheaterPagination.vue';
import TheaterList from './TheaterList.vue';
import ThraterHeader from './TheaterHeader.vue';

export default {
    components: {
        TheaterPagination,
        TheaterList,
        ThraterHeader
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