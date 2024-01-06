<!-- <template>
  <div>
    <order-table :response-data="responseData"
      :table-headers="['Order ID', 'Order Status', 'Purchase Time', 'Quantity', 'Ticket ID', 'User ID']"
      :table-fields="['OrderID', 'OrderStatus', 'PurchaseTime', 'Quantity', 'TicketID', 'UserID']"
      :unique-key="'OrderID'"></order-table>
  </div>
</template>

<script>
import OrderTable from "@/components/OrderTable.vue";
import axios from 'axios';

export default {
  components: {
    OrderTable,
  },
  data() {
    return {
      responseData: {
        code: "2000",
        data: [],
        message: "successfully!",
      },
      userID: '0',
    };
  },
  mounted() {
    // Make the GET request to the backend API
    this.fetchData();
  },
  methods: {
    fetchData() {
      // 
      // const url = `http://127.0.0.1:5000/orders/queryUser?UserID=${encodeURIComponent(this.userID)}`;
      const url = 'http://127.0.0.1:5000//Orders';
      fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      })
        .then(response => response.json())
        .then(data => {
          console.log('Response from backend:', data); 
          this.responseData.data =data.data || [];
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
  }
};
</script> -->



<template>
  <HeaderNav></HeaderNav>
  <div class="order">
    <ProductList></ProductList>
    <ProductPagination></ProductPagination>
  </div>
</template>

<script>

import HeaderNav from '@/components/HeaderNav.vue';
import ProductList from './ProductList.vue';
import ProductPagination from './ProductPagination.vue';
export default {
  components: {
    HeaderNav,
    ProductList,
    ProductPagination
  },
  data() {
    return {}
  },

}
</script>

<style scoped>
.order {
  width: 1200px;
  margin: 0 auto;
  padding-top: 15px;
}
</style>