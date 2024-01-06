<template>
    <div class="counter-component">
        <div class="counter-btn" @click="minHandle"> - </div>
        <div class="counter-show">
            <input type="text" v-model="counter" />
        </div>
        <div class="counter-btn" @click="addHandle"> + </div>
    </div>
</template>

<script>
export default {
    name: 'Counter',
    data() {
        return {
            counter: 1,
        };
    },
    methods: {
        addHandle() {
            this.counter++;
        },
        minHandle() {
            if (this.counter <= 1) return;
            this.counter--;
        },
    }
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
}</style>
