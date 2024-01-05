<template>
    <div class="index-left-block">
        <h2 class="h2">全部演出</h2>
        <div v-for="(product, index) in showList">
            <h3>{{ product.title }}</h3>
            <ul>
                <li v-for="(item, index) in product.list" :key="index">
                    <a :href="item.url">{{ item.name }}</a>
                    <span v-if="item.hot" class="hot-tag">HOT</span>
                </li>
            </ul>
        </div>
    </div>
</template>
  
<script>

export default {
    data() {
        return {
            showList: [
                {
                    title: "演唱会",
                    list: [
                        {
                            id: 1,
                            name: "张云雷“歌者·启程“巡回演唱会上海站",
                            url: "",
                            hot: true
                        },
                        {
                            id: 2,
                            name: "马思唯“黑马季节Dark Horse Season”巡回演唱会-武汉站",
                            url: "",
                            hot: false
                        }, {
                            id: 3,
                            name: "郎朗音乐盛典",
                            url: "",
                            hot: false
                        },
                    ]
                },
                {
                    title: "话剧歌剧",
                    list: [
                        {
                            id: 1,
                            name: "开心麻花✖百老汇2024贺岁大戏《婚礼歌手》",
                            url: "",
                            hot: true
                        },
                        {
                            id: 2,
                            name: "话剧：《正红旗下》",
                            url: "",
                            hot: false
                        }, {
                            id: 3,
                            name: "开心麻花2024爆笑贺岁大戏《这家伙不赖》",
                            url: "",
                            hot: false
                        },
                    ]
                },
                {
                    title: "音乐会",
                    list: [
                        {
                            id: 1,
                            name: "欧阳娜娜·初星Stardust古典跨界巡回音乐会-广州站",
                            url: "",
                            hot: true
                        },
                        {
                            id: 2,
                            name: "郎朗钢琴元宇宙暨郎朗钢琴盛典",
                            url: "",
                            hot: true
                        }, {
                            id: 3,
                            name: "春节序曲”经典名曲——北京新春交响音乐会",
                            url: "",
                            hot: false
                        },
                    ]
                },
                {
                    title: "展览休闲",
                    list: [
                        {
                            id: 1,
                            name: "X美术馆冬季三联展",
                            url: "",
                            hot: false
                        },
                        {
                            id: 2,
                            name: "永久的当下：斯蒂芬·肖尔回顾展",
                            url: "",
                            hot: false
                        }, {
                            id: 3,
                            name: "天生我材·李白——中国古诗词新媒体艺术系列展",
                            url: "",
                            hot: true
                        },
                    ]
                },
                {
                    title: "舞蹈芭蕾",
                    list: [
                        {
                            id: 1,
                            name: "中央芭蕾舞团《灰姑娘》",
                            url: "",
                            hot: false
                        },
                        {
                            id: 2,
                            name: "“为人民而舞”-《舞动经典》",
                            url: "",
                            hot: false
                        }, {
                            id: 3,
                            name: "大型民族舞剧《醒·狮》",
                            url: "",
                            hot: true
                        },
                    ]
                },
            ]
        }
    }
}
</script>
  
<style scoped lang="less">




.index-left-block {
    margin: 15px;
    background: #fff;
    box-shadow: 0 0 1px #ddd;
}

.index-left-block .hr {
    margin-bottom: 20px;
    height: 1px;
    background: #ddd;
    width: 100%;
}

.index-left-block .h2 {
    background: #4fc08d !important;
    color: #fff;
    padding: 10px 15px;
    margin-bottom: 20px;
}

.index-left-block .h3 {
    padding: 5px 15px 5px 15px;
    font-weight: bold;
    color: #222;
}

.index-left-block ul {
    padding: 10px 15px;
}

.index-left-block li {
    padding: 5px;

    a {
        color: #222;
    }
}

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

/* .index-board-open .index-board-item-inner {
    background: url(../../../assets/01.png) no-repeat;
}

.index-board-logo .index-board-item-inner {
    background: url(../../../assets/02.png) no-repeat;
}

.index-board-golife .index-board-item-inner {
    background: url(../../../assets/03.png) no-repeat;
}

.index-board-heigh .index-board-item-inner {
    background: url(../../../assets/04.png) no-repeat;
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
} */

.hot-tag {
    background: red;
    color: #fff;
}

/* .new-item {
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
} */
</style>    