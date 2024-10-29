<template>
    <button>
        <slot></slot>
    </button>
</template>

<script setup>
defineOptions({
  name: 'PinkButton'
})

</script>

<style lang="scss" scoped>
button {
  padding: 2px 5px;
  border: 1px #de39a2 solid;
  border-radius: 6px;
  background: #fff;
  color: #de39a2;
  cursor: pointer;

  &:hover {
    background-color: #de39a2;
    color: #fff;
  }
}
</style>
