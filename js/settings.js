/* ==========================================
        TransitOps Settings Controller
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
        Save Settings
========================================== */


const saveButton =
document.querySelector(
".settings-card .btn-primary"
);



if(saveButton){


saveButton.addEventListener(
"click",
()=>{


saveButton.innerHTML = `

<i class="fa-solid fa-spinner fa-spin"></i>

Saving...

`;



setTimeout(()=>{


saveButton.innerHTML = `

Save Changes

`;



alert(
"Settings updated successfully!"
);



},1500);



});



}







/* ==========================================
        Toggle Notification Message
========================================== */


const switches =
document.querySelectorAll(
".form-check-input"
);



switches.forEach(
(toggle)=>{


toggle.addEventListener(
"change",
()=>{


let status =
toggle.checked
?
"Enabled"
:
"Disabled";



console.log(
"Setting:",
status
);



});


});








/* ==========================================
        Settings Search
========================================== */


const search =
document.querySelector(
".search-box input"
);



const cards =
document.querySelectorAll(
".settings-card"
);



if(search){


search.addEventListener(
"keyup",
()=>{


let value =
search.value.toLowerCase();



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






/* ==========================================
        Auto Save Simulation
========================================== */


let changes = false;



switches.forEach(
(item)=>{


item.addEventListener(
"change",
()=>{


changes=true;


});


});



window.addEventListener(
"beforeunload",
(e)=>{


if(changes){


e.preventDefault();


e.returnValue="";


}


});






});