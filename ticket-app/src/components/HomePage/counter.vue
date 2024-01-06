<template>
    <div class="counter-component">
        <div class="counter-btn" @click="minHandle"> - </div>
        <div class="counter-show">
            <input type="text" @keyup="inputHandle" v-model="counter" />
        </div>
        <div class="counter-btn" @click="addHandle"> + </div>
    </div>
</template>

<script>
// import VueAxios from 'vue-axios';
import axios from 'axios';

export default {
    name: 'Counter',
    data() {
        return {
            counter: 1,
            maxCounter: 1,
        };
    },
    methods: {
        addHandle() {
            if (this.counter >= this.maxCounter) return;
            this.counter++;
        },
        minHandle() {
            if (this.counter <= 1) return;
            this.counter--;
        },
        inputHandle() {
            var fix;
            if (typeof this.counter === 'string') {
                fix = Number(this.counter.replace(/\D/g, ""));
            } else {
                fix = 1;
            }
            this.counter = fix;
            // 额外逻辑
            if (this.counter < 1)
                this.counter = 1;
            if (this.counter > this.maxCounter)
                this.counter = this.maxCounter;

        }
    },
    created: async function () {
        const response = await axios.get('http://39.106.37.28:5000/Ticketprices');
        this.maxCounter = response.data?.data?.[0].RemainingQuantity;// 假设响应的数据就是你需要的最大计数器值
        if (this.maxCounter !== undefined) {
            console.log(this.maxCounter);
        } else {
            console.error("RemainingQuantity is undefined in the response data.");
        }
        console.log(response.data);
    },
};
</script>

<style scoped>
.counter-component {
    position: relative;
    display: inline-block;
    overflow: hidden;
    vertical-align: middle;
}

.counter-show {
    float: left;
}

.counter-show input {
    border: none;
    border-top: 1px solid #e3e3e3;
    border-bottom: 1px solid #e3e3e3;
    height: 25px;
    line-height: 25px;
    width: 30px;
    outline: none;
    text-indent: 4px;
}

.counter-btn {
    border: 1px solid #e3e3e3;
    float: left;
    height: 25px;
    line-height: 25px;
    text-align: center;
    cursor: pointer;
    width: 15px;
}

.counter-btn hover {
    background: #4fc08d;
    color: #fff;
    border-color: #4fc08d;
}
</style>
