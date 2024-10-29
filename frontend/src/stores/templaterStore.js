import { defineStore } from 'pinia'
import axios from "axios";
import { ref } from 'vue';


axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";



export const useTemplaterStore = defineStore('templaterStore', () => {
    const id_created = ref('')
    const city = ref('') 


    return { id_created, city }
})


export const useTokenStore = defineStore('tokenStore', () => {
    const access = ref(localStorage.getItem('access'))
    const refresh = ref(localStorage.getItem('refresh')) 
    const email = ref(localStorage.getItem('email'))



    function $reset() {
        access.value = ''
        refresh.value = ''
        email.value = ''
    }

    return { access, refresh, email, $reset }
})





export const useEventListStore = defineStore('eventListStore', () => {
    const events = ref([])    

    return { events }
})

