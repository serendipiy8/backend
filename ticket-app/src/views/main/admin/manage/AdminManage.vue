<template>
    <div class="order">
        <manageHeader></manageHeader>
        <manageList></manageList>
        <managePagination></managePagination>
        <manageAdd></manageAdd>
        <manageEditor></manageEditor>
    </div>
</template>
  
<script>
import managePagination from './managePagination.vue';
import manageList from './manageList.vue';
import manageHeader from './manageHeader.vue';
import manageAdd from './manageAdd.vue';
import manageEditor from './manageEditor.vue';

export default {
    components: {
        managePagination,
        manageList,
        manageHeader,
        manageAdd,
        manageEditor
    },
    data() {
        return {}
    },
}
</script>
  
<style>
.order {
    width: 1100px;
    margin: 0 auto;
    padding-top: 15px;
}
</style>