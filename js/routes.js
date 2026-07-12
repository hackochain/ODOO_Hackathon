/* ==========================================
        TransitOps Route Management
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

    menuBtn.addEventListener("click",()=>{

        sidebar.classList.toggle("active");

    });

}



/* ==========================================
        Leaflet Map
========================================== */


const map = L.map("routeMap").setView(
    [13.0827,80.2707],
    12
);



L.tileLayer(
"https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
{

    attribution:
    "© OpenStreetMap contributors"

}

).addTo(map);





/* ==========================================
        Route Path
========================================== */


const routeCoordinates=[

[13.0827,80.2707],

[13.0674,80.2376],

[13.0569,80.2425],

[13.0418,80.2341],

[13.0120,80.2210]

];



const routeLine =
L.polyline(
routeCoordinates,
{

    color:"#2563EB",

    weight:5,

    opacity:.8

}

).addTo(map);





map.fitBounds(
routeLine.getBounds()
);





/* ==========================================
        Stop Markers
========================================== */


const stops=[


{

name:"Central Station",

lat:13.0827,

lng:80.2707

},


{

name:"City Mall",

lat:13.0674,

lng:80.2376

},


{

name:"University",

lat:13.0569,

lng:80.2425

},


{

name:"Airport Road",

lat:13.0418,

lng:80.2341

},


{

name:"Terminal",

lat:13.0120,

lng:80.2210

}


];




stops.forEach(stop=>{


L.marker(
[stop.lat,stop.lng]
)

.addTo(map)

.bindPopup(

`

<div>

<h6>${stop.name}</h6>

<p>
Route Stop
</p>

</div>

`

);


});






/* ==========================================
        Bus Marker
========================================== */


const busIcon =
L.divIcon({

html:

`

<i class="fa-solid fa-bus"
style="
font-size:25px;
color:#06B6D4;
">
</i>

`,

className:""

});




const busMarker =
L.marker(

[13.0569,80.2425],

{
icon:busIcon
}

)

.addTo(map);



busMarker.bindPopup(

`

<h6>Bus TR-101</h6>

<p>
Speed : 42 km/h
</p>

<p>
Status : Running
</p>

`

);





/* ==========================================
        Route Search
========================================== */


const search =
document.getElementById("routeSearch");



const routes =
document.querySelectorAll(".route-card");



if(search){


search.addEventListener(
"keyup",
()=>{


let keyword =
search.value.toLowerCase();



routes.forEach(route=>{


let text =
route.innerText.toLowerCase();



if(text.includes(keyword)){


route.style.display="block";


}

else{


route.style.display="none";


}



});


}

);


}





/* ==========================================
        Delete Route
========================================== */


const deleteButtons =
document.querySelectorAll(
".btn-outline-danger"
);



deleteButtons.forEach(button=>{


button.addEventListener(
"click",
()=>{


const card =
button.closest(".route-card");



const name =
card.querySelector("h4")
.innerText;



if(confirm(
"Delete "+name+"?"
)){


card.remove();


}


}

);


});





/* ==========================================
        View Route
========================================== */


document
.querySelectorAll(".btn-outline-info")
.forEach(button=>{


button.addEventListener(
"click",
()=>{


const card =
button.closest(".route-card");


const route =
card.querySelector("h4")
.innerText;



alert(

route+
" details opened."

);


}

);


});





/* ==========================================
        Edit Route
========================================== */


document
.querySelectorAll(".btn-outline-warning")
.forEach(button=>{


button.addEventListener(
"click",
()=>{


alert(
"Route editing module coming soon."
);


}

);


});





});