<template>
    <div>
        <my-modal
                v-model:show="isVisible"
        >
            <form class="form">
                <h4>Вставьте ссылки на мероприятия, через запятую</h4>
                <my-textarea
                        v-model:value="eventsLinks"
                        :placeholder="placeholder"
                        @focus="error = ''"
                ></my-textarea>
                <p
                        v-if="error"
                >
                    {{ error }}
                </p>
                <violett-button
                        @click.prevent="loadEvents"
                >
                    Добавить мероприятия
                </violett-button>
            </form>
        </my-modal>
        <violett-button
                style="margin-top: 0"
                @click="modalOpen"
        >
            Добавить мероприятия
        </violett-button>
    </div>
</template>

<script>
import MyTextarea from '../UI/MyTextarea.vue'

export default {
    emits: ['loadEvents'],
    components: {MyTextarea},
    data() {
        return {
            eventsLinks: '',
            isVisible: false,
            placeholder: 'Например \n' +
                'https://ekb.kassy.ru/events/teatr/2-54300/\n' +
                'https://ekb.kassy.ru/events/koncerty-i-shou/3-13203509/\n' +
                'https://ekb.kassy.ru/events/koncerty-i-shou/2-53902/',
            error: ''
        }
    },
    methods: {
        modalOpen() {
            this.isVisible = true
        },
        loadEvents() {
            !this.eventsLinks ? this.error = 'Добавьте минимум 1 ссылку на мероприятие' : null

            const regex = /^((http[s]:\/\/))?((\w*)|(\w*-\w*)).?(kassy).(ru)\/(events)\/((\w*-\w*-\w*)|(\w*)|(\w*-\w*))\/(\d*.\d*)/
            const events = this.eventsLinks
                .replace(/\s/g, '')
                .replace(',', '')
                .replace(new RegExp('https:', 'g'), '*https:')
                .split('*')
                .filter(el => el !== '')
                .map(link => !regex.test(link) ? this.error += `Не корректная ссылка ${link}` : link)

            if (!this.error) {
                this.$emit('loadEvents', events)
                this.eventsLinks = ''
                this.isVisible = false
            }
        }
    }
}
</script>

<style scoped>
p {
    color: red;
    margin-top: 10px;
    word-break: break-word;
}
</style>
