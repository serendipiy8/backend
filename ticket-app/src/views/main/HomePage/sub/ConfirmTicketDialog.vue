<!-- ConfirmTicketDialog.vue -->
<template>
    <div>
      <div>
        <p>支付信息：{{ paymentInfo }}</p>
        <img :src="qrCode" alt="二维码">
      </div>
      <button @click="handlePaymentComplete">支付完成</button>
      <button @click="handleCancel">取消</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    props: {
      paymentInfo: String,
      qrCode: String,
      orderID: {
        type:Number,
            default:function(){
                return [
                    {
                        value:1,
                    }
                ]
            }
      },
    },
    methods: {
      handlePaymentComplete() {
        const formData = new URLSearchParams();
        formData.append('OrderID', this.orderID);
        formData.append('OrderStatus', '已支付');
        

        console.log(formData);
        
        axios.put('http://39.106.37.28:5000/orders', formData)
          .then(response => {
            // 处理后端返回的数据
            console.log('支付完成', response.data);
            this.$emit('paymentComplete');
          })
          .catch(error => {
            // 处理错误
            console.error('支付完成失败', error);
          });
      },
      handleCancel() {
        this.$emit('cancel');
      },
    },
  };
  </script>
  