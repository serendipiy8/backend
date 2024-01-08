<template>
    <el-Dialog v-model="dialogVisible" title="编辑票信息" width="50%" :before-close="handleClose">
        <el-form label="70px" :model="editorForm" ref="addForm">
            <el-form-item label="管理员账号">
                <el-input v-model="editorForm.Account"></el-input>
            </el-form-item>
            <el-form-item label="密码">
                <el-input v-model="editorForm.Password"></el-input>
            </el-form-item>
            <el-form-item label="管理员类别">
                <el-input v-model="editorForm.AdminType"></el-input>
            </el-form-item>
            <el-form-item label="权限别">
                <el-input v-model="editorForm.Permissions"></el-input>
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
            this.editorForm.AdminID = data.AdminID;
            this.editorForm.Account = data.Account;
            this.editorForm.AdminType = data.AdminType;
            this.editorForm.Password = data.Password;
            this.editorForm.Permissions = data.Permissions; 
        },
        editorSubmit() {
            // this.editorForm.AdminID = this.getAdminID
            const formData = qs.stringify(this.editorForm);
            console.log(formData)
            this.$api.editorAdmin(formData, {
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
                Account: "",
                AdminID: "",
                AdminType: "",
                Password: "",
                Permissions: "",
            }
        }
    }
}

</script>

<style scoped>
/* Your styles here */
</style>
