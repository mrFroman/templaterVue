// const pool = require('../data/config')
// const axios = require('axios');
// const cheerio = require('cheerio');
// const {response} = require("express");

// const parseEvent = async (link) => {
//     const event = {}
//     const response = await axios.get(link)
//     const $ = cheerio.load(response.data)

//     let fullVenue = $('p.venue').text().split(',').map(el => el.trim())
//     let price = $('div.price > p').text().includes('') ? $('div.price > p').text().split(':')[1].replace('', '').trim() : 'Нет цены'

//     event.id = link.split('/')[link.split('/').length - 2]
//     event.link = link
//     event.image = `${new URL(link).origin}${$('div.img > a').attr('href')}`
//     event.title = $('h1').text().trim()
//     event.description = $('div.price').next().text()
//     event.date = `${fullVenue[fullVenue.length -1].split(' ')[0]} ${fullVenue[fullVenue.length -1].split(' ')[1]}`
//     event.time = $('p.venue > b').text()
//     event.rate = $('div.RARS').text()
//     event.venue = fullVenue[0]
//     event.price = price
//     event.is_pushkin_card = $('h1').next('small').text() === 'Пушкинская карта'

//     return event
// }

// const parseCities = async () => {
//     const response = await axios.get('https://kassy.ru/')
//     const $ = cheerio.load(response.data)
//     const cities = $('div[id="cities"]').find('a')
//     const citiesArray = []

//     for(let city of cities) {
//         citiesArray.push(city.attribs.title)
//     }

//     return JSON.stringify(citiesArray)
// }
// const router = app => {

//     app.get('/', (request, response) => {
//         response.send({message: 'Hello, server!'})
//     })

//     app.get('/events', async (request, response) => {
//         const event = await parseEvent(request.url.split('?')[1].split('=')[1])
//         response.send(event)
//     })

//     app.get('/events/demo', (request, response) => {
//         pool.query('SELECT * FROM events', (error, result) => {
//             if (error) throw error;
//             response.send(result);
//         });
//     });

//     app.get('/cities', async (request, response) => {
//         const citiesArray = await parseCities()
//         response.send(citiesArray)
//     })
// }
// module.exports = router
