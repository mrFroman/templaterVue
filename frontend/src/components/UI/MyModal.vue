<template>
  <div class="dialog" v-if="show" @mousedown="hideModal($event)">
    <div class="dialog__content" @mousedown.stop>
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
defineOptions({
  name: 'MyModal',
})

const emit = defineEmits(['update:show'])

const prop = defineProps({
  show:{
    type: Boolean,
    default: false
  }
})

const hideModal = () => {
  emit('update:show', false)
}

// export default {
//   name: 'MyModal',
//   props: {
//     show: {
//       type: Boolean,
//       default: false
//     }
//   },
//   methods: {
//     hideModal() {
//       this.$emit('update:show', false)
//     }
//   }
// }
</script>

<style lang="scss" scoped>
.dialog {
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, .5);
  position: fixed;
  display: flex;
  z-index: 100;
  overflow-y: scroll;

  &__content {
    margin: auto;
    background-color: #fff;
    border-radius: 6px;
    padding: 20px;
    min-width: 300px;
    min-height: 50px;
  }
}
</style>
