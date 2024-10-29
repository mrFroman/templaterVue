// const express = require('express')
// const port = 3000
// const app = express()
// const bodyParser = require('body-parser')
// const routes = require('./routes/routes')

// app.use(bodyParser.json())
// app.use(bodyParser.urlencoded({
//     extended: true
// }))
// app.use((req, res, next) => {
//     // этот заголовок ответа указывает, что тело ответа будет в JSON формате
//     res.setHeader('Content-Type', 'application/json');
//     // CORS заголовки ответа для поддержки кросс-доменных запросов из браузера
//     res.setHeader('Access-Control-Allow-Origin', '*');
//     res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS');
//     res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
//     next();
// });

// routes(app)

// const server = app.listen(port, (error) => {
//     if(error) return console.log(`Ошибка: ${error}`)

//     console.log(`Сервер запущен на порту ${server.address().port}`)
// })
