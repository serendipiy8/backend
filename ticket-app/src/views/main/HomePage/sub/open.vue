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
                    <Type :selecterData="selecterData"></Type>
                </div>
            </div>
            <div class="sales-board-form">
                <div class="sales-board-line-left">场次</div>
                <div class="sales-board-line-right">
                    <Timer :timerData="timerData"></Timer>

                </div>
            </div>
            <button @click="showTicketDialog">购票</button>
            <TicketDialog :visible="ticketDialogVisible" :timerData="timerData" :selecterData="selecterData"
                :username="username" @confirm="handleConfirmTicket" @close="handleCloseTicket">
            </TicketDialog>
            <ConfirmTicketDialog v-if="showConfirmDialog" :paymentInfo="paymentInfo" :qrCode="qrCode" :orderID="orderID"
                @paymentComplete="handlePaymentComplete" @cancel="handleCancel" />
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
import Type from '@/components/HomePage/type.vue'
import Timer from '@/components/HomePage/timer.vue'
import TicketDialog from './TicketDialog.vue'
import axios from 'axios';
import ConfirmTicketDialog from './ConfirmTicketDialog.vue';

export default {
    name: 'Open',
    data() {
        return {
            selecterData: [
                {
                    value: "内场前排",
                    id: 1
                },
                {
                    value: "内场后排",
                    id: 2
                },
                {
                    value: "看台前排",
                    id: 3
                },
                {
                    value: "看台后排",
                    id: 4
                },
                {
                    value: "山顶位置",
                    id: 5
                }
            ],
            timerData: [
                {
                    value: '2021-06-01',
                    id: 1
                },
                {
                    value: '2021-07-01',
                    id: 2
                },
                {
                    value: '2021-08-01',
                    id: 3
                },
            ],
            ticketDialogVisible: false,
            username: this.$store.state.login.user.data.username,
            selectedTimer: null,
            selectedQuantity: 1,
            selectedType: null,
            postData: {
                UserID: String(666666),
                TicketID: String(32434),
                // timerData: ticketInfo.timerData,
                PurchaseTime: new Date().toLocaleString(),
                OrderStatus: "已支付",
                Quantity: String(1),
            },
            showConfirmDialog: false,
            paymentInfo: '', // 从后端获取的支付信息
            qrCode: '',
            orderID: ''// 从后端获取的二维码链接
        }
    },
    components: {
        Counter,
        Type,
        Timer,
        TicketDialog,
        ConfirmTicketDialog,
    },
    methods: {
        showTicketDialog() {
            // 设置购票信息
            this.username = this.$store.state.login.user.data.username
            console.log(this.username)// 设置默认值
            this.selectedTimer = null; // 设置默认值
            this.selectedQuantity = 1; // 设置默认值
            this.selectedType = null; // 设置默认值

            // 弹出购票对话框
            this.ticketDialogVisible = true;
        },

        handleConfirmTicket(ticketInfo) {
            // 处理确认购票逻辑，你可以在这里调用后端接口提交购票信息
            console.log("确认购票", ticketInfo);
            // 获取当前时间
            const currentDate = new Date();

            // 提取年、月、日
            const year = currentDate.getFullYear();
            const month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); // 月份是从0开始的，因此要加1
            const day = currentDate.getDate().toString().padStart(2, '0');

            // 构建年月日字符串
            const formattedDate = `${year}-${month}-${day}`;

            console.log(formattedDate);

            // 创建一个空的 URLSearchParams 对象
            const formData = new URLSearchParams();

            // 添加键值对到对象中
            formData.append('UserID', this.postData.UserID);
            formData.append('TicketID', this.postData.TicketID);
            formData.append('PurchaseTime', this.postData.PurchaseTime);
            formData.append('OrderStatus', '未支付');
            formData.append('Quantity', this.postData.Quantity);
            // ... 添加其他键值对

            // 使用 fetch 发送 POST 请求
            fetch('http://39.106.37.28:5000/orders', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    console.log('请求成功', data);
                    this.showConfirmDialog = true;
                    this.paymentInfo = data.data.OrderStatus;
                    this.qrCode = "https://img2.baidu.com/it/u=1443929167,3597244248&fm=253&fmt=auto&app=138&f=GIF?w=150&h=150";
                    this.orderID = data.data.OrderID;
                })
                .catch(error => {
                    console.error('请求失败', error);
                });

            this.ticketDialogVisible = false;


        },

        handleCloseTicket() {
            // 处理取消购票逻辑
            console.log("取消购票");

            // 关闭购票对话框
            this.ticketDialogVisible = false;
        },



        handlePaymentComplete() {
            // 支付完成后的处理，可以关闭对话框或执行其他操作
            this.showConfirmDialog = false;
            // 在这里可以进行支付完成后的其他逻辑处理
        },
        handleCancel() {
            // 取消按钮的处理，可以关闭对话框或执行其他操作
            this.showConfirmDialog = false;
        },
    }
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