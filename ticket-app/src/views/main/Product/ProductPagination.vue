<template>
  <div>
    <el-pagination layout="prev, pager, next ,jumper" :total="100" @size-change="handleSizechange"
      @current-change="handleCurrentChange" :current-page.sync="currentPage">

    </el-pagination>
  </div>
</template>
  
<script>

export default {
  components: {
  },
  data() {
    return {
      currentPage: 1
    }
  },
  methods: {
    handleSizechange() {
    },
    handleCurrentChange(val) {
      console.log(val)
    }
  }
}
</script>
  
<style></style>