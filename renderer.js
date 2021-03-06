// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
function Weather(){
  let city = "kathmandu"
  let weatherApiKey = "09e40b1c0da9d4171b249c629d8755dc"
  let apiUrl = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+weatherApiKey+"&units=metric";
  $.ajax({
     type: 'GET',
     url: apiUrl,
     success: function( data ) {
       let retData = "<img class='weath-icon' src='res/img/"+data.weather[0].icon+".png'><p class='mid-font'>"+data.main.temp+ " &#8451;, "+data.weather[0].description+"</p><p class='mid-font'>"+data.name+"</p>"
       let wt = document.getElementsByClassName("weath")
       wt[0].innerHTML = retData
     },
     error: function(xhr, status, error) {
        // check status && error
        // alert(error)
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
        // alert(error)

     },
     dataType: 'json'
  });
}
function News(){
  let apiUrl = "https://news.google.com/news/rss/headlines/section/topic/TECHNOLOGY"
  $.ajax({
     type: 'GET',
     url: apiUrl,
     success: function( data ) {
       let item = data.getElementsByTagName("item")
       let newsHeadlines = ""
       for (let i=0; i<3; i++){
         let title = item[getRandomInt(0, item.length)].getElementsByTagName("title")[0].innerHTML
         newsHeadlines = newsHeadlines + "<p class='small-font'>" + title + "</p>"
       }
       let retData = newsHeadlines
       let wt = document.getElementsByClassName("nes")
       wt[0].innerHTML = retData
     },
     error: function(xhr, status, error) {
        // check status && error
        // alert(error)

     },
     dataType: 'xml'
  });
}
function Events(){
  let apiUrl = "https://www.ashesh.com.np/calendar-event/event_en.html"
  let eventList = ""
  $.ajax({
     type: 'GET',
     url: apiUrl,
     success: function( data ) {
       $result = $(data).find(".ev_left")
       for (let i=0; i<5; i++){
         eventList += "<p>"+$result[i].innerHTML+"</p>"
       }
       let retData = eventList
       let wt = document.getElementsByClassName("evt")
       wt[0].innerHTML = retData
     },
     error: function(xhr, status, error) {
        // check status && error
        // alert(error)

     },
     dataType: 'html'
  });
}
Weather()
Quote()
News()
Events()
window.setInterval(function(){
  News()
}, 20000);
window.setInterval(function(){
  Weather()
  Events()
}, 3600000);
