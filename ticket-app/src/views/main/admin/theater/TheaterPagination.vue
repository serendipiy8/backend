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
        UserID: "",
      },
      count: 0,
      total: 1,
    }
  },
  computed: {
    ...mapGetters('login', ['getUserID']),
    ...mapState('login', ['user']),
  },
  methods: {
    handleSizechange() {
    },
    handleCurrentChange(val) {
      // console.log(val)
      eventBus.emit('changePage', val)
    },
  },
  mounted() {
    // this.Form.UserID = this.getUserID;
    this.$api.selectRefund(this.Form).then(res => {
      console.log(res.data)
      if (res.data.code == 2000) {
        this.total = res.data.totalPage * 10
        this.count = res.data.totalCount
      }
    })
  }
}
</script>
  
<style></style>