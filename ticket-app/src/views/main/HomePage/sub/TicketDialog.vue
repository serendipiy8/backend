<template>
    <div class="ticket-dialog" v-show="visible">
        <div class="dialog-content">
            <label for="username">用户名：</label>
            <input type="text" v-model="username" id="username" />

            <label for="selectedTimer">场次：</label>
            <select v-model="selectedTimer" id="selectedTimer">
                <option v-for="(timer, index) in timerData" :key="index" :value="timer">
                    {{ timer.value }}
                </option>
            </select>

            <label for="selectedQuantity">购票数量：</label>
            <input type="number" v-model="selectedQuantity" id="selectedQuantity" />

            <label for="selectedType">票档：</label>
            <select v-model="selectedType" id="selectedType">
                <option v-for="(type, index) in selecterData" :key="index" :value="type">
                    {{ type.value }}
                </option>
            </select>

            <button @click="confirmTicket">确认</button>
            <button @click="cancelTicket">取消</button>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        visible: Boolean,
        timerData: Array,
        selecterData: Array,
        username: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            username: this.$store.state.login.user.data.username,
            selectedTimer: null,
            selectedQuantity: 1,
            selectedType: null,
        };
    },
    methods: {
        confirmTicket() {
            console.log(this.selecterData);
            // 处理确认购票逻辑
            this.$emit('confirm', {
                username: this.username,
                selectedTimer: this.timerData[0].value,
                selectedType: this.selecterData[0].value,
                UserID: String(666666),
                TicketID: String(32434),
                // timerData: ticketInfo.timerData,
                PurchaseTime: new Date().toLocaleString(),
                OrderStatus: "已支付",
                Quantity: this.selectedQuantity,
            });

            // 关闭购票对话框
            this.$emit('close');
        },
        cancelTicket() {
            // 处理取消购票逻辑
            this.$emit('close');
        },
    },
};
</script>

<style scoped>
.ticket-dialog {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    padding: 20px;
    border: 1px solid #ccc;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}

.dialog-content {
    display: flex;
    flex-direction: column;
}

label {
    margin-bottom: 5px;
}
</style>
