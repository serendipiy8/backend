<template>
    <div class="home-swiper">
        <swiper :options="swiperOptions">
            <swiper-slide v-for="(slide, index) in slides" :key="index">
                <img :src="slide.image" alt="Slide Image" class="swiperimg"/>
            </swiper-slide>
            <div class="swiper-pagination" slot="pagination"></div>
            <div class="swiper-button-next" slot="button-next"></div>
            <div class="swiper-button-prev" slot="button-prev"></div>
        </swiper>
    </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/swiper-bundle.css';

export default {
    name: 'HomeSwiper',
    components: {
        Swiper,
        SwiperSlide,
    },
    data() {
        return {
            swiperOptions: {
                loop: true,
                autoplay: {
                    delay: 300,
                    disableOnInteraction: false,
                },
                pagination: {
                    el: '.swiper-pagination',
                },
                navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            },
            slides: [
                {
                    image: require('@/assets/slide1.png'),
                },
                {
                    image: require('@/assets/slide2.jpg'),
                },
                {
                    image: require('@/assets/slide3.jpg'),
                },
            ],
        };
    },
};
</script>

<style scoped>
.home-swiper {
    width: 100%;
    height: 100%;
}

.swiper-pagination {
    /* position: absolute; */
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
}
</style>
