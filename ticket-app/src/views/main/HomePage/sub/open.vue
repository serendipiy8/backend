<template>
    <div class="open">
        <div class="sales-board">
            <div class="sales-board-intro">
                <h2>郎朗音乐盛典</h2>
                <p>2024年2月4日，正值新春到来之际，郎朗将在北京华熙live五棵松举办个人音乐盛典，邀你一起奏响春天的乐章，用音乐的方式迎接新春的美好华章，同时，此次官宣也公布了北京场的嘉宾——许嵩！
                    二人曾在央视《经典咏流传》的舞台上合作演绎该节目主题曲《心有所向》，用音乐诠释青春，给观众们留下了深刻印象。此次，两人将再度同台演奏、献唱，强强联手，一定是一场精彩绝伦的音乐盛宴！
                </p>
            </div>
            <div class="sales-board-form">
                <div class="sales-board-line-left">购买数量：</div>
                <div class="sales-board-line-right">
                    <Counter></Counter>
                </div>
            </div>
            <div class="sales-board-form">
                <div class="sales-board-line-left">票档：</div>
                <div class="sales-board-line-right">
                    <Type></Type>
                </div>
            </div>
            <div class="sales-board-form">
                <div class="sales-board-line-left">购买数量：</div>
                <div class="sales-board-line-right">加减操作</div>
            </div>
        </div>

        <div class="sales-board-des">
            <h3>购票须知</h3>
            <ul>
                <li>每笔订单最多购买4张、每个账号最多购买4张。</li>
                <li>支持多种票品验票后入场，如证件电子票。</li>
                <li>本项目支持有条件退款，若需要收取退票手续费，将以用户实际支付票款为基准收取。</li>
                <li>儿童一律凭票入场</li>
            </ul>
            <h3>观演须知</h3>
            <ul>
                <li>演出时长约90分钟</li>
                <li>请于演出前约120分钟入场</li>
                <li>请携带有效证件入场</li>
                <li>请勿携带食品、酒水等物品入场</li>
            </ul>
        </div>
    </div>
</template>

<script>
import Counter from '@/components/HomePage/counter.vue'
import Type from'@/components/HomePage/type.vue'

export default {
    name: 'Open',
    data() {
        return {
            
        }
    },
    components: {
        Counter,
        Type
    },
}
</script>

<style scoped>
.open {
    text-align: left;
}

.buy-dialog-title {
    font-size: 16px;
    font-weight: bold;
}

.buy-dialog-btn {
    margin-top: 20px;
}

.buy-dialog-table {
    width: 100%;
    margin-bottom: 20px;
}

.buy-dialog-table td,
.buy-dialog-table th {
    padding: 5px 0;
    border: 1px solid #e3e3e3;
    text-align: center;
}

.buy-dialog-table th {
    background: #4fc08d;
    color: #fff;
    border: 1px solid #4fc08d;
}

.button {
    background: #4fc08d;
    color: #fff;
    padding: 10px 20px;
    display: inline-block;
    cursor: pointer;
}
</style>