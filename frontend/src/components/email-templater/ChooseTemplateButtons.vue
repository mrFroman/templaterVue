<template>
  <violett-button
          @click="$emit('template', button)"
  >
      {{ button.name }}
  </violett-button>
</template>

<script setup>

const emit = defineEmits(['template'])
const prop = defineProps({ button: Object})

</script>

<style>

</style>
