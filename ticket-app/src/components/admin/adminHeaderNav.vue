<template>
    <el-menu :default-active="activeIndex" class="el-menu" mode="horizontal" @select="handleSelect" router>
        <el-menu-item index="/admin/adminticket">售票管理</el-menu-item>
        <el-menu-item index="/admin/theater">剧院管理</el-menu-item>
        <el-menu-item index="/admin/adminrefund">退票管理</el-menu-item>
        <el-menu-item index="/admin/adminorder">订单查询</el-menu-item>

        <div class="flex-grow" />
        <el-menu-item index="/adlogin">登录</el-menu-item>
        <el-sub-menu index="3">
            <template #title>管理员中心</template>
            <el-menu-item index="">管理员信息</el-menu-item>
            <el-menu-item index="/admin" @click="logoutHandle">注销</el-menu-item>
        </el-sub-menu>
    </el-menu>
</template>
  
<script>
export default {
    data() {
        return {
            activeIndex: "1",
        };
    },
    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        },
        logoutHandle() {
            this.$store.dispatch('logout');
            // this.$router.push("/login")
        }
    },
};
</script>
  
<style>
.flex-grow {
    flex-grow: 1;
}
</style>
  