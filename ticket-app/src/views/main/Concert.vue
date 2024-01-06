<template>
  <HeaderNav></HeaderNav>
  <div class="detail-wrap">
    <div class="detail-left">
      <div class="product-board">
        <img src="../../assets/logo.jpg" alt="">
        <ul>
          <router-link tag="li" active-class="active" v-for="(item, index) in showNav" :key="index"
            :to="'/concert/' + item.id">
            {{ item.title }}
          </router-link>
        </ul>
      </div>
    </div>
    <div class="detail-right">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import HeaderNav from '@/components/HeaderNav.vue';
export default {
  components: {
    HeaderNav,
  },
  data() {
    return {
      showNav: [
        {
          title: "音乐会",
          id: "open",
        },
        {
          title: "演唱会",
          id: "logo",
        },
        {
          title: "歌剧话剧",
          id: "golife",
        },
        {
          title: "曲苑杂坛",
          id: "heigh",
        },
      ]
    }

  },
  methods: {

  },
};
</script>

<style>
.detail-wrap {
  width: 1200px;
  margin: 0 auto;
  overflow: hidden;
  padding-top: 20px;
}

.detail-left {
  float: left;
  width: 200px;
  text-align: center;
}

.detail-right {
  float: left;
  width: 980px;
  margin-left: 20px;
}

.product-board {
  background: #fff;
  padding: 20px 0;
}

.product-board ul {
  margin-top: 20px;
}

.product-board a {
  text-align: left;
  padding: 10px 15px;
  cursor: pointer;
}

.product-board a.active,
.product-board a:hover {
  background: #4fc08d;
  color: #fff;
}

.product-board a {
  display: block;
}

.sales-board {
  background: #fff;
}

/* .sales-board-form {} */

.sales-board-intro h2 {
  font-size: 20px;
  padding: 20px;
}

.sales-board-intro p {
  background: #f7fcff;
  padding: 10px 20px;
  color: #999;
  line-height: 1.8;
}

.sales-board-form {
  padding: 10px 20px;
  font-size: 14px;
}

.sales-board-line {
  clear: both;
  padding-bottom: 20px;
}

.sales-board-line-left {
  display: inline-block;
  /* width: 100px; */
  margin-right: 10px;
}

.sales-board-line-right {
  display: inline-block;
  width: 75%;
}

.sales-board-des {
  border-top: 20px solid #fff;
  background: #fff;
  padding: 15px 20px;
}

.sales-board-des p {
  line-height: 1.6;
}

.sales-board-des h2 {
  font-size: 20px;
  padding-bottom: 15px;
}

.sales-board-des h3 {
  font-size: 20px;
  font-weight: bold;
  padding: 20px 0 10px 0;
}

.sales-board-des li {
  padding: 5px 0;
}

.sales-board-table {
  width: 100%;
  margin-top: 20px;
}

.sales-board-table th {
  background: #4fc08d;
  color: #fff;
}

.sales-board-table td {
  border: 1px solid #f0f2f5;
  padding: 15px;
}
</style>
