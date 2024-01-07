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
export default {
    data() {
        return {
            tableData: [],
            Form: {
                UserID: "0",
            },
            count: 0,
            page: 1,
        }
    },
    mounted() {
        console.log(this.Form)
        this.$api.selectOrder(this.From).then(res => {
            console.log(res.data)
            if (res.data.code == 2000) {
                this.tableData = res.data.data
                this.count = res.data.totalCount
                this.page = res.data.totalPage
                console.log(this.page)
            }
        })
    },
}
</script>
<style>
/* .el-table__header-wrapper{
    margin-left: 145px;
} */
</style>