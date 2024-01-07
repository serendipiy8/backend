<template>
    <div class="order">
        <TheaterList></TheaterList>
        <TheaterPagination></TheaterPagination>
    </div>
</template>
  
<script>
import TheaterPagination from './TheaterPagination.vue';
import TheaterList from './TheaterList.vue';

export default {
    components: {
        TheaterPagination,
        TheaterList
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