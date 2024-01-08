<template>
    <el-table :data="tableData">
        <el-table-column label="演出ID" width="170" prop="ShowID"></el-table-column>
        <el-table-column label="演出名称" width="170" prop="ShowName"></el-table-column>
        <el-table-column label="剧院ID" width="170" prop="TheaterID"></el-table-column>
        <el-table-column label="演出日期" width="170" prop="ShowDate"></el-table-column>
        <el-table-column label="演出时长" width="170" prop="Duration"></el-table-column>
        <el-table-column label="简介" width="170" prop="Description"></el-table-column>
        <el-table-column label="演出地点" width="170" prop="City"></el-table-column>        
        <el-table-column label="分类" width="170" prop="Category"></el-table-column>
        <el-table-column label="图片" width="170" prop="Image"></el-table-column>
        <el-table-column label="管理员id" width="170" prop="AdminID"></el-table-column>
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
            deleteShow: {
                ShowID: "",
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
        const searchShowHandler = this.searchShowHandler;
        const onAddSuccessHandler = this.onAddSuccessHandler;
        const editorSuccessHandler = this.editorSuccessHandler;
        eventBus.on("changePage", changePageHandler);
        eventBus.on("searchData", searchShowHandler);
        eventBus.on("onAddSuccess", onAddSuccessHandler);
        eventBus.on("editorSuccess", editorSuccessHandler);
        this.$api.selectShow(this.Form).then(res => {
            console.log(res.data)
            if (res.data.code == 2000) {
                this.tableData = res.data.data,
                    this.totalCount = res.data.totalCount;
                this.totalPage = res.data.totalPage;
            }
        })
        onBeforeUnmount(() => {
            eventBus.off("changePage", changePageHandler);
            eventBus.off("searchData", searchShowHandler);
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
            this.$api.selectShow(this.Form).then(res => {
                if (res.data.code == 2000) {
                    this.tableData = res.data.data;
                }
            });
        },
        handleEdit(index, row) {
            eventBus.emit('editorEvent', row);
        },
        handleDelete(index, row) {
            this.deleteShow.ShowID = row.ShowID;
            console.log(this.deleteShow);
            ElMessageBox.confirm('proxy will permanently delete the file. Continue?', 'Warning',
                {
                    confirmButtonText: 'OK',
                    cancelButtonText: 'Cancel',
                    type: 'warning',
                })
                .then(() => {
                    this.$api.deleteShow().then(res => {
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
        searchShowHandler(data) {
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