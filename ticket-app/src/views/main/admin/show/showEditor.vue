<template>
    <el-Dialog v-model="dialogVisible" title="编辑票信息" width="50%" :before-close="handleClose">
        <el-form label-width="80px" :model="editorForm" ref="addForm">
            <el-form-item label="演出ID">
                <el-input v-model="editorForm.ShowID"></el-input>
            </el-form-item>
            <el-form-item label="演出名称">
                <el-input v-model="editorForm.ShowName"></el-input>
            </el-form-item>
            <el-form-item label="剧院ID">
                <el-input v-model="editorForm.TheaterID"></el-input>
            </el-form-item>
            <el-form-item label="演出日期">
                <el-input v-model="editorForm.ShowDate"></el-input>
            </el-form-item>
            <el-form-item label="演出时长">
                <el-input v-model="editorForm.Duration"></el-input>
            </el-form-item>
            <el-form-item label="简介">
                <el-input v-model="editorForm.Description"></el-input>
            </el-form-item>
            <el-form-item label="演出地点">
                <el-input v-model="editorForm.City"></el-input>
            </el-form-item>
            <el-form-item label="分类">
                <el-input v-model="editorForm.Category"></el-input>
            </el-form-item>
            <el-form-item label="图片">
                <el-input v-model="editorForm.Image"></el-input>
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
            this.editorForm.ShowID = data.ShowID;
            this.editorForm.ShowName = data.ShowName;
            this.editorForm.TheaterID = data.TheaterID;
            this.editorForm.ShowDate = data.ShowDate;
            this.editorForm.Duration = data.Duration;
            this.editorForm.Description = data.Description; 
            this.editorForm.City = data.City;
            this.editorForm.Category = data.Category;
            this.editorForm.AdminID = data.AdminID;
            this.editorForm.Image = data.Image;
        },
        editorSubmit() {
            // this.editorForm.AdminID = this.getAdminID
            const formData = qs.stringify(this.editorForm);
            console.log(formData)
            this.$api.editorShow(formData, {
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
                AdminID: "",
                Category: "",
                City: "",
                Description: "",
                Duration: "",
                ShowDate: "",
                ShowID: "",
                ShowName: "",
                TheaterID: "",
                Image:"",
            }
        }
    }
}

</script>

<style scoped>
/* Your styles here */
</style>