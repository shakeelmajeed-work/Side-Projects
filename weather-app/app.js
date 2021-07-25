const request = require('request')

const weather_url = "http://api.weatherstack.com/current?access_key=9448362948781768af00226076dbd565&query=51.509865,-0.118092"



//first argument is the object and second is a function to run on the response of the request (body property of response holds the data I want to manipulate) 
request({url:weather_url, json:true},(error,response,body) => {
    data = response.body
    console.log(data.current.weather_descriptions[0],":It is currently",data.current.temperature, " degrees and a", data.current.precip,"% chance of rain")
})