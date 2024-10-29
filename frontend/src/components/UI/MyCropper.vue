<template>
    <div class="cropperWrapper">
      <h4>Для масштабирования изображения воспользуйтесь колесиком мыши</h4>
        <cropper
                class="cropper"
                :style="size"
                :src="currentImage"
                :stencil-props="{
                                handlers: {},
                                movable: false,
                                resizable: false,
                                aspectRatio: size.width/size.height,
                              }"
                :resize-image="{
                                adjustStencil: false
                              }"
                image-restriction="stencil"
                ref="cropper"
                :stencil-size="{
                width: size.width,
                height: size.height
                            }"
        ></cropper>
        <div class="buttons">
            <violett-button @click="crop">Обрезать</violett-button>
            <violett-button @click="$refs.file.click()">
                <input style="display: none" type="file" ref="file" @change="loadImage($event)" accept="image/*">
                Загрузить изображение
            </violett-button>
        </div>
    </div>
</template>

<script>
import {Cropper} from "vue-advanced-cropper"
import 'vue-advanced-cropper/dist/style.css'
import ViolettButton from "@/components/UI/ViolettButton.vue"
// import { ref } from "vue"


// const prop = defineProps({
//     image: String,
//     size: {
//         width: Number,
//         height: Number
//     }
// })


// const currentImage = ref(prop.image)
// const blob = ref(prop.image)
// const coordinates = ref({
//     width: 0,
//     height: 0,
//     left: 0,
//     top: 0,
// })

// const loadImage = (event) => {
//     const {files} = event.target

//     if (files && files[0]) {
//         if (currentImage.value) {
//             URL.revokeObjectURL(currentImage.value)
//         }

//         const bloba = URL.createObjectURL(files[0])
//         const reader = new FileReader()
//         reader.onload = () => {
//             currentImage.value = bloba
//             blob.value = bloba
//         }
//         reader.readAsArrayBuffer(files[0])
//     }
// }

// const crop = () => {
//     const {coordinates, canvas} = ref.cropper.getResult()   // this.$refs.cropper.getResult();
//     coordinates.value = coordinates;
//     currentImage.value = canvas.toDataURL();
//     $emit('upgradeimage', currentImage, blob)
// }

export default {
    components: {ViolettButton, Cropper},
    props: {
        image: {
            type: String
        },
        size: {
            width: Number,
            height: Number
        }
    },
    data() {
        return {
            currentImage: this.image,
            blob: this.image,
            coordinates: {
                width: 0,
                height: 0,
                left: 0,
                top: 0,
            },
        }
    },
    methods: {
        loadImage(event) {
            const {files} = event.target;
            if (files && files[0]) {
                if (this.currentImage) {
                    URL.revokeObjectURL(this.currentImage)
                }
                const blob = URL.createObjectURL(files[0]);
                const reader = new FileReader();
                reader.onload = () => {
                    this.currentImage = blob
                    this.blob = blob
                };
                reader.readAsArrayBuffer(files[0]);
            }
        },
        crop() {
            const {coordinates, canvas,} = this.$refs.cropper.getResult();
            this.coordinates = coordinates;
            this.currentImage = canvas.toDataURL();
            this.$emit('upgradeimage', this.currentImage, this.blob)
        }
    }
}
</script>

<style lang="scss" scoped>
.cropper {
    width: 700px;
    height: 550px;
}
    .buttons {
        display: flex;
        gap: 20px;
    }
</style>
