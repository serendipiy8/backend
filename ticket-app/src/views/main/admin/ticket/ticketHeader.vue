<template>
    <div class="head">
        <el-form ref="searchForm" :model="search">
            <el-form-item>
                <el-input v-model="search.TicketID" placeholder="请输入票ID"/>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmitSearch">查询</el-button>
                <el-button type="primary" @click="addFormHandle">添加</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
import eventBus from "@/utils/eventBus.js";
export default {
    components: {
    },
    data() {
        return {
            search: {
                TicketID: "",
            },
        }
    },
    methods: {
        onSubmitSearch() {
            if (this.search.TicketID == "") {
                this.$message({
                    message: "请输入票ID",
                    type: "warning"
                });
                return;
            }
            if (this.search.TicketID == "/") {
                this.$api.selectTicket().then(res => {
                if (res.data.code == 2000) {
                    eventBus.emit('searchData', res.data.data)
                }
            });
            }else{
                this.$api.searchTicket(this.search).then(res => {
                console.log(res.data);
                if (res.data.code == 2000) {
                    eventBus.emit('searchData', res.data.data)
                    this.$message({
                        message: "查询成功",
                        type: "success"
                    });
                }
                else {
                    this.$message({
                        message: "查询失败",
                        type: "error"
                    });
                }
            })
                .catch(error => {
                    console.error("Error in searchTicketHandler:", error);
                    this.$message({
                        message: "查询出错",
                        type: "error"
                    });
                });
            }
            
        },
        addFormHandle() {
            eventBus.emit('onAddEvent',true)
        }
    }
}
</script>

<style scoped lang="less">
.el-form {
    overflow: hidden;
    clear: both;

    .el-form-item {
        float: left;
        margin-right: 10px;

        .el-input {
            width: 1030px;
        }
    }
}

.head {
    margin-top: 20px;
    width: 100%;
}
</style>