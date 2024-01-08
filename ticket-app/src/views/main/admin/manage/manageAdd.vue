<template>
    <el-Dialog v-model="dialogVisible" title="添加票" width="50%" :before-close="handleClose">
        <el-form label-width="90px" :model="addForm" ref="addForm">
            <el-form-item label="管理员账号">
                <el-input v-model="addForm.Account"></el-input>
            </el-form-item>
            <el-form-item label="密码">
                <el-input v-model="addForm.Password"></el-input>
            </el-form-item>
            <el-form-item label="管理员类别">
                <el-input v-model="addForm.AdminType"></el-input>
            </el-form-item>
            <el-form-item label="权限别">
                <el-input v-model="addForm.Permissions"></el-input>
            </el-form-item>
        </el-form>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="sureSubmit">
            确定
        </el-button>
    </el-Dialog>
</template>

<script>
import { ref } from 'vue'
import { ElMessageBox } from 'element-plus'
import eventBus from "@/utils/eventBus.js";
import { mapState, mapGetters } from 'vuex';
const dialogVisible = ref(false)

export default {
    computed: {
        ...mapGetters('adminlogin', ['getAdminID']),
        ...mapState('adminogin', ['user']),
    },
    mounted() {
        const addFormHandle = this.addFormHandle;
        eventBus.on("onAddEvent", addFormHandle);
        this.addForm.AdminID = this.getAdminID
        // console.log("UserID from Vuex:", this.getAdminID);
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
        addFormHandle(flag) {
            this.dialogVisible = flag;
        },
        sureSubmit() {
            console.log(this.addForm)
            this.$api.addAdmin(this.addForm).then((res) => {
                console.log(res.data);
                if (res.data.code == 2000) {
                    // this.clearForm();
                    this.dialogVisible = false;
                    eventBus.emit("onAddSuccess");
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
            addForm: {
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
