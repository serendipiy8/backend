<template>
    <el-table :data="tableData">
        <el-table-column label="订单ID" width="200" prop="OrderID"></el-table-column>
        <el-table-column label="订单号" width="200" prop="OrderStatus"></el-table-column>
        <el-table-column label="订单时间" width="200" prop="PurchaseTime"></el-table-column>
        <el-table-column label="数量" width="200" prop="Quantity"></el-table-column>
        <el-table-column label="票ID" width="200" prop="TicketID"></el-table-column>
        <el-table-column label="账号ID" width="200" prop="UserID"></el-table-column>
    </el-table>
</template>
  
<script>
import eventBus from "@/utils/eventBus.js";
import { onMounted, onBeforeUnmount } from 'vue';
import { mapState, mapGetters } from 'vuex';
export default {
    data() {
        return {
            tableData: [],
            Form: {
                // UserID: "",
                Page: 1,
            },
            currentPage: 1,
            totalCount: 0,
            totalPage: 1,
        }
    },
    computed: {
        ...mapGetters('login', ['getUserID']),
        ...mapState('login', ['user']),
    },
    mounted() {
        console.log("UserID from Vuex:", this.getUserID);
        // this.Form.UserID = this.getUserID;
        console.log(this.Form)
        const changePageHandler = this.changePageHandler;
        eventBus.on("changePage", changePageHandler);
        this.$api.selectOrder(this.Form).then(res => {
            console.log(res.data)
            if (res.data.code == 2000) {
                this.tableData = res.data.data,
                    this.totalCount = res.data.totalCount;
                this.totalPage = res.data.totalPage;
            }
        })
        onBeforeUnmount(() => {
            eventBus.off("changePage", changePageHandler);
        });
    },
    methods: {
        changePageHandler(val) {
            console.log(val);
            this.currentPage = val;
            this.fetchData();  // 更新当前页码
        },
        fetchData() {
            console.log("UserID from Vuex:", this.getUserID);
            // 更新请求参数
            this.Form.Page = this.currentPage;
            console.log(this.Form);
            this.$api.selectOrder(this.Form).then(res => {
                console.log(res.data);
                if (res.data.code == 2000) {
                    this.tableData = res.data.data;
                }
            });
        },
    },
    // computed: {
    //     paginatedData() {
    //         const startIndex = (this.currentPage - 1) * this.itemsPerPage;
    //         const endIndex = startIndex + this.itemsPerPage;
    //         return this.tableData.slice(startIndex, endIndex);
    //     }
    // },
}
</script>
<style>
/* .el-table__header-wrapper{
    margin-left: 145px;
} */
</style>