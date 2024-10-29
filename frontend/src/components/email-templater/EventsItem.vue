<template>
    <div class="events__card"
         :draggable="isDraggable"
         @dragstart="dragStart($event, event)"
    >
        <h4>{{ event.title }}</h4>
        <div class="card__body">
            <div><strong>Дата: </strong>{{ event.date }}</div>
            <div><strong>Цена: </strong>{{ isDone.price }}</div>
            <div><strong>Ценз: </strong><span>{{ isDone.rate }}</span></div>
            <div class="error" v-if="errors">
                {{ errors }}
            </div>
            <div class="card__buttons">
                <pink-button
                        @click="updateEvent($event, true)"
                >
                    Заменить
                </pink-button>
                <pink-button
                        @click="updateEvent(event, false)"
                >
                    Удалить
                </pink-button>
            </div>

        </div>

    </div>
</template>

<script>
import PinkButton from '@/components/UI/PinkButton.vue'


export default {
    emits: ['remove'],
    components: {
        PinkButton
    },
    props: {
        event: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            errors: '',
            isDraggable: true
        }
    },
    methods: {
        dragStart(event, currentEvent) {
            event.dataTransfer.dropEffect = 'copy'
            event.dataTransfer.effectAllowed = 'copy'
            event.dataTransfer.setData('event', JSON.stringify(currentEvent));
        },
        updateEvent() {
            this.$emit('remove')
        }
    },
    computed: {
        isDone() {
            const rateArray = ['0+', '6+', '12+', '16+', '18+']
            if (!rateArray.includes(this.event.rate)) {
                this.errors += 'Неверный ценз '
                this.isDraggable = false
            }

            if (this.event.price === 'Нет цены') {
                this.errors += 'Нет цены '
                this.isDraggable = false
            }

            return this.event
        }
    }
}
</script>
<style lang="scss" scoped>
.events__card[draggable=true] {
  width: 190px;
  height: 190px;
  border: 1px #ccc solid;
  border-radius: 6px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 5px;
  background-color: #fff;
  user-select: none;

  &:hover {
    cursor: move;
    background-color: #f7f7f7;
    color: #8e4adf;
  }
}

.events__card[draggable=false] {
  cursor: no-drop;
  width: 190px;
  height: 190px;
  border: 1px red solid;
  border-radius: 6px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 5px;
  background-color: rgba(255, 0, 0, .1);
  user-select: none;
}

h4 {
  margin-bottom: 5px;
  height: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card__body {
  div:not(:first-child) {
    margin-top: 10px;

    span {
      padding: 2px 5px;
      font-weight: bold;
      font-size: 12px;
      border-radius: 6px;
      color: #fff;
      background-color: #bebebe;
    }
  }
}

.card__buttons {
  display: flex;
  justify-content: space-between;
}

.error {
  color: red;
  text-align: center;
}
</style>
