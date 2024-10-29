<template>
  <button>
    <slot></slot>
  </button>
</template>

<script setup>
defineOptions({
  name: 'ViolettButton'
})

</script>

<style lang="scss" scoped>
button {
    display: block;
    margin-top: 15px;
    padding: 10px 15px;
    background: transparent;
    border: 1px #8e4adf solid;
    border-radius: 6px;
    color: #8e4adf;
    cursor: pointer;

    &:hover {
        background: #8e4adf;
        color: #fff;
    }
}
</style>