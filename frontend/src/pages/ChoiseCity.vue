<template>
    <div>
        <h2>Выбрать город для рассылки</h2>            
            <select 
                @click="fetchCity" 
                v-model="select"
                >
                <option disabled value="Выберите город">Выберите город</option>
                <option 
                    v-for="city in cities"
                    :city="city.city"
                    :key="city.id"
                    :value="city.city"
                    @update:selected="update"
                >
                    {{ city.city }}
                </option>
            </select>

            {{ select }}

            <button
                v-if="select"
                @click="$router.push('/create-newsletter')" 
            >
                создать заявку на рассылку
            </button>


            <div v-if="select" 
                v-for="mail in filteredCity"
                :city="mail.city">

                <table>

                <tr>
                    <td>
                        <p>дата создания</p>
                    </td>
                    <td>
                        <p>дата обновления</p>
                    </td>
                    <td>
                        <p>создатель рассылки</p>
                    </td>
                    <td>
                        <p>тип рассылки</p>
                    </td>
                    <td>
                        <p>платная</p>
                    </td>
                    <td>
                        <p>С кем согласовать</p>
                    </td>
                    <td>
                        <p>дата отправки письма</p>
                    </td>
                    <td>
                        <p>клиентская база</p>
                    </td>
                </tr>
                    <tr v-for="data in mail.list_city"
                    :city="mail.city">
                        <td>
                            {{ data.date_create_mail }}
                        </td>
                        <td>
                            {{ data.date_update_mail }}
                        </td>
                        <td>
                            {{ data.user_create }}
                        </td>
                        <td>
                            {{ data.type_mail }}
                        </td>
                        <td>
                            {{ data.paid_mailing }}
                        </td>
                        <td>
                            {{ data.agreement }}
                        </td>
                        <td>
                            {{ data.date_departure }}
                        </td>
                        <td>
                            {{ data.client_base }}
                        </td>
                        <button class="city_button"
                        >
                        просмотреть содержимое рассылки
                    </button>                        
                    </tr>
                </table>
                
        </div>

    </div>
</template>

<script setup>
import axios from 'axios';
import CityItem from '@/pages/CityItem.vue';
import { useTemplaterStore } from "@/stores/templaterStore";
import { onMounted, ref, computed } from 'vue';

const templaterStore = useTemplaterStore()
const cities = ref([])
const select = ref('')

const fetchCity = async () =>  {
    try {
        await axios.get('http://127.0.0.1:8000/api/v1/cities/')
            .then(response => {
                cities.value = response.data
            })
    }
    catch(e) {
        alert('Города не заружены')
    }
}

const filteredCity = computed(() => {
    templaterStore.$patch({city: select.value})
    return cities.value.filter(({ city }) => select.value ? city === select.value : true)
})

onMounted(() => {
    fetchCity()
})

</script>


<style scoped>
.city_button{
    margin: 10px;
    background: #8e4adf;
    color: #fff;
    font-size: 12px;
    border-radius: 50px;
    border: 2px #fff solid;
    padding: 5px 10px;
    box-shadow: 0px 5px 10px #bebebe;
    cursor: pointer;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
}

td {
  padding: 10px;
  background-color: #8e4adf;
  border: 2px #fff solid;
  color: #fff;

}

</style>