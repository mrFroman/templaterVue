<template>
    <div>
        <form 
            @submit.prevent="registerForm"
            >
            <p>
                <input 
                    v-model="useremail"
                    id="useremail"
                    type="email"
                    placeholder="Введите email"    
                >
            </p>
            <p>
                <input 
                    v-model="password"
                    id="password"
                    type="password"
                    placeholder="Введите пароль"
                >
            </p>
            <p>
                <input 
                    v-model="repeatPassword"
                    id="repeatPassword"
                    type="password"
                    placeholder="Повторите пароль"
                >
            </p>

            <button
                type="submit"    
            >
                Зарегистрироваться
            </button>
        </form>
    </div>



</template>


<script setup>
import axios from "axios";
import { ref } from "vue";
import router from "@/router/router";

const useremail = ref('')
const password = ref('')
const repeatPassword = ref('')

const registerForm = (e) => {
    const formData ={
        email: useremail.value,
        password: password.value,
        headers: { 'Content-Type': 'application/json' },
    }

    axios.post('http://127.0.0.1:8000/api/v1/register/', formData)
        .then(response => {
                router.push('/login')
            })
        .catch(error => {
            console.log(error)
        })
}

// export default {    
//     data() {
//         return {
//             useremail: '',
//             password: '',
//             repeatPassword: ''
//         }
//     },

//     methods: {  
//         registerForm(e) {
//             const formData = {
//                 email: this.useremail,
//                 password: this.password,
//                 headers: { 'Content-Type': 'application/json' },
//             }

//             axios
//                 .post('http://127.0.0.1:8000/api/v1/register/', formData)
//                 .then(response => {
//                         this.$router.push('/login')
//                     })
//                 .catch(error => {console.log(error)})
//         },
//     },
// }



</script>


<style scoped>


</style>