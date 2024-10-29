<template>
    <my-modal v-model:show="isVisible">
        <my-cropper
            :image="currentImage"
            @upgradeimage="upgradeImage"
            :size="cropperSize"
        ></my-cropper>
    </my-modal>
    <div class="top"
         @dragover.prevent
         @drop="dragDrop($event)"
    >

        <img
                :src="event.image"
                alt=""
                @click="openModal"
        >
        <div v-if="isText">
            <p contenteditable="true">
                {{ event.description }}
            </p>
            <p
                    class="pushkin"
                    v-if="event.is_pushkin_card"
            >
                Действует Пушкинская карта
            </p>
            <p>
                {{ event.date }} {{ event.time }} {{ event.venue }}
            </p>
            <a :href="event.link" target="_blank">Выбрать место</a>
        </div>
    </div>
</template>

<script>
import plugImage from '@/assets/img/plug600.png'
import ViolettButton from "@/components/UI/ViolettButton.vue";
import MyModal from "@/components/UI/MyModal.vue";
import MyCropper from "@/components/UI/MyCropper.vue";

export default {
    components: {MyCropper, MyModal, ViolettButton},
    props: {
        template: {
            type: Object
        },
        isText: {
            type: Boolean
        }
    },
    data() {
        return {
            event: {
                description: 'Описание мероприятия',
                date: 'Дата',
                time: 'Время',
                venue: 'Место',
                is_pushkin_card: false,
                image: plugImage
            },
            isVisible: false,
            coordinates: {
                width: 0,
                height: 0,
                left: 0,
                top: 0,
            },
            currentImage: plugImage,
            cropperSize: {
                width: 600,
                height: 300
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
        upgradeImage(image, oldImage) {
            this.event.image = image
            this.currentImage = oldImage
            this.isVisible = false
        }
    }
}

</script>

<style lang="scss" scoped>
.buttons {
  display: flex;
  gap: 20px;
}

.cropper {
  width: 700px;
  height: 400px;
}

.top {
  position: relative;
  text-align: center;
  border-radius: 5px;
  font-family: Tahoma, Geneva, sans-serif;
  font-size: 14px;
  font-weight: bold;
  margin: 0 0 30px;
}

p {
  margin: 20px 0;
}

img {
  width: 570px;
  height: 285px;
  border-radius: 5px;
}

a {
  text-decoration: none;
  font-weight: normal;
  margin: auto;
  display: inline-block;
  background: #8e4adf;
  color: #fff;
  border-radius: 50px;
  padding: 13px 35px 14px;
  font-size: 18px;
  line-height: 15px;
  border: none;
}

.pushkin {
  color: #de39a2;
}
</style>
