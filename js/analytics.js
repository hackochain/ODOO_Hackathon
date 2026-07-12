/* ==========================================
        TransitOps Analytics Controller
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
        Animated KPI Counters
========================================== */


const counters =
document.querySelectorAll(
".analytics-card h2"
);



counters.forEach(counter=>{


let text =
counter.innerText;



let number =
parseInt(
text.replace(/[^0-9]/g,"")
);



if(!number) return;



let current = 0;



let increment =
Math.ceil(number/80);



let timer =
setInterval(()=>{


current += increment;



if(current >= number){


current = number;


clearInterval(timer);


}



if(text.includes("K")){


counter.innerText =
current+"K";


}

else if(text.includes("₹")){


counter.innerText =
"₹"+current+"L";


}

else if(text.includes("%")){


counter.innerText =
current+"%";


}

else{


counter.innerText =
current;


}



},20);



});







/* ==========================================
        Analytics Search
========================================== */


const searchInput =
document.querySelector(
".search-box input"
);



if(searchInput){


searchInput.addEventListener(
"keyup",
()=>{


let value =
searchInput.value.toLowerCase();



const cards =
document.querySelectorAll(
".glass-card"
);



cards.forEach(card=>{


let content =
card.innerText.toLowerCase();



if(content.includes(value)){


card.style.display="";


}

else{


card.style.display="none";


}



});



});


}







/* ==========================================
        Report Generation Button Support
========================================== */


window.generateAnalyticsReport =
function(){


alert(

"Analytics report generated successfully."

);


};






/* ==========================================
        AI Insight Animation
========================================== */


const insights =
document.querySelectorAll(
".insight-box"
);



insights.forEach(
(item,index)=>{


item.style.animationDelay =
(index*0.15)+"s";


});





});