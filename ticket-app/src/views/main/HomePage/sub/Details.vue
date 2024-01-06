<template>
    <div class="show-details">
        <div class="show-header">
            <h1>{{ show.title }}</h1>
            <p>{{ show.date }}</p>
        </div>
        <div class="show-content">
            <img :src="show.image" alt="Show Image" />
            <p>{{ show.description }}</p>
            <div class="ticket-info">
                <h2>Ticket Information</h2>
                <p>{{ show.ticketPrice }}</p>
                <p>{{ show.ticketAvailability }}</p>
                <button @click="buyTicket">Buy Ticket</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            show: {
                title: 'Show Title',
                date: 'Show Date',
                image: 'show-image.jpg',
                description: 'Show Description',
                ticketPrice: 'Ticket Price',
                ticketAvailability: 'Ticket Availability',
            },
        };
    },
    methods: {
        buyTicket() {
            // Handle ticket purchase logic here
        },
    },
};
</script>

<style scoped>
.show-details {
    padding: auto;
}

.show-header {
    padding: auto;
}

.show-content {
    padding: auto;
}

.ticket-info {
    padding: auto;
}
</style>
