<template>
  <button>
    <slot></slot>
  </button>
</template>

<script setup>
defineOptions({
  name: 'CalculatorButton'
})

</script>

<style lang="scss" scoped>
button {
  background: #8e4adf;
  color: #fff;
  font-size: 16px;
  border-radius: 50px;
  border: 2px #fff solid;
  padding: 10px 30px;
  box-shadow: 0px 5px 10px #bebebe;
  cursor: pointer;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: bold;
}
</style>
