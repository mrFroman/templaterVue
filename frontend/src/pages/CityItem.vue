<template>
    <div class="city">
        <div class="input_newslatter">
            <form method="post" @submit.prevent="createTask">
                <p>Согласовать рассылку 
                    <input 
                        :value="agreement"
                        @input="agreement = $event.target.value"
                        type="text" 
                        placeholder="введите с кем согласовать рассылку"></p>
                
                <p>База отправки рассылки 
                    <input 
                        :value="client_base"
                        @input="client_base = $event.target.value"
                        type="text" 
                        placeholder="введите базу рассылки"></p>
                
                <p>Выбрать дату отправки письма 
                    <input 
                        :value="date_departure"
                        @input="date_departure = $event.target.value"
                        type="date" 
                        id="date" 
                        name="date_departure"/></p>
                
                <p>Платная рассылка 
                    <input class="checkbox"
                        v-model="checked"
                        type="checkbox" 
                        name="paid_mailing"></p>

                <button 
                    >
                    
                    Внести данные о мероприятиях
                </button>
            </form>
            
        </div>
    </div>
</template>


<script setup>
import { ref } from 'vue';
import { useTemplaterStore } from "@/stores/templaterStore";
import axios from 'axios';
import router from '@/router/router';


// @click="$router.push('/email-templater')"  не забудь вернуть в метод пост

const templaterStore = useTemplaterStore()
const agreement = ref('')
const client_base = ref('')
const date_departure = ref('')
const checked = ref(false)
const date = addZero(new Date().getFullYear()) + '-' + addZero(new Date().getMonth() + 1) + '-' + addZero(new Date().getDate())

function addZero(num) {
	if (num >= 0 && num <= 9) {
		return '0' + num;
	} else {
		return num;
	}
}

const createTask = () => {
    const newTask = {
        agreement: agreement.value,
        client_base: client_base.value,
        date_create_mail: date,
        date_update_mail: date,
        date_departure: date_departure.value,
        paid_mailing: checked.value,
        user_create: localStorage.getItem('email'),
        city_mail: templaterStore.city,
        type_mail: '1 топ'
    }

    axios.post('http://127.0.0.1:8000/api/v1/postdate/', newTask)
        .then(response => {
            templaterStore.$patch({
                id_created: response.data
            })
            router.push('/email-templater')
        })
        .catch(error => {
            alert('ошибка создания', error)
        })
    }


// export default{
//     data() {
//         return {
//             agreement: '',
//             client_base: '',
//             date_departure: '',
//             paid_mailing: '',
//         }

//     },

//     methods: {
//         createTask() {
//             const newTask = {
//                 agreement: this.agreement,
//                 client_base: this.client_base,
//                 date_create_mail: Date.now,
//                 date_update_mail: Date.now,
//                 date_departure: this.date_departure,
//                 paid_mailing: this.paid_mailing
//             }
//         },
//     }
// }

</script>


<style scoped>
.city {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: flex-start;
    align-items: flex-start;
    padding-top: 20px;
}

.input_newslatter {
    width: 600px;
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
}

.checkbox {
    margin-top: 0px;
    margin-bottom: 0px;
    width: 30%;
}

input {
    width: 100%;
    padding: 10px;
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>