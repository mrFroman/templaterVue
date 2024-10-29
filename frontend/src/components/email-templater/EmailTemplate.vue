<template>
    <div class="root">
        <div
            v-if="template === 'Формат не выбран'"
        >
            Формат не выбран
        </div>
        <top-template
            v-if="template.tops > 0"
            :template="template"
            :is-text="true"
        ></top-template>
        <div class="head__poster">
            <poster-template
                v-for="poster in template.headPoster"
            ></poster-template>
        </div>
        <top-template
            v-if="template.tops > 1"
            :template="template"
            :is-text="isText"
        ></top-template>
        <div class="footer__poster">
            <poster-template
                v-for="poster in template.footerPoster"
            ></poster-template>
        </div>
        <top-template
            v-if="template.tops > 2"
            :template="template"
            :is-text="isText"
        >
        </top-template>
        <technic-template
            v-if="template.tops === 0"
        ></technic-template>
    </div>
</template>

<script setup>
import TopTemplate from "@/components/email-templater/TopTemplate.vue";
import PosterTemplate from "@/components/email-templater/PosterTemplate.vue";
import TechnicTemplate from "@/components/email-templater/TechnicTemplate.vue";
import { computed } from 'vue';

const props = defineProps({
    template: {
        tops: {
            type: Number,
        },
        headPoster: {
            type: Number,
        },
        footerPoster: {
            type: Number,
        }
    }
})

const isText = computed(() => {
    return props.template.tops > 1 && props.template.footerPoster === 0 && props.template.headPoster === 0
})

// export default {
//     components: {TechnicTemplate, PosterTemplate, TopTemplate},
//     props: {
//         template: {
//             tops: {
//                 type: Number,
//             },
//             headPoster: {
//                 type: Number,
//             },
//             footerPoster: {
//                 type: Number,
//             }
//         }
//     },
//     computed: {
//         isText() {
//             return this.template.tops > 1 && this.template.footerPoster === 0 && this.template.headPoster === 0
//         }
//     }
// }
</script>

<style lang="scss" scoped>
.head__poster,
.footer__poster {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.root {
  width: 100%;
  min-height: 100%;
  background-color: #fff;
  padding: 15px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 40px;
}
</style>
