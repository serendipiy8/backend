<template>
  <div class="login">
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>欢迎</span>
        </div>
      </template>
      <el-tabs v-model="currentIndex" class="demo-tabs" @tab-click="handleTabsClick" stretch="True">
        <el-tab-pane label="登录" name="login">
          <el-form :model="loginForm" status-icon :rules="rules" ref="loginForm">
            <el-form-item label="用户名" label-width="80px" prop="username">
              <el-input type="text" v-model="loginForm.username">
              </el-input>
            </el-form-item>
            <el-form-item label="密码" label-width="80px" prop="password">
              <el-input type="password" v-model="loginForm.password">
              </el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('loginForm')">提交</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="注册" name="register">
          <el-form :model="registerForm" status-icon :rules="rules" ref="registerForm">
            <el-form-item label="用户名" label-width="80px" prop="username">
              <el-input type="text" v-model="registerForm.username">
              </el-input>
            </el-form-item>
            <el-form-item label="邮箱" label-width="80px" prop="email">
              <el-input type="text" v-model="registerForm.email">
              </el-input>
            </el-form-item>
            <el-form-item label="密码" label-width="80px" prop="password">
              <el-input type="password" v-model="registerForm.password">
              </el-input>
            </el-form-item>
            <el-form-item label="确认密码" label-width="80px" prop="configurePassword">
              <el-input type="password" v-model="registerForm.configurePassword">
              </el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('registerForm')">注册</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>

<script>
// import { validate } from 'json-schema';

import api from "@/api"
import { mapMutations } from "vuex"
import { h } from 'vue'
import store from "../../store"

export default {
  data() {
    //验证规则
    var validateUserName = (rule, value, callback) => {
      if (value === '') {
        callback(new Error("请输入用户名"))
      } else if (value.length < 4) {
        callback(new Error("用户名最少为4位"))
      }
      else {
        callback()
      }
    }
    var validateEmail = (rule, value, callback) => {
      const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
      if (!value) {
        return callback(new Error("请输入邮箱"));
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback();
        } else {
          callback(new Error("请输入正确的邮箱格式"));
        }
      }, 100);

    }
    var validatePassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error("请输入密码"))
      } else {
        callback()
      }
    }
    var validateConfigurePassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error("请再次输入密码"))
      } else if (value !== this.registerForm.password) {
        callback(new Error("两次密码输入不一致"))
      }
      else {
        callback()
      }
    }
    return {
      currentIndex: "login",
      loginForm: {
        username: "",
        password: "",
      },
      registerForm: {
        username: "",
        password: "",
        configurePassword: "",
        email: ""
      },
      activeTab: "login",
      rules: {
        username: [
          {
            validator: validateUserName, trriger: 'blur',
          }
        ],
        password: [
          {
            validator: validatePassword, trriger: 'blur'
          }
        ],
        configurePassword: [
          {
            validator: validateConfigurePassword, trriger: 'blur'
          }
        ],
        email: [
          {
            validator: validateEmail, trriger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    ...mapMutations("login", ["setUser"]),
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          if (this.activeTab === "login") {
            console.log(this.loginForm)
            api.login(this.loginForm).then(res => {
              console.log(res.data)
              if (res.data.code === "2000") {
                this.setUser(res.data)
                localStorage.setItem(
                  "ticket",
                  JSON.stringify(res.data)
                )
                store.commit('setAuthentication',true)
                this.$router.push('/')
              } else {
                const notification = {
                  title: "登录失败",
                  message: h(
                    "i",
                    { style: "color:teal" },
                    "用户名密码错误"
                  ),
                }
                this.$notify(notification)
              }
            })
          }
          if (this.activeTab === "register") {
            console.log(this.registerForm)
            api.register(this.registerForm).then(res => {
              if (res.data.code === "2000") {
                const notification = {
                  title: "注册成功",
                  message: h(
                    "i",
                    { style: "color:teal" },
                    "请返回首页登录"
                  ),
                }
                this.$notify(notification)
                this.$router.push('/')
              }else{
                const notification = {
                  title: "注册失败",
                  message: h(
                    "i",
                    { style: "color:teal" },
                    "请重新填写信息"
                  ),
                }
                this.$notify(notification)
              }
            })
          }
        } else {
          return;
        }
      })
    },
    handleTabsClick(tab) {
      console.log(tab.props.name)
      this.activeTab = tab.props.name
    }
  }
}
</script>

<style scoped lang="less">
.login {
  width: 500px;
  margin: 0 auto;

  .box-card {
    width: 500px auto;
    margin: 100px auto;
  }

  .el-button {
    margin: auto;
  }
}
</style>