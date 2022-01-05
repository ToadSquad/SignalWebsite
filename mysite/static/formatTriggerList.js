

window.addEventListener("load", function(){
    console.log("loading")
    var elements = document.getElementsByClassName("coins");

    var section = document.getElementsByClassName("triggers")
    
    var string = ""
    for(element in elements){
        console.log(elements[element].innerText)
        if(true){
            string += `<div class="card">
                            <div class="text">${elements[element].innerText}</div>
                      </div>
            `
            elements[element].innerHTML = ''
        }
        
        
    }
    console.log(string)
    section[0].innerHTML = string
});

