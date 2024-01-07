// import  Vue from  'vue'

// const EventBus = new Vue()
// Object.defineProperties(Vue.prototype, {
//     $bus: {
//         get: function () {
//             return EventBus
//         }
//     }
// })

// import { createApp } from 'vue';

// const app = createApp({});
// const EventBus = app.config.globalProperties.$bus = app.config.globalProperties.$bus || createApp({});

// export default app;

import mitt from 'mitt';

const eventBus = mitt();

export default eventBus;
