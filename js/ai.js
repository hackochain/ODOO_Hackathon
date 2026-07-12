/* ==========================================
        TransitOps AI Center Controller
========================================== */


document.addEventListener("DOMContentLoaded",()=>{



/* ==========================================
        Sidebar Toggle
========================================== */


const menuBtn =
document.getElementById("menuBtn");


const sidebar =
document.querySelector(".sidebar");



if(menuBtn){


menuBtn.addEventListener(
"click",
()=>{


sidebar.classList.toggle("active");


});


}







/* ==========================================
        AI Accuracy Counter
========================================== */


const counters =
document.querySelectorAll(
".ai-card h2"
);



counters.forEach(counter=>{


let value =
parseInt(
counter.innerText
.replace("%","")
);



let current = 0;



let interval =
setInterval(()=>{


current++;


counter.innerText =
current+"%";



if(current>=value){


clearInterval(interval);


}



},20);



});








/* ==========================================
        Recommendation Animation
========================================== */


const recommendations =
document.querySelectorAll(
".recommendation"
);



recommendations.forEach(
(item,index)=>{


item.style.animationDelay =
(index*0.15)+"s";


});








/* ==========================================
        Prediction Click Events
========================================== */


const predictions =
document.querySelectorAll(
".prediction-item"
);



predictions.forEach(item=>{


item.addEventListener(
"click",
()=>{


let title =
item.querySelector("h6")
.innerText;



alert(

title+
" analysis opened."

);



});


});








/* ==========================================
        AI Risk Level Simulation
========================================== */


const riskBar =
document.querySelector(
".risk-progress"
);



if(riskBar){


let risk =
Math.floor(
Math.random()*40
)+20;



riskBar.style.width =
risk+"%";



const riskText =
document.querySelector(
".risk-container"
.nextElementSibling
.querySelector("strong")
);



if(riskText){


riskText.innerText =
risk+"% Risk Level";


}



}






/* ==========================================
        Search AI Insights
========================================== */


const search =
document.querySelector(
".search-box input"
);



if(search){


search.addEventListener(
"keyup",
()=>{


let value =
search.value.toLowerCase();



const cards =
document.querySelectorAll(
".glass-card"
);



cards.forEach(card=>{


let text =
card.innerText.toLowerCase();



if(text.includes(value)){


card.style.display="";


}

else{


card.style.display="none";


}



});


});


}







});