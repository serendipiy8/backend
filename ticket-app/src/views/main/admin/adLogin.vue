<template>
    <div class="login">
        <el-card class="box-card">
            <template #header>
                <div class="card-header">
                    <span>欢迎管理员</span>
                </div>
            </template>
            <el-form :model="loginForm" status-icon :rules="rules" ref="loginForm">
                <el-form-item label="管理员账号" label-width="100px" prop="username">
                    <el-input type="text" v-model="loginForm.Account">
                    </el-input>
                </el-form-item>
                <el-form-item label="密码" label-width="100px" prop="password">
                    <el-input type="password" v-model="loginForm.Password">
                    </el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm('loginForm')">提交</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>
  
<script>
import api from "@/api"
import { mapMutations } from "vuex"
import { h } from 'vue'
export default {
    components: {

    },
    data() {
        var validatePassword = (rule, value, callback) => {
            if (value === '') {
                callback(new Error("请输入密码"))
            } else {
                callback()
            }
        }

        return {
            loginForm: {
                Account: "",
                Password: "",
            },
            rules: {
                Password: [
                    {
                        validator: validatePassword, trriger: 'blur'
                    }
                ],
            }
        }
    },
    methods: {
        ...mapMutations("adminlogin", ["setAdmin"]),
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    console.log(this.loginForm)
                    api.adminLogin(this.loginForm).then(res => {
                        if (res.data.code == 2000) {
                            console.log(res.data)
                            this.$message({
                                message: "登录成功",
                                type: "success"
                            })
                            this.setAdmin(res.data)
                            localStorage.setItem(
                                "adminticket",
                                JSON.stringify(res.data)
                            )
                            this.$store.dispatch('adminlogin');
                            // this.$store.dispatch('login', res.data.data)
                            this.$router.push("/admin")
                        } else {
                            console.log(res.data)
                            this.$message({
                                message: res.data.message,
                                type: "error"
                            })
                        }
                    })
                } else {
                    this.$message({
                        message: "请检查输入",
                        type: "error"
                    })
                    return false
                }
            })
        }
    }
}
</script>
  
<style>
.login {
    width: 550px;
    margin: 0 auto;

    .box-card {
        width: 550px auto;
        margin: 100px auto;
    }

    .el-button {
        margin: auto;
    }
}
</style>