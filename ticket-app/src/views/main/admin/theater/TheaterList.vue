<template>
    <el-table :data="tableData">
        <el-table-column label="剧院ID" width="200" prop="TheaterID"></el-table-column>
        <el-table-column label="剧院名称" width="200" prop="TheaterName"></el-table-column>
        <el-table-column label="剧院地址" width="200" prop="Address"></el-table-column>
        <el-table-column label="剧院容量" width="200" prop="Capacity"></el-table-column>
        <el-table-column label="账号ID" width="200" prop="AdminID"></el-table-column>
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
            deleteTheater: {
                TheaterID: "",
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
        const searchTheaterHandler = this.searchTheaterHandler;
        const onAddSuccessHandler = this.onAddSuccessHandler;
        const editorSuccessHandler = this.editorSuccessHandler;
        eventBus.on("changePage", changePageHandler);
        eventBus.on("searchData", searchTheaterHandler);
        eventBus.on("onAddSuccess", onAddSuccessHandler);
        eventBus.on("editorSuccess", editorSuccessHandler);
        this.$api.selectTheater(this.Form).then(res => {
            console.log(res.data)
            if (res.data.code == 2000) {
                this.tableData = res.data.data,
                    this.totalCount = res.data.totalCount;
                this.totalPage = res.data.totalPage;
            }
        })
        onBeforeUnmount(() => {
            eventBus.off("changePage", changePageHandler);
            eventBus.off("searchData", searchTheaterHandler);
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
            this.$api.selectTheater(this.Form).then(res => {
                if (res.data.code == 2000) {
                    this.tableData = res.data.data;
                }
            });
        },
        handleEdit(index, row) {
            eventBus.emit('editorEvent', row);
        },
        handleDelete(index, row) {
            this.deleteTheater.TheaterID = row.TheaterID;
            console.log(this.deleteTheater);
            ElMessageBox.confirm('proxy will permanently delete the file. Continue?', 'Warning',
                {
                    confirmButtonText: 'OK',
                    cancelButtonText: 'Cancel',
                    type: 'warning',
                })
                .then(() => {
                    this.$api.deleteTheater(this.deleteTheater).then(res => {
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
        searchTheaterHandler(data) {
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