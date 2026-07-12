/* ==========================================
        TransitOps Chart Engine
========================================== */


document.addEventListener("DOMContentLoaded",()=>{



/* ===============================
        Passenger Growth Chart
================================ */


const passengerCanvas =
document.getElementById("passengerChart");


if(passengerCanvas){


new Chart(
passengerCanvas,
{

type:"line",


data:{


labels:[

"Jan",
"Feb",
"Mar",
"Apr",
"May",
"Jun"

],


datasets:[{

label:"Passengers",

data:[

180,
195,
210,
225,
240,
248

],


borderWidth:3,

tension:.4,

fill:true


}]


},


options:{


responsive:true,


plugins:{


legend:{


labels:{


color:"#94A3B8"


}


}


},



scales:{


x:{


ticks:{


color:"#94A3B8"


}


},


y:{


ticks:{


color:"#94A3B8"


}


}


}



}


}

);


}







/* ===============================
        Revenue Chart
================================ */


const revenueCanvas =
document.getElementById("revenueChart");



if(revenueCanvas){


new Chart(
revenueCanvas,
{


type:"doughnut",



data:{


labels:[

"Bus Tickets",

"Passes",

"Corporate",

"Others"

],


datasets:[{


data:[

45,
25,
20,
10

],


borderWidth:0


}]


},



options:{


responsive:true,


plugins:{


legend:{


position:"bottom",


labels:{


color:"#94A3B8"


}


}


}


}


}

);


}









/* ===============================
        Fuel Chart
================================ */


const fuelCanvas =
document.getElementById("fuelChart");



if(fuelCanvas){


new Chart(
fuelCanvas,
{


type:"bar",



data:{


labels:[

"Route 101",
"Route 205",
"Route 330",
"Route 450"

],



datasets:[{


label:"Fuel Usage (L)",


data:[

320,
280,
350,
260

],


borderWidth:1


}]


},



options:{


responsive:true,


plugins:{


legend:{


labels:{


color:"#94A3B8"


}


}


},



scales:{


x:{


ticks:{


color:"#94A3B8"


}


},


y:{


ticks:{


color:"#94A3B8"


}


}


}


}


}

);


}









/* ===============================
        Delay Analysis Chart
================================ */


const delayCanvas =
document.getElementById("delayChart");



if(delayCanvas){


new Chart(
delayCanvas,
{


type:"line",



data:{


labels:[

"Mon",
"Tue",
"Wed",
"Thu",
"Fri",
"Sat",
"Sun"

],



datasets:[{


label:"Delay Percentage",


data:[

12,
18,
10,
22,
15,
8,
14

],


borderWidth:3,


tension:.4


}]


},




options:{


responsive:true,


plugins:{


legend:{


labels:{


color:"#94A3B8"


}


}


},


scales:{


x:{


ticks:{


color:"#94A3B8"


}


},


y:{


ticks:{


color:"#94A3B8"


}


}


}


}


}

);


}



});