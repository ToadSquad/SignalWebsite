


//https://www.coingecko.com/en/api/documentation

var script = document.createElement("SCRIPT");
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js';
script.type = 'text/javascript';
head = document.getElementsByTagName("head")[0].appendChild(script);

script.onreadystatechange = handler;
script.onload = handler;



function handler(){
    console.log("clicked")
    $('th').on('click',sortTable)
}

const Http = new XMLHttpRequest();
const url="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C1y";
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
    console.log(Http.responseText)

var data = JSON.parse(Http.responseText) 

var table = document.getElementById("pricedata")

for (var x = 0; x < data.length; x++){
    var row = `<tr>
    <td class="coin"><img class = "image" src="${data[x]["image"]}" alt="" border=3 height=16 width=16></img>${" "+data[x]["name"].toUpperCase()+" ("+data[x]["symbol"].toUpperCase()+")"}</td>
    <td>$${numberWithCommas(data[x]["current_price"])}</td>
    <td>$${numberWithCommas(data[x]["market_cap"])}</td>
    <td>${(data[x]["price_change_percentage_1h_in_currency"]).toPrecision(2)}%</td>
    <td>${(data[x]["price_change_percentage_24h_in_currency"]).toPrecision(2)}%</td>
    <td>${(data[x]["price_change_percentage_7d_in_currency"]).toPrecision(2)}%</td>
    <td>${(data[x]["price_change_percentage_1y_in_currency"]).toPrecision(4)}%</td>
    </tr>
`
    table.innerHTML += row
}
}
function numberWithCommas(x) {
    if(x<1){return x;}
    x = x.toString();
    var pattern = /(-?\d+)(\d{3})/;
    while (pattern.test(x))
        x = x.replace(pattern, "$1,$2");
    return x;
}
function apiCall(url){
    const Httpnew = new XMLHttpRequest();
    Httpnew.open("GET", url);
    Httpnew.send();
    Httpnew.onreadystatechange = (e) => {
            //console.log(Http.responseText)
                data = JSON.parse(Httpnew.responseText)
                populateTable(data)
            }
}

function populateTable(data){
    console.log(data)
    var table = document.getElementById("pricedata")
    table.innerHTML = ''
    for (var x = 0; x < data.length; x++){
        var row = `<tr>
        <td class="coin"><img class = "image" src="${data[x]["image"]}" alt="" border=3 height=16 width=16></img>${" "+data[x]["name"].toUpperCase()+" ("+data[x]["symbol"].toUpperCase()+")"}</td>
        <td>$${numberWithCommas(data[x]["current_price"])}</td>
        <td>$${numberWithCommas(data[x]["market_cap"])}</td>
        <td>${(data[x]["price_change_percentage_1h_in_currency"]).toPrecision(2)}%</td>
        <td>${(data[x]["price_change_percentage_24h_in_currency"]).toPrecision(2)}%</td>
        <td>${(data[x]["price_change_percentage_7d_in_currency"]).toPrecision(2)}%</td>
        <td>${(data[x]["price_change_percentage_1y_in_currency"]).toPrecision(4)}%</td>
        </tr>
    `
        
        table.innerHTML += row
    }
}
function sortTable() {
    var column = $(this).data('column')
    var order = $(this).data('order')
    console.log('Coloumn was clicked '+column+' '+order)
    var data = null
    
    var text = $(this).html()
    

    

    if(column=="symbol"){
        if(order == "asc"){
            
            $(this).data('order','dsc')
            text = text.substring(0,text.length-1)
            text += '&#9660'
            urlnew = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=id_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C1y"
            const Httpnew = new XMLHttpRequest();
            Httpnew.open("GET", urlnew);
            Httpnew.send();
            Httpnew.onreadystatechange = (e) => {
            //console.log(Http.responseText)
                data = JSON.parse(Httpnew.responseText)
                populateTable(data)
            }
        }
        
        else{
            
            $(this).data('order','asc')
            text = text.substring(0,text.length-1)
            text += '&#9650'
            urlnew = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=id_asc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C1y"
            const Httpnew = new XMLHttpRequest();
            Httpnew.open("GET", urlnew);
            Httpnew.send();
            Httpnew.onreadystatechange = (e) => {
            //console.log(Http.responseText)
                data = JSON.parse(Httpnew.responseText)
                populateTable(data)
            }
        }
    }
    if(column=="market cap"){
        if(order == "asc"){
            
            $(this).data('order','dsc')
            text = text.substring(0,text.length-1)
            text += '&#9660'
            urlnew = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C1y"
            apiCall(urlnew)
        }
        else {
            $(this).data('order','asc')
            text = text.substring(0,text.length-1)
            text += '&#9650'
            urlnew = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_asc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C1y"
            apiCall(urlnew)
        }

    }
    $(this).html(text)
    /*
    

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
    
    */
    

}


