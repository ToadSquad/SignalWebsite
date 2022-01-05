

window.addEventListener("load", function(){
    console.log("loading")
    var elements = document.getElementsByClassName("coins");

    var section = document.getElementsByClassName("triggers")
    
    var string = ""
    for(element in elements){
        console.log(elements[element].innerText)
        try{
        if(elements[element].innerText.length>3){
            string += `<div class="card">
                            <div class="text">${elements[element].innerText}</div>
                      </div>
            `
        }
        }
        catch{
            console.log("undefined")
        }
        elements[element].innerHTML = ''
        
        
    }
    console.log(string)
    section[0].innerHTML = string
});

