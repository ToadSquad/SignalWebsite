


//https://www.coingecko.com/en/api/documentation

var script = document.createElement("SCRIPT");
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js';
script.type = 'text/javascript';
head = document.getElementsByTagName("head")[0].appendChild(script);

script.onreadystatechange = handler;
script.onload = handler;



function handler(){
    //$('th').on('click',sortTable)
}

const Http = new XMLHttpRequest();
const url="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false";
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
    console.log(Http.responseText)

var data = JSON.parse(Http.responseText) 

var table = document.getElementById("pricedata")

for (var x = 0; x < data.length; x++){
    var row = `<tr>
            <td>${data[x]["name"]}</td>
            <td>${data[x]["current_price"]}</td>
            <td>${data[x]["market_cap"]}</td>
            <td>${data[x]["price_change_percentage_24h"]}</td>
            </tr>
    `
    table.innerHTML += row
}
}
function sortTable() {
    var column = $(this).data('column')
    var order = $(this).data('order')
    console.log('Coloumn was clicked '+column+' '+order)
    var data = JSON.parse(Http.responseText) 
    var table = document.getElementById("pricedata")

    var text = $(this).html()
    text = text.substring(0,text.length-1)

    if(order == 'desc'){
        $(this).data('order','asc')
        text += '&#9660'
        data = data.sort((a,b) => a[column] > b[column] ? 1 : -1)
    }
    else {
        $(this).data('order','desc')
        text += '&#9650'
        data = data.sort((a,b) => a[column] < b[column] ? 1 : -1)
    }
    $(this).html(text)
    console.log(data)
    table.innerHTML = ''
    for (var x = 0; x < data.length; x++){
        var row = `<tr>
                <td>${data[x]["name"]}</td>
                <td>${data[x]["current_price"]}</td>
                <td>${data[x]["market_cap"]}</td>
                <td>${data[x]["price_change_percentage_24h"]}</td>
                </tr>
        `
        
        table.innerHTML += row
    }
}


