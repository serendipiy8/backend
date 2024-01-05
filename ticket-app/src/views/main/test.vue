<template>
    <div>
      <!-- 导航栏 -->
      <header>
        <img src="../../assets/logo.png" alt="Logo" />
        <nav>
          <router-link to="/">首页</router-link>
          <router-link to="/categories">分类</router-link>
          <input type="text" v-model="searchKeyword" placeholder="搜索" />
          <button @click="search">搜索</button>
          <router-link v-if="!loggedIn" to="/login">登录</router-link>
          <router-link v-if="!loggedIn" to="/login">注册</router-link>
          <button v-if="loggedIn" @click="logout">注销</button>
        </nav>
      </header>
  
      <!-- 轮播图 -->
      <carousel>
        <!-- 轮播项 -->
        <carousel-item v-for="(item, index) in carouselItems" :key="index">
          <img :src="item.image" alt="Carousel Item" />
        </carousel-item>
      </carousel>
  
      <!-- 演唱会列表 -->
      <section class="concerts">
        <div v-for="(concert, index) in concerts" :key="index" class="concert">
          <img :src="concert.poster" alt="Concert Poster" />
          <div class="details">
            <h3>{{ concert.name }}</h3>
            <p>日期: {{ concert.date }}</p>
            <p>地点: {{ concert.location }}</p>
            <p>价格: {{ concert.price }}</p>
            <button @click="buyTicket(concert)">购票</button>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchKeyword: '',
        loggedIn: false, // 根据实际情况处理登录状态
        carouselItems: [
          { image: 'https://gw.alicdn.com/tfs/TB1KiMMq7L0gK0jSZFtXXXQCXXa-1200-320.png' },
          // { image: '../../assets/1.png' },
          // Add more carousel items as needed
        ],
        concerts: [
          {
            name: '演唱会1', 
            poster: 'https://img.alicdn.com/bao/uploaded/i1/2251059038/O1CN01vQlt0k2GdSXWKrrk9_!!2-item_pic.png_q60.jpg_.webp',
            date: '2023-01-01',
            location: '演唱会地点1',
            price: '$50',
          },
          {
            name: '演唱会2',
            poster: 'https://img.alicdn.com/bao/uploaded/i3/2251059038/O1CN01gsB4WE2GdSXgarchv_!!2-item_pic.png_q60.jpg_.webp',
            date: '2023-02-01',
            location: '演唱会地点2',
            price: '$60',
          },
          // Add more concert items as needed
        ],
      };
    },
    methods: {
      search() {
        // 处理搜索逻辑
        console.log('Search for:', this.searchKeyword);
      },
      logout() {
        // 处理注销逻辑
        this.loggedIn = false;
      },
      buyTicket(concert) {
        // 处理购票逻辑
        console.log('Buy ticket for:', concert.name);
      },
    },
  };
  </script>
  
  <style scoped>
  /* 添加样式以美化页面 */
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    background-color: #333;
    color: white;
  }
  
  nav {
    display: flex;
    align-items: center;
  }
  
  nav a {
    margin: 0 10px;
    color: white;
    text-decoration: none;
  }
  
  input, button {
    margin: 0 10px;
  }
  
  carousel {
    width: 100%;
    overflow: hidden;
  }
  
  carousel-item {
    width: 100%;
    display: inline-block;
  }
  
  .concerts {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    margin: 20px;
  }
  
  .concert {
    margin: 20px;
  }
  
  .concert img {
    max-width: 40%;
    height: auto;
  }
  
  .details {
    text-align: center;
  }
  
  button {
    background-color: #007BFF;
    color: white;
    padding: 10px;
    cursor: pointer;
    border: none;
  }
  </style>
  

