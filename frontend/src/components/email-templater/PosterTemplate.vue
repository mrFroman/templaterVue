<template>
    <my-modal v-model:show="isVisible">
        <my-cropper
            :image="currentImage"
            @upgradeimage="upgradeImage"
            :size="cropperSize"
        ></my-cropper>
    </my-modal>
    <div
            class="poster"
            @dragover.prevent
            @drop="dragDrop($event)"
    >
        <img
                :src="event.image"
                alt="image"
                @click="openModal"
        >
        <div class="poster__body">
            <p class="poster__category">{{ event.category }}</p>
            <p class="poster__title" contenteditable="true">{{ event.title }}</p>
            <p class="poster__pushkin"><span v-if="event.is_pushkin_card">Пушкинская карта</span></p>
            <p style="font-size: 13px">
                <span class="poster__date">{{ event.date }}</span> <span class="poster__time">{{ updateTime }}</span> <span class="poster__rate">{{ event.rate }}</span>
            </p>
            <p class="poster__venue" contenteditable="true">{{ event.venue }}</p>
            <a class="poster__price" :href="event.link" target="_blank" >{{ splitPrice }}</a>
        </div>
    </div>
</template>

<script>
import plugImage from '@/assets/img/plug300.png'
import MyModal from "@/components/UI/MyModal.vue";
import ViolettButton from "@/components/UI/ViolettButton.vue";
import MyCropper from "@/components/UI/MyCropper.vue";

export default {
    components: {MyCropper, ViolettButton, MyModal},
    data() {
        return {
            event: {
                category: 'Категория',
                title: 'Название',
                is_pushkin_card: false,
                date: 'Дата',
                time: 'Время',
                rate: '0+',
                venue: 'Место',
                price: '0',
                image: plugImage
            },
            isVisible: false,
            currentImage: plugImage,
            cropperSize: {
                width: 300,
                height: 425
            }
        }
    },
    methods: {
        dragDrop(event) {
            const data = JSON.parse(event.dataTransfer.getData('event'))
            this.event = Object.assign(this.event, data)
            this.currentImage = data.image
        },
        openModal() {
            this.isVisible = true
        },
        crop() {
            const {coordinates, canvas,} = this.$refs.cropper.getResult();
            this.coordinates = coordinates;
            this.event.image = canvas.toDataURL();
            this.isVisible = false
        },
        upgradeImage(image, oldImage) {
            this.event.image = image
            this.currentImage = oldImage
            this.isVisible = false
        }
    },
    computed: {
        splitPrice: function () {
            return this.event.price.split('—').length > 1 ? `от ${this.event.price.split('—')[0]} Р` : `${this.event.price.split('—')[0]} Р`
        },
        updateTime: function () {
            return `в ${this.event.time}`
        }
    }
}
</script>

<style lang="scss" scoped>
.poster {
  width: 177px;
  border-radius: 6px;
  overflow: hidden;
  border: 1px #ccc solid;
  box-shadow: 0 1px 6px #ccc;
  margin-bottom: 30px;
  font-size: 14px;
  font-weight: bold;

  img {
    width: 100%;
    height: 234px;
    display: block;
    background: transparent;
  }

  &__body {
    height: 228px;
    width: 100%;
    padding: 0 10px;
    border-top: 1px #bebebe solid;
  }

  &__category {
    font-size: 12px;
    color: #de39a2;
    font-weight: normal;
    padding-top: 6px;
  }

  &__pushkin {
    height: 15px;
    margin: 5px 0;
    font-size: 12px;
    color: #de39a2;
    font-weight: normal;
  }

  &__title {
    height: 50px;
    margin-top: 10px;
    overflow: hidden;
  }

  &__time {
    color: #868686;
  }

  &__rate {
    background-color: #bebebe;
    color: #fff;
    font-size: 10px;
    padding: 1px 2px;
    border-radius: 2px;
    vertical-align: top;
  }

  &__venue {
    font-size: 13px;
    font-weight: normal;
    color: #868686;
    height: 50px;
    margin: 5px 0;
  }

  &__price {
    text-decoration: none;
    font-weight: normal;
    background-color: #8e4adf;
    display: block;
    width: 148px;
    border: none;
    border-radius: 50px;
    color: #ffffff;
    font-family: sans-serif;
    font-size: 16px;
    text-align: center;
    padding: 7px 10px;
  }
}
</style>
