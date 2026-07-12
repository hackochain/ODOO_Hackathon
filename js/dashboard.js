/* ==========================================
   TransitOps Dashboard JS
========================================== */

document.addEventListener("DOMContentLoaded", () => {

    /* ======================================
            Sidebar Toggle
    ====================================== */

    const menuBtn = document.getElementById("menuBtn");
    const sidebar = document.querySelector(".sidebar");

    if (menuBtn) {

        menuBtn.addEventListener("click", () => {

            sidebar.classList.toggle("active");

        });

    }

    /* ======================================
            Counter Animation
    ====================================== */

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const updateCounter = () => {

            const target = +counter.dataset.target;
            const current = +counter.innerText;

            const increment = Math.ceil(target / 80);

            if (current < target) {

                counter.innerText = current + increment;

                setTimeout(updateCounter, 20);

            } else {

                counter.innerText = target;

            }

        };

        updateCounter();

    });

    /* ======================================
            Leaflet Map
    ====================================== */

    const map = L.map('fleetMap').setView([13.0827, 80.2707], 12);

    L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        {
            attribution: '&copy; OpenStreetMap'
        }
    ).addTo(map);

    /* Vehicle Markers */

    const busIcon = L.icon({

        iconUrl:
        "https://cdn-icons-png.flaticon.com/512/61/61231.png",

        iconSize: [35,35]

    });

    const buses = [

        {
            name:"TR-101",
            lat:13.0827,
            lng:80.2707
        },

        {
            name:"TR-205",
            lat:13.0615,
            lng:80.2496
        },

        {
            name:"TR-118",
            lat:13.1020,
            lng:80.2850
        }

    ];

    buses.forEach(bus=>{

        L.marker(
            [bus.lat,bus.lng],
            {icon:busIcon}
        )
        .addTo(map)
        .bindPopup(`
            <strong>${bus.name}</strong>
            <br>
            Status : Active
        `);

    });

    /* ======================================
            Revenue Chart
    ====================================== */

    const revenueCtx =
        document.getElementById("revenueChart");

    if(revenueCtx){

        new Chart(revenueCtx,{

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

                    label:"Revenue",

                    data:[
                        18,
                        22,
                        24,
                        27,
                        30,
                        35
                    ],

                    borderColor:"#2563EB",

                    backgroundColor:"rgba(37,99,235,.15)",

                    tension:.4,

                    fill:true

                }]

            },

            options:{

                responsive:true,

                plugins:{
                    legend:{
                        labels:{
                            color:"#fff"
                        }
                    }
                },

                scales:{

                    x:{
                        ticks:{
                            color:"#94A3B8"
                        },
                        grid:{
                            color:"rgba(255,255,255,.05)"
                        }
                    },

                    y:{
                        ticks:{
                            color:"#94A3B8"
                        },
                        grid:{
                            color:"rgba(255,255,255,.05)"
                        }
                    }

                }

            }

        });

    }

    /* ======================================
            Fleet Distribution
    ====================================== */

    const fleetCtx =
        document.getElementById("fleetChart");

    if(fleetCtx){

        new Chart(fleetCtx,{

            type:"doughnut",

            data:{

                labels:[
                    "Active",
                    "Maintenance",
                    "Idle"
                ],

                datasets:[{

                    data:[
                        180,
                        35,
                        33
                    ],

                    backgroundColor:[
                        "#10B981",
                        "#F59E0B",
                        "#2563EB"
                    ],

                    borderWidth:0

                }]

            },

            options:{

                plugins:{

                    legend:{

                        labels:{
                            color:"#fff"
                        }

                    }

                }

            }

        });

    }

    /* ======================================
            Live Notification
    ====================================== */

    setInterval(()=>{

        console.log("TransitOps Live Monitoring...");

    },5000);

});