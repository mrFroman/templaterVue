import {createRouter, createWebHistory} from "vue-router";
import TemplaterPage from "@/pages/TemplaterPage.vue";
import ChoiseCity from "@/pages/ChoiseCity.vue";
import CityItem from "@/pages/CityItem.vue";
import RegisterUser from "@/pages/RegisterUser.vue";
import LoginUser from "@/pages/LoginUser.vue";
import UserCabinet from '@/pages/UserCabinet.vue'


const routes = [
    {
        path: '/',
        component: TemplaterPage
    },
    {
        path: '/choise-city',
        component: ChoiseCity
    },
    {
        path: '/create-newsletter',
        component: CityItem
    },
    {
        path: '/register',
        component: RegisterUser
    },
    {
        path: '/login',
        component: LoginUser
    },
    {
        path: '/user-cabinet',
        component: UserCabinet
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router
