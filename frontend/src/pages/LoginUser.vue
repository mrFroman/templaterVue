<template>
    <div class="userauth">
        <p v-if="incorrectAuth">Incorrect username or password entered - please try again</p>
        <form 
            @submit.prevent="submitForm"
            >
            <p>
                <input class="input_word"
                    v-model="useremail"
                    id="useremail"
                    type="email"
                    placeholder="Введите email"    
                >
            </p>
            <p>
                <input class="input_word"
                    v-model="password"
                    id="password"
                    type="password"
                    placeholder="Введите пароль"
                >
            </p>
            <button
                type="submit"    
            >
                Войти
            </button>
        </form>
    </div>
</template>


<script setup>
import axios from "axios"; 
import { ref } from "vue";
import { useTokenStore } from "@/stores/templaterStore";
import router from "@/router/router";

const password = ref('')
const useremail = ref('')
const incorrectAuth = ref(false)
const tokenStore = useTokenStore()


const submitForm = (e) => {
    axios.defaults.headers.common['Authorization'] = ''
    localStorage.removeItem('access')

    const formData = {
        email: useremail.value,
        password: password.value,
        headers: { 'Content-Type': 'application/json' },
    }

    axios
        //.post('http://127.0.0.1:8000/api/v1/auth/jwt/create', formData)
        .post('http://127.0.0.1:8000/api/v1/login/', formData)
        .then(response => {
            const access = response.data.tokens.access
            const refresh = response.data.tokens.refresh
            const useremail = response.data.email

            tokenStore.$patch({
                'access': access,
                'refresh': refresh,
                'email': useremail
            })

            axios.defaults.headers.common['Authorization']  = "Calculation " + access
            localStorage.setItem('access', access)
            localStorage.setItem('refresh', refresh)
            localStorage.setItem('email', useremail)

            router.push('/')
        })
        .catch(error => {
            console.log(error)
            incorrectAuth.value = true
        })
}

// export default {    
//     data() {
//         return {
//             useremail: '',
//             password: '',
//             incorrectAuth: false
//         }
//     },

//     methods: {
//       submitForm(e) {
//             axios.defaults.headers.common['Authorization'] = ''
//             localStorage.removeItem('access')

//             const formData = {
//                 email: this.useremail,
//                 password: this.password,
//                 headers: { 'Content-Type': 'application/json' },
//             }

//             axios.
//               post('http://127.0.0.1:8000/api/v1/auth/jwt/create', formData)
//               .then(response => {
//                         const access = response.data.access
//                         const refresh = response.data.refresh

//                         this.$store.commit('setAccess', access)
//                         this.$store.commit('setRefresh', refresh)

//                         axios.defaults.headers.common['Authorization']  = "Calculation "  + access

//                         localStorage.setItem('access', access)
//                         localStorage.setItem('refresh', refresh)

//                         this.$router.push('/')

//                     })
//                 .catch(error => {
//                   console.log(error)
//                   this.incorrectAuth = true
//                 })
//         },  
        
//     },
// }

</script>


<style scoped>

.userauth {
    display: flex;
    margin: 0 auto;
    justify-content: space-around;
    width: 50%;
    flex-direction: column;
}

.input_word {
    width: 100%;
    padding: 10px;
    /* margin: 10px; */
    margin-top: 80px;
}
</style>
