<template>
    <div
            class="events"
            v-show="events.length > 0"
    >
        <h4 class="events__title">Список мероприятий</h4>
        <div class="events__list">
            <events-item
                    v-for="event of events"
                    :event="event"
                    :key="event.id"
                    @remove="$emit('remove', event)"
                    @replace="$emit('replace')"
            />
        </div>
    </div>
    <div
            class="events"
            v-show="events.length === 0"
    >
        <h4>Список мероприятий пуст</h4>
    </div>

</template>

<script setup>
import EventsItem from '@/components/email-templater/EventsItem.vue';

const emits = defineEmits(['remove', 'replace'])
const props = defineProps({
  events: {
    type: Array,
    required: true
  }
})

</script>

<style lang="scss" scoped>
.events {
  width: calc(100% - 650px);
  margin-right: 650px;
  padding: 20px;

  &__title {
    margin-bottom: 15px;
  }

  &__list {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    height: 600px;
    overflow-y: scroll;
    flex-direction: row;
    align-content: flex-start;
    // align-content: start;

    &::-webkit-scrollbar {
      width: 3px;
    }

    &::-webkit-scrollbar-thumb {
      background: #B0B0B0;
      border-radius: 50px;

    }

    &::-webkit-scrollbar-track {
      background: #F5F5F5;
    }
  }
}
</style>
