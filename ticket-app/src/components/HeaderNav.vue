<template>
    <el-menu :default-active="activeIndex" 
    class="el-menu" mode="horizontal" 
    @select="handleSelect"
        background-color="#545c64" 
        text-color="#fff" 
        active-text-color="#ffd04b"
        router>
        <el-menu-item index="/">首页</el-menu-item>
        <el-menu-item index="/concert">演出</el-menu-item>
        <el-sub-menu index="3">
            <template #title>票务</template>
            <el-menu-item index="3-1">选项1</el-menu-item>
            <el-menu-item index="3-2">选项2</el-menu-item>
        </el-sub-menu>
        <div class="flex-grow" />
        <el-menu-item index="login">登录</el-menu-item>
        <el-menu-item index="login">注册</el-menu-item>
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
    },
};
</script>
  
<style>
.flex-grow {
    flex-grow: 1;
}
</style>
  