<template>
  <div class="navbar">
    <img @click="$router.push('/')" src="@/assets/img/rassylka.png" alt="logo">
    <hr>
    <!-- <navbar-link @click="$router.push('/')">Калькулятор</navbar-link> -->
    <!-- <navbar-link @click="$router.push('/email-templater')">Шаблонизатор</navbar-link> -->
    <navbar-link @click="$router.push('/choise-city')">Города рассылок</navbar-link>
    <div
      style="margin-left: auto;"
      v-if="user_data">
      <navbar-link style="margin-inline-start: auto;" :src="user_data">{{ user_data }}</navbar-link>
      <navbar-link style="margin-inline-start: auto;" @click="logOut">Выйти</navbar-link>
    </div>
    <div style="margin-left: auto;" v-else>
      <navbar-link style="margin-inline-start: auto;" @click="$router.push('/login')">Войти</navbar-link>
    </div>
    <navbar-link style="margin-inline-start: auto; margin-left: inherit;" @click="$router.push('/register')">Регистрация</navbar-link>
  </div>
</template>

<script setup>
import { useTokenStore } from "@/stores/templaterStore";
import NavbarLink from "@/components/UI/NavbarLink.vue";
import { ref, watch, watchEffect} from "vue";


const tokenStore = useTokenStore();
const user_data = ref(tokenStore.email)

// watchEffect(() => {
//   console.log(user_data.value)
// })

// const getMe = () => {
  
//   // axios
//     // .get('http://127.0.0.1:8000/api/v1/auth/users/me/', localStorage.getItem('access'))
//     // .get('http://127.0.0.1:8000/api/v1/user/', localStorage.getItem('access'))
//     // .then(response => {
//     //     user_data = response.data.email
//     // })
// }

const logOut = () => {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh') 
  localStorage.removeItem('email')
  tokenStore.$reset()
}

// onMounted(() => {
//   getMe()
// })

// export default {
//   components: {NavbarLink},

//   data() {
//     return {
//       user_data: ''
//     }
//   },

//   mounted () {
//     this.getMe()
//   },

//   methods: {
//     getMe(e) {
//       axios 
//         .get('http://127.0.0.1:8000/api/v1/auth/users/me/')
//         .then(response => {
//           this.user_data = response.data.email
//         })
//     },

//     logOut(){
//       localStorage.removeItem('access')
//       localStorage.removeItem('refresh')
//     }
//   },



// }

</script>


<style lang="scss" scoped>
.navbar {
  height: 60px;
  background-color: #8e4adf;
  box-shadow: 2px 2px 4px #222;
  display: flex;
  align-items: center;
  padding: 0 20px;
  gap: 20px;
  z-index: 100;
  position: sticky;
  top: 0;

  img {
    height: 40px;
    margin-right: 50px;
    cursor: pointer;
  }

  hr {
    height: 30px;
    border-left: 2px #fff solid;
    border-radius: 5px;
  }
}
</style>
