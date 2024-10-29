<template>
    <div class="choose">
        <my-modal
            v-model:show="isVisible"
        >
            <h4>Выберите формат рассылки: </h4>
            <choose-template-buttons
            v-for="button of buttons"
            :button="button"
            v-bind:key="button.data"
            @template="chooseTemplate(button)"
            />
        </my-modal>
        <h4>Формат рассылки:</h4>
        <violett-button
            style="margin-top: 0"
            @click="modalOpen"
        >
            {{ template }}
        </violett-button>
    </div>
</template>

<script>
import ChooseTemplateButtons from '@/components/email-templater/ChooseTemplateButtons.vue'
export default {
    emits: ['choose'],
    components: {
        ChooseTemplateButtons
    },
    data() {
        return {
            isVisible: false,
            buttons: [
                {
                    name: '1 топ',
                    data: {
                        tops: 1,
                        headPoster: 0,
                        footerPoster: 0
                    }
                },
                {
                    name: '2 топа',
                    data: {
                        tops: 2,
                        headPoster: 0,
                        footerPoster: 0
                    }
                },
                {
                    name: '3 топа',
                    data: {
                        tops: 3,
                        headPoster: 0,
                        footerPoster: 0
                    }
                },
                {
                    name: '1 топ 3 афиши',
                    data: {
                        tops: 1,
                        headPoster: 3,
                        footerPoster: 0
                    }
                },
                {
                    name: '1 топ 6 афиш',
                    data: {
                        tops: 1,
                        headPoster: 6,
                        footerPoster: 0
                    }
                },
                {
                    name: '2 топа 3 афиши',
                    data: {
                        tops: 2,
                        headPoster: 3,
                        footerPoster: 0
                    }
                },
                {
                    name: '2 топа 6 афиш',
                    data: {
                        tops: 2,
                        headPoster: 6,
                        footerPoster: 0
                    }
                },
                {
                    name: '2 топа 9 афиш',
                    data: {
                        tops: 2,
                        headPoster: 6,
                        footerPoster: 3
                    }
                },
                {
                    name: '2 топа 12 афиш',
                    data: {
                        tops: 2,
                        headPoster: 6,
                        footerPoster: 6
                    }
                },
                {
                    name: '3 топа 9 афиш',
                    data: {
                        tops: 3,
                        headPoster: 6,
                        footerPoster: 3
                    }
                },
                {
                    name: '3 топа 12 афиш',
                    data: {
                        tops: 3,
                        headPoster: 6,
                        footerPoster: 6
                    }
                },
                {
                    name: 'Техническая рассылка',
                    data: {
                        tops: 0,
                        headPoster: 0,
                        footerPoster: 0
                    }
                }
            ],
            template: 'Выбрать формат'
        }
    },
    methods: {
        modalOpen() {
            this.isVisible = true
        },
        chooseTemplate(button) {
            this.$emit('choose', button)
            this.template = button.name
            this.isVisible = false
        }
    }
}
</script>

<style lang="scss" scoped>
button {
    width: 100%;
}

h4 {
    margin: 0;
    white-space: nowrap;
}

.choose {
    display: flex;
    align-items: center;
    gap: 20px;
}
</style>
