<template>
  <div>
    <el-pagination layout="prev, pager, next ,jumper" :total="total" @size-change="handleSizechange"
      @current-change="handleCurrentChange" v-model="currentPage">

    </el-pagination>
  </div>
</template>
  
<script>
import eventBus from "@/utils/eventBus.js";
import { mapState, mapGetters } from 'vuex';
export default {
  components: {
  },
  data() {
    return {
      currentPage: 1,
      Form: {
        TheaterID: "",
      },
      count: 0,
      total: 1,
    }
  },
  computed: {
    // ...mapGetters('login', ['getUserID']),
    // ...mapState('login', ['user']),
  },
  mounted() {
    // this.Form.UserID = this.getUserID;
    const onAddSuccessHandler = this.onAddSuccessHandler;
    const deleteSuccessHandler = this.deleteSuccessHandler;
    eventBus.on("onAddSuccess", onAddSuccessHandler);
    eventBus.on("deleteSuccess", deleteSuccessHandler);
    this.$api.selectTheater(this.Form).then(res => {
      console.log(res.data)
      if (res.data.code == 2000) {
        this.total = res.data.totalPage * 10
        this.count = res.data.totalCount
      }
    })
  },
  methods: {
    handleSizechange() {
    },
    handleCurrentChange(val) {
      // console.log(val)
      eventBus.emit('changePage', val)
    },
    onAddSuccessHandler() {
      this.$api.selectTheater(this.Form).then(res => {
        console.log(res.data)
        if (res.data.code == 2000) {
          this.total = res.data.totalPage * 10
          this.count = res.data.totalCount
        }
      })
    },
    deleteSuccessHandler() {
      this.$api.selectTheater(this.Form).then(res => {
        console.log(res.data)
        if (res.data.code == 2000) {
          this.total = res.data.totalPage * 10
          this.count = res.data.totalCount
        }
      })
    }
  },
}
</script>
  
<style></style>