<template>
  <navbar></navbar>
  <div class="main">
    <router-view></router-view>
  </div>
</template>

<script setup>
import { useTemplaterStore, useTokenStore, useEventListStore } from "@/stores/templaterStore";
import { onMounted } from "vue";

const templaterStore = useTemplaterStore();
const tokenStore = useTokenStore();
const eventListStore = useEventListStore();

import Navbar from "@/components/UI/Navbar.vue";
import axios from "axios";

  // this.tokenStore.commit("initializeStore");
  const access = localStorage.getItem('access')
    if ( access ) {
        axios.defaults.headers.common['Authorization']  = "Calculation " + access
    } else {
        axios.defaults.headers.common['Authorization'] = ''
    }

  const getAccess = (e) => {
    const accessData = {
      refresh: localStorage.getItem('refresh')
    }

    axios
      .post('http://127.0.0.1:8000/api/v1/auth/jwt/refresh', accessData)
      .then(response => {
        const access = response.data.access
        localStorage.setItem('access', access)
        tokenStore.$patch({access: access})
      })
  };

  onMounted(() => {
    setInterval(() => {
      getAccess()
    }, 580000)
  });

</script>

<style lang="scss">
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body {
  font-family: Helvetica, Geneva, sans-serif;
  font-size: 14px;
}

.main__panel {
  width: calc(100% - 650px);
  margin-right: 650px;
  padding: 20px;
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
  border-bottom: 1px #ccc solid;
}

h4 {
  margin-bottom: 15px;
}

.email {
  width: 650px;
  height: 100%;
  position: fixed;
  top: 0;
  right: 0;
  border-left: 1px #ccc solid;
  background-color: #f7f7f7;
  overflow-y: scroll;
  margin-top: 65px;
  z-index: 0;
}

.email__template {
  width: 600px;
  min-height: 100%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  background-color: #fff;
}

.header {
  height: 118px;
}

*[contenteditable] {
  border: 1px #868686 dashed;
  border-radius: 5px;
}
</style>
