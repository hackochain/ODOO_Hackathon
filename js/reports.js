/* ==========================================
        TransitOps Reports Controller
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
        Generate Report
========================================== */


const generateBtn =
document.querySelector(
".btn-primary"
);



if(generateBtn){


generateBtn.addEventListener(
"click",
()=>{


generateBtn.innerHTML = `

<i class="fa-solid fa-spinner fa-spin"></i>

Generating...

`;



setTimeout(()=>{


generateBtn.innerHTML = `

<i class="fa-solid fa-file-circle-plus"></i>

Generate Report

`;



alert(
"Report generated successfully!"
);



},1500);



});


}






/* ==========================================
        Export Buttons
========================================== */


const excelBtn =
document.querySelector(
".btn-outline-success"
);



const pdfBtn =
document.querySelector(
".btn-outline-danger"
);




if(excelBtn){


excelBtn.addEventListener(
"click",
()=>{


alert(
"Excel report exported successfully."
);


});


}





if(pdfBtn){


pdfBtn.addEventListener(
"click",
()=>{


alert(
"PDF report exported successfully."
);


});


}







/* ==========================================
        Report Search
========================================== */


const search =
document.querySelector(
".search-box input"
);



const rows =
document.querySelectorAll(
"tbody tr"
);



if(search){


search.addEventListener(
"keyup",
()=>{


let value =
search.value.toLowerCase();



rows.forEach(row=>{


let text =
row.innerText.toLowerCase();



if(text.includes(value)){


row.style.display="";


}

else{


row.style.display="none";


}



});



});


}







/* ==========================================
        View Report Buttons
========================================== */


const viewButtons =
document.querySelectorAll(
"tbody .btn-primary"
);



viewButtons.forEach(button=>{


button.addEventListener(
"click",
()=>{


let row =
button.closest("tr");


let reportName =
row.children[0]
.innerText;



alert(

"Opening "+reportName

);



});


});






/* ==========================================
        Counter Animation
========================================== */


const counters =
document.querySelectorAll(
".report-card h3"
);



counters.forEach(counter=>{


let value =
parseInt(
counter.innerText
.replace(/[^0-9]/g,"")
);



if(!value)
return;



let current=0;



let timer =
setInterval(()=>{


current++;


counter.innerText =
current;



if(current>=value){


clearInterval(timer);



}



},20);



});






});