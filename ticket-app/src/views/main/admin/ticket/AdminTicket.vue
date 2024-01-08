<template>
    <div class="order">
        <ticketHeader></ticketHeader>
        <ticketList></ticketList>
        <ticketPagination></ticketPagination>
        <ticketAdd></ticketAdd>
        <ticketEditor></ticketEditor>
    </div>
</template>
  
<script>
import ticketPagination from './ticketPagination.vue';
import ticketList from './ticketList.vue';
import ticketHeader from './ticketHeader.vue';
import ticketAdd from './ticketAdd.vue';
import ticketEditor from './ticketEditor.vue';

export default {
    components: {
        ticketPagination,
        ticketList,
        ticketHeader,
        ticketAdd,
        ticketEditor
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