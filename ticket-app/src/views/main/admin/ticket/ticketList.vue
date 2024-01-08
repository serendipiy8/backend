<template>
    <el-table :data="tableData">
        <el-table-column label="票ID" width="170" prop="TicketID"></el-table-column>
        <el-table-column label="演出场次ID" width="170" prop="ShowID"></el-table-column>
        <el-table-column label="价格" width="170" prop="Price"></el-table-column>
        <el-table-column label="票档" width="170" prop="Category"></el-table-column>
        <el-table-column label="剩余数量" width="170" prop="RemainingQuantity"></el-table-column>
        <el-table-column label="总数量" width="170" prop="TotalQuantity"></el-table-column>
        <el-table-column label="操作">
            <template #default="scope">
                <el-button size="small" @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
                <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>
  
<script>
import eventBus from "@/utils/eventBus.js";
import { onMounted, onBeforeUnmount } from 'vue';
import { mapState, mapGetters } from 'vuex';
import { ElMessage, ElMessageBox } from 'element-plus'
import base from "@/api/base";
export default {
    data() {
        return {
            tableData: [],
            Form: {
                Page: 1,
            },
            currentPage: 1,
            totalCount: 0,
            totalPage: 1,
            deleteTicket: {
                TicketID: "",
            }
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
        const searchTicketHandler = this.searchTicketHandler;
        const onAddSuccessHandler = this.onAddSuccessHandler;
        const editorSuccessHandler = this.editorSuccessHandler;
        eventBus.on("changePage", changePageHandler);
        eventBus.on("searchData", searchTicketHandler);
        eventBus.on("onAddSuccess", onAddSuccessHandler);
        eventBus.on("editorSuccess", editorSuccessHandler);
        this.$api.selectTicket(this.Form).then(res => {
            console.log(res.data)
            if (res.data.code == 2000) {
                this.tableData = res.data.data,
                    this.totalCount = res.data.totalCount;
                this.totalPage = res.data.totalPage;
            }
        })
        onBeforeUnmount(() => {
            eventBus.off("changePage", changePageHandler);
            eventBus.off("searchData", searchTicketHandler);
            eventBus.off("onAddSuccess", onAddSuccessHandler);
            eventBus.off("editorSuccess", editorSuccessHandler);
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
            this.$api.selectTicket(this.Form).then(res => {
                if (res.data.code == 2000) {
                    this.tableData = res.data.data;
                }
            });
        },
        handleEdit(index, row) {
            eventBus.emit('editorEvent', row);
        },
        handleDelete(index, row) {
            this.deleteTicket.TicketID = row.TicketID;
            console.log(this.deleteTicket);
            ElMessageBox.confirm('proxy will permanently delete the file. Continue?', 'Warning',
                {
                    confirmButtonText: 'OK',
                    cancelButtonText: 'Cancel',
                    type: 'warning',
                })
                .then(() => {
                    this.$api.deleteTicket(this.deleteTicket.TicketID).then(res => {
                        console.log(res.data);
                        if (res.data.code == 2000) {
                            this.$message({
                                message: "删除成功",
                                type: "success"
                            })
                            this.fetchData()
                            eventBus.emit("deleteSuccess");
                        } else {
                            this.$message({
                                message: "删除失败",
                                type: "error"
                            })
                        }
                    })
                    ElMessage({
                        type: 'success',
                        message: 'Delete completed',
                    })
                })
                .catch(() => {
                    ElMessage({
                        type: 'info',
                        message: 'Delete canceled',
                    })
                })
        },
        searchTicketHandler(data) {
            if (Array.isArray(data)) {
                this.tableData = data;
            } else {
                data = [data];
                this.tableData = data;
                console.log(data);
            }
        },
        onAddSuccessHandler() {
            this.fetchData();
        },
        editorSuccessHandler() {
            this.fetchData();
        }
    }
}
</script>
<style>
/* .el-table__header-wrapper{
    margin-left: 145px;
} */
</style>