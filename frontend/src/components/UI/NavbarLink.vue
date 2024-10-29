<template>
  <button>
    <slot></slot>
  </button>
</template>

<script setup>

</script>

<style lang="scss" scoped>
button {
  color: #fff;
  background: transparent;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background: #fff;
    color: #8e4adf;
  }
}
</style>
