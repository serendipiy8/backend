<template>
    <div class="chooser-component">
        <ul class="chooser-list">
            <li :class="{active:nowIndex === index}" v-for="(item,index) in timerDate" :key="index" @click="timerHandle(item,index)">
                {{ item.value }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data(){
        return{
            nowIndex:0,
            timerDate:[
                {
                    value:'2021-06-01',
                    id:1
                },
                {
                    value:'2021-07-01',
                    id:2
                },
                {
                    value:'2021-08-01',
                    id:3
                },
            ]
        }

    },
    methods:{
            timerHandle(item,index){
                this.nowIndex = index;
                this.$emit('timer',item);
            }
        
        }
};
</script>

<style scoped>

.chooser-component {
    position: relative;
    display: inline-block;
}

.chooser-list li {
    display: inline-block;
    border: 1px solid #e3e3e3;
    height: 25px;
    line-height: 25px;
    padding: 0 8px;
    margin-right: 5px;
    border-radius: 3px;
    text-align: center;
    cursor: pointer;
}

.chooser-list li.active {
    border-color: #4fc08d;
    background: #4fc08d;
    color: #fff;
}
</style>