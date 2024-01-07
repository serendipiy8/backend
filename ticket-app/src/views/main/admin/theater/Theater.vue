<template>
    <div class="order">
        <TheaterHeader></TheaterHeader>
        <TheaterList></TheaterList>
        <TheaterPagination></TheaterPagination>
        <TheaterAdd></TheaterAdd>
        <TheaterEditor></TheaterEditor>
    </div>
</template>
  
<script>
import TheaterPagination from './TheaterPagination.vue';
import TheaterList from './TheaterList.vue';
import TheaterHeader from './TheaterHeader.vue';
import TheaterAdd from './TheaterAdd.vue';
import TheaterEditor from './TheaterEditor.vue';

export default {
    components: {
        TheaterPagination,
        TheaterList,
        TheaterHeader,
        TheaterAdd,
        TheaterEditor
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