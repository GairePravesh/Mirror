// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.
function Clock(){
  // Date Time
  let dtUtil = new Date()
  let datetime = "<h1>"+dtUtil.toLocaleTimeString()+"</h1><h2>"+dtUtil.toDateString()+"</h2>"
  let dt = document.getElementsByClassName("dt")
  dt[0].innerHTML = datetime
}
function Weather(){
  let city = "kathmandu"
  let weatherApiKey = "09e40b1c0da9d4171b249c629d8755dc"
  let apiUrl = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+weatherApiKey+"&units=metric";

  $.ajax({
     type: 'GET',
     url: apiUrl,
     success: function( data ) {
       let retData = "<p><img src='res/img/"+data.weather[0].icon+".png'></p><h2>"+data.name+"</h2><h2>"+data.main.temp+" * C</h2><h2>Humidity "+data.main.humidity+" %</h2>"
       let wt = document.getElementsByClassName("weath")
       wt[0].innerHTML = retData
     },
     error: function(xhr, status, error) {
        // check status && error
        alert(error)
     },
     dataType: 'json'
  });
}
function Quote(){
  let apiUrl = "http://quotes.rest/qod.json";

  $.ajax({
     type: 'GET',
     url: apiUrl,
     success: function( data ) {
       let retData = '"'+data.contents.quotes[0].quote+'" - '+data.contents.quotes[0].author
       let wt = document.getElementsByClassName("quot")
       wt[0].innerHTML = retData
     },
     error: function(xhr, status, error) {
        // check status && error
        alert(error)
     },
     dataType: 'json'
  });
}

Clock()
Weather()
Quote()
window.setInterval(function(){
  Clock()
}, 1000);
window.setInterval(function(){
  Weather()
}, 3600000);
