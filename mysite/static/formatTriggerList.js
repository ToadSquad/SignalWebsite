/*function apiCall(url){
    const Httpnew = new XMLHttpRequest();
    Httpnew.open("GET", url);
    Httpnew.send();
    Httpnew.onreadystatechange = (e) => {
            //console.log(Http.responseText)
                data = JSON.parse(Httpnew.responseText)
                return data;
            }
}

window.addEventListener("load", function(){
    console.log("loading")
    var elements = document.getElementsByClassName("coins");

    var section = document.getElementsByClassName("data")
    
    var string = ""

    var type = ""
    for(element in elements){
        console.log(elements[element].innerText)
        try{
        if(elements[element].innerText.length>3){
            if(elements[element].innerText.includes("Buy")){type = "buy"}
            if(elements[element].innerText.includes("Sell")){type = "sell"}
            coin = elements[element].innerText.split(" ")[0].replace("USDT","")
            //
            //currentPrice = apiCall("https://api.coingecko.com/api/v3/simple/price?ids="+coin+"&vs_currencies=usd")[coin]["usd"]
            string = `<div class="card${type}">
                            <div class="text">${elements[element].innerText}</div>
                      </div>
            `
            section[0].innerHTML += string
        }//<iframe frameBorder='0' scrolling='no' width='800' height='420' src='https://api.stockdio.com/visualization/financial/charts/v1/HistoricalPrices?app-key=471E6142AA3F4F859104396FB72636BE&indicators=BollingerBands(10,2.0);Stochastics(10,10);&stockExchange=CRYPTO&symbol=${coin}&displayPrices=Candlestick&dividends=true&splits=true&palette=Financial-Light'></iframe>
        }
        catch{
            console.log("undefined")
        }
        elements[element].innerHTML = ''
        
        
    }
    console.log(string)
    


*/
window.addEventListener("load", function(){
    console.log("RUNNING")
    var elements = document.getElementsByClassName("price");
    //const Binance = require('node-binance-api');
    const binance = new Binance().options({
    APIKEY: 'cfDpIoySSCjRBkL4QMN0pXr6V0dp4cUqYMoW91tyKuAiMS5XscZuqKfxpX0sOUG7',
    APISECRET: 'i5IiWEsnR9gssVXqXDzJS4Us1jAlyWCsH21fuSJ39ITKHTQPDtQdR3fFOH3fwJdI'
    });
    let ticker = binance.prices();
    for(element in elements){
        elements[element]=ticker.elements[element].innerHTML
        console.log(ticker.elements[element].innerHTML)
    }
});
