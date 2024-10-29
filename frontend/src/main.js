import { createApp } from 'vue';
import { createPinia } from 'pinia'
import App from './App';
import components from '@/components/UI';
import router from "@/router/router";
// import store from "@/store";

const app = createApp(App)
const store = createPinia()

components.forEach(component => {
    app.component(component.name, component)
})

app
    .use(router)
    .use(store)
    .mount('#app')


