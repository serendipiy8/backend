<template>
    <el-table :data="tableData">
        <el-table-column label="订单ID" width="200" prop="OrderID"></el-table-column>
        <el-table-column label="退票ID" width="200" prop="RefundID"></el-table-column>
        <el-table-column label="退票原因" width="200" prop="RefundReason"></el-table-column>
        <el-table-column label="退票时间" width="200" prop="RefundTime"></el-table-column>
        <el-table-column label="账号ID" width="200" prop="UserID"></el-table-column>
        <el-table-column label="处理状态" width="200" prop="TicketStatus"></el-table-column>
        <el-table-column label="操作">
            <template #default="scope">
                <el-button size="small" @click="handleCommit(scope.$index, scope.row)">确认</el-button>
                <el-button size="small" type="danger" @click="handleRetreat(scope.$index, scope.row)">退回</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>
  
<script>
import eventBus from "@/utils/eventBus.js";
import { onMounted, onBeforeUnmount } from 'vue';
import { mapState, mapGetters } from 'vuex';
import { ElMessage, ElMessageBox } from 'element-plus'
const qs = require('qs');
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
            commitForm: {
                RefundID: "",
                TicketStatus: "",
            },
        }
    },
    computed: {
        // ...mapGetters('login', ['getUserID']),
        // ...mapState('login', ['user']),
    },
    mounted() {
        // console.log("UserID from Vuex:", this.getUserID);
        // this.Form.UserID = this.getUserID;
        console.log(this.Form)
        const changePageHandler = this.changePageHandler;
        eventBus.on("changePage", changePageHandler);
        this.$api.selectRefund(this.Form).then(res => {
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
            // console.log("UserID from Vuex:", this.getUserID);
            // 更新请求参数
            this.Form.Page = this.currentPage;
            console.log(this.Form);
            this.$api.selectRefund(this.Form).then(res => {
                console.log(res.data);
                if (res.data.code == 2000) {
                    this.tableData = res.data.data;
                }
            });
        },
        handleCommit(index, row) {
            this.commitForm.RefundID = row.RefundID;
            this.commitForm.TicketStatus = "已退款";
            const formData = qs.stringify(this.commitForm);
            console.log(formData);
            ElMessageBox.confirm('确定取消用户订单？', 'Warning',
                {
                    confirmButtonText: 'OK',
                    cancelButtonText: 'Cancel',
                    type: 'warning',
                })
                .then(() => {
                    this.$api.commitRefund(formData, {
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        }
                    }).then(res => {
                        console.log(res.data);
                        if (res.data.code == 2000) {
                            this.$message({
                                message: "取消成功",
                                type: "success"
                            })
                            this.fetchData()
                            // eventBus.emit("deleteSuccess");
                        } else {
                            this.$message({
                                message: "失败",
                                type: "error"
                            })
                        }
                    })
                    ElMessage({
                        type: 'success',
                        message: '取消成功',
                    })
                })
                .catch(() => {
                    ElMessage({
                        type: 'info',
                        message: '取消成功',
                    })
                })
        },
        handleRetreat(index,row){
            this.commitForm.RefundID = row.RefundID;
            this.commitForm.TicketStatus = "已退回";
            const formData = qs.stringify(this.commitForm);
            console.log(formData);
            ElMessageBox.confirm('确定退回用户订单？', 'Warning',
                {
                    confirmButtonText: 'OK',
                    cancelButtonText: 'Cancel',
                    type: 'warning',
                })
                .then(() => {
                    this.$api.commitRefund(formData, {
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        }
                    }).then(res => {
                        console.log(res.data);
                        if (res.data.code == 2000) {
                            this.$message({
                                message: "退回成功",
                                type: "success"
                            })
                            this.fetchData()
                            // eventBus.emit("deleteSuccess");
                        } else {
                            this.$message({
                                message: "失败",
                                type: "error"
                            })
                        }
                    })
                    ElMessage({
                        type: 'success',
                        message: '取消成功',
                    })
                })
                .catch(() => {
                    ElMessage({
                        type: 'info',
                        message: '取消成功',
                    })
                })
        }
    },

}
</script>
<style>
/* .el-table__header-wrapper{
    margin-left: 145px;
} */
</style>