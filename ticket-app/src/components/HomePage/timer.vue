<template>
    <div class="chooser-component">
        <ul>
            <li v-for="(item,index) in timerDate" :key="index">
                {{ item.value  }}
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data(){
        return{
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

chooser-list li.active {
    border-color: #4fc08d;
    background: #4fc08d;
    color: #fff;
}
</style>