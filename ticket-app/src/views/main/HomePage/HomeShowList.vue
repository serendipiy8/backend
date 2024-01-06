<template>
    <div class="index-board-list">
        <div class="index-board-item" v-for="(item, index) in buyData" :key="index"
            :class="['index-board-' + item.flag, { 'line-last': index % 2 !== 0 }]">
            <div class="index-board-item-inner">
                <h2>{{ item.title }}</h2>
                <p>{{ item.desc }}</p>
                <div class="index-board-button">
                    <router-link :to="'/concert/'+item.flag" class="button">查看详情</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomeShowList',
    data() {
        return {
            buyData: [
                {
                    title: "音乐会",
                    desc: "音乐会描述",
                    flag: "open",
                },
                {
                    title: "演唱会",
                    desc: "演唱会描述",
                    flag: "logo",
                },
                {
                    title: "歌剧话剧",
                    desc: "歌剧话剧描述",
                    flag: "golife",
                },
                {
                    title: "曲苑杂坛",
                    desc: "曲苑杂坛描述",
                    flag: "heigh",
                },
            ]
        }
    }
}
</script>

<style scoped>
.index-board-list {
    overflow: hidden;
    margin-top: 15px;
}

.index-board-item {
    float: left;
    width: 400px;
    padding: 20px;
    background: #fff;
    box-shadow: 0 0 1px #ddd;
    padding: 20px;
    margin-right: 20px;
    margin-bottom: 20px;
}

.index-board-item-inner {
    min-height: 125px;
    padding-left: 120px;
}

.index-board-open .index-board-item-inner {
    background: url(https://img.alicdn.com/bao/uploaded/https://img.alicdn.com/imgextra/i3/2251059038/O1CN01tQ7x1y2GdSYI5d9jg_!!2251059038.jpg) no-repeat;
    background-size: 100px 140px;
}

.index-board-logo .index-board-item-inner {
    background: url(../../../assets/concert2.png) no-repeat;
}

.index-board-golife .index-board-item-inner {
    background: url(https://img.alicdn.com/bao/uploaded/https://img.alicdn.com/imgextra/i3/2251059038/O1CN01QCVZD22GdSYBYkOYd_!!2251059038.jpg_q60.jpg_.webp) no-repeat;
    background-size: 100px 140px;
}

.index-board-heigh .index-board-item-inner {
    background: url(../../../assets/concert4.png) no-repeat;
}

.index-board-item h2 {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 15px;
    color: #000;
}

.line-last {
    margin-right: 0;
}

.index-board-button {
    margin-top: 20px;
}

.lastest-news {
    min-height: 350px;
}

.new-item {
    display: inline-block;
    width: 230px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.button {
    background: #4fc08d;
    color: #fff;
    display: inline-block;
    padding: 10px 20px;
    cursor: pointer;
}
</style>


