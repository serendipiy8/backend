<template>
    <el-table :data="tableData">
        <el-table-column label="订单ID" width="200" prop="OrderID"></el-table-column>
        <el-table-column label="订单时间" width="200" prop="PurchaseTime"></el-table-column>
        <el-table-column label="数量" width="200" prop="Quantity"></el-table-column>
        <el-table-column label="票ID" width="200" prop="TicketID"></el-table-column>
        <el-table-column label="账号ID" width="200" prop="UserID"></el-table-column>
        <el-table-column label="支付状态" width="200" prop="OrderStatus"></el-table-column>
        <el-table-column label="退票">
            <template #default="scope">
                <el-button size="small" type="danger" @click="handleRefund(scope.$index, scope.row)">退票</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>
  
<script>
import eventBus from "@/utils/eventBus.js";
import { onMounted, onBeforeUnmount } from 'vue';
import { mapState, mapGetters } from 'vuex';
import { ElMessage, ElMessageBox } from 'element-plus'
export default {
    data() {
        return {
            tableData: [],
            Form: {
                UserID: "666666",
                Page: 1,
            },
            currentPage: 1,
            totalCount: 0,
            totalPage: 1,
            refundOrder: {
                UserID: "",
                AdminID: "",
                RefundTime: "",
                RefundReason: "没时间",
                TicketStatus: "未处理",
                OrderID: "",
            }
        }
    },
    computed: {
        ...mapGetters('login', ['getUserID']),
        ...mapState('login', ['user']),
    },
    mounted() {
        console.log("UserID from Vuex:", this.getUserID);
        this.Form.UserID = this.getUserID;
        // this.refundOrder.UserID = this.getUserID;
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
            // 更新请求参数
            this.Form.Page = this.currentPage;
            this.$api.selectOrder(this.Form).then(res => {
                if (res.data.code == 2000) {
                    this.tableData = res.data.data;
                }
            });
        },
        handleRefund(index, row) {
            this.refundOrder.OrderID = String(row.OrderID);
            this.refundOrder.UserID = this.getUserID;
            const currentDate = new Date();
            // 提取年、月、日
            const year = currentDate.getFullYear();
            const month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); // 月份是从0开始的，因此要加1
            const day = currentDate.getDate().toString().padStart(2, '0');
            // 构建年月日字符串
            const formattedDate = `${year}-${month}-${day}`;
            this.refundOrder.RefundTime = formattedDate;
            console.log(this.refundOrder);
            ElMessageBox.confirm('确定要退票吗?', 'Warning',
                {
                    confirmButtonText: 'OK',
                    cancelButtonText: 'Cancel',
                    type: 'warning',
                })
                .then(() => {
                    this.$api.refundOrder(this.refundOrder).then(res => {
                        console.log(res.data);
                        if (res.data.code == 2000) {
                            this.$message({
                                message: "提交成功",
                                type: "success"
                            })
                            this.fetchData()
                        } else {
                            this.$message({
                                message: "提交失败",
                                type: "error"
                            })
                        }
                    })
                    ElMessage({
                        type: 'success',
                        message: '提交成功',
                    })
                })
                .catch(() => {
                    ElMessage({
                        type: 'info',
                        message: '取消退票',
                    })
                })
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