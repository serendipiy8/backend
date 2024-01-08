<template>
    <div class="order">
        <showHeader></showHeader>
        <showList></showList>
        <showPagination></showPagination>
        <showAdd></showAdd>
        <showEditor></showEditor>
    </div>
</template>
  
<script>
import showPagination from './showPagination.vue';
import showList from './showList.vue';
import showHeader from './showHeader.vue';
import showAdd from './showAdd.vue';
import showEditor from './showEditor.vue';

export default {
    components: {
        showPagination,
        showList,
        showHeader,
        showAdd,
        showEditor
    },
    data() {
        return {}
    },
}
</script>
  
<style>
.order {
    width: 1300px;
    margin: 0 auto;
    padding-top: 15px;
}
</style>