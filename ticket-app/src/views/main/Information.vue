<template>
  <HeaderNav></HeaderNav>
  <h1>个人信息</h1>
  <div class="form">
    <el-form label-width="90px" :model="editorForm" ref="addForm">
      <el-form-item label="真实姓名">
        <el-input v-model="editorForm.RealName"></el-input>
      </el-form-item>
      <el-form-item label="性别">
        <el-input v-model="editorForm.Gender"></el-input>
      </el-form-item>
      <el-form-item label="身份证号">
        <el-input v-model="editorForm.IDcard"></el-input>
      </el-form-item>
      <el-form-item label="住址">
        <el-input v-model="editorForm.Address"></el-input>
      </el-form-item>
      <el-form-item label="电话号码">
        <el-input v-model="editorForm.Account"></el-input>
      </el-form-item>
      <el-form-item label="电子邮箱">
        <el-input v-model="editorForm.Email"></el-input>
      </el-form-item>
    </el-form>
    <el-button @click="dialogVisible = false">取消</el-button>
    <el-button type="primary" @click="editorSubmit">
      确定
    </el-button>
  </div>
</template>

<script>
import { ref, onBeforeUnmount } from 'vue';
import { ElMessageBox } from 'element-plus'
import eventBus from "@/utils/eventBus.js";
const dialogVisible = ref(false)
import { mapState, mapGetters } from 'vuex';
const qs = require('qs');
import HeaderNav from '@/components/HeaderNav.vue'
export default {
  components: {
    HeaderNav
  },
  computed: {
    ...mapGetters('login', ['getUserID']),
    ...mapState('login', ['user']),
  },
  mounted() {
    this.editorForm.UserID = this.getUserID;
    console.log(this.editorForm.UserID)
    this.$api.getUser(this.editorForm).then((res) => {
        if (res.data.code == 2000) {
          this.editorForm.RealName = res.data.data.RealName;
          this.editorForm.Gender = res.data.data.Gender;
          this.editorForm.IDcard = res.data.data.IDCard;
          this.editorForm.Address = res.data.data.Address;
          this.editorForm.Account = res.data.data.Account;
          this.editorForm.Email = res.data.data.Email;
          this.$message({
            message: "请求成功",
            type: "success"
          });
        } else {
          this.$message({
            message: "请求失败",
            type: "error"
          });
        }
      });

  },
  methods: {
    editorSubmit() {
      // this.editorForm.AdminID = this.getAdminID
      const formData = qs.stringify(this.editorForm);
      console.log(formData)
      this.$api.editorUser(formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }).then((res) => {
        console.log(res.data);
        if (res.data.code == 2000) {
          this.$message({
            message: "编辑成功",
            type: "success"
          });
        } else {
          this.$message({
            message: "编辑失败",
            type: "error"
          });
        }
      });
    }
  },
  data() {
    return {
      editorForm: {
        RealName: "",
        Gender: "",
        IDcard: "",
        Address: "",
        Account: "",
        Email: "",
        UserID: "",
      }
    }
  }
}

</script>

<style scoped>
.form {
  width: 1000px;
  margin: 20px auto;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.el-form-item {
  padding-top: 10px;
  padding: 5px;
}

.el-button {
  margin-bottom: 20px;
}

.el-input {
  margin-left: 20px;
  width: 820px;
}
</style>
