<template>
    <el-Dialog v-model="dialogVisible" title="编辑票信息" width="50%" :before-close="handleClose">
        <el-form label="70px" :model="editorForm" ref="addForm">
            <el-form-item label="演出场次ID">
                <el-input v-model="editorForm.ShowID"></el-input>
            </el-form-item>
            <el-form-item label="价格">
                <el-input v-model="editorForm.Price"></el-input>
            </el-form-item>
            <el-form-item label="票档">
                <el-input v-model="editorForm.Category"></el-input>
            </el-form-item>
            <el-form-item label="剩余数量">
                <el-input v-model="editorForm.RemainingQuantity"></el-input>
            </el-form-item>
            <el-form-item label="总数量">
                <el-input v-model="editorForm.TotalQuantity"></el-input>
            </el-form-item>
        </el-form>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="editorSubmit">
            确定
        </el-button>
    </el-Dialog>
</template>

<script>
import { ref, onBeforeUnmount } from 'vue';
import { ElMessageBox } from 'element-plus'
import eventBus from "@/utils/eventBus.js";
const dialogVisible = ref(false)
import { mapState, mapGetters } from 'vuex';
const qs = require('qs');
export default {
    computed: {
        ...mapGetters('adminlogin', ['getAdminID']),
        ...mapState('adminogin', ['user']),
    },
    mounted() {
        const editorFormHandle = this.editorFormHandle;
        eventBus.on("editorEvent", editorFormHandle);
        onBeforeUnmount(() => {
            eventBus.off("editorEvent", editorFormHandle);
        });

    },
    methods: {
        handleClose(done) {
            ElMessageBox.confirm('确定关闭对话框？')
                .then(() => {
                    done()
                })
                .catch(() => {
                    // catch error
                })
        },
        editorFormHandle(data) {
            this.dialogVisible = true;
            this.editorForm.TicketID = data.TicketID;
            this.editorForm.ShowID = data.ShowID;
            this.editorForm.Price = data.Price;
            this.editorForm.Category = data.Category;
            this.editorForm.RemainingQuantity = data.RemainingQuantity;
            this.editorForm.TotalQuantity = data.TotalQuantity; 
        },
        editorSubmit() {
            // this.editorForm.AdminID = this.getAdminID
            const formData = qs.stringify(this.editorForm);
            console.log(formData)
            this.$api.editorTicket(formData, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).then((res) => {
                console.log(res.data);
                if (res.data.code == 2000) {
                    this.dialogVisible = false;
                    eventBus.emit("editorSuccess");
                    this.$message({
                        message: "添加成功",
                        type: "success"
                    });
                } else {
                    this.$message({
                        message: "添加失败",
                        type: "error"
                    });
                }
            });
        }
    },
    data() {
        return {
            dialogVisible: false,
            editorForm: {
                Category: "",
                Address: "",
                Price: "",
                RemainingQuantity: "",
                ShowID: "",
                TotalQuantity: "",
                // AdminID: "",
            }
        }
    }
}

</script>

<style scoped>
/* Your styles here */
</style>