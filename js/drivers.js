/* ==========================================
   TransitOps Driver Management
========================================== */


document.addEventListener("DOMContentLoaded",()=>{


    /* ===========================
        Sidebar Toggle
    =========================== */

    const menuBtn =
    document.getElementById("menuBtn");

    const sidebar =
    document.querySelector(".sidebar");


    if(menuBtn){

        menuBtn.addEventListener("click",()=>{

            sidebar.classList.toggle("active");

        });

    }



    /* ===========================
        Driver Search
    =========================== */


    const search =
    document.getElementById("driverSearch");


    const drivers =
    document.querySelectorAll(".driver-card");


    if(search){

        search.addEventListener("keyup",()=>{


            let keyword =
            search.value.toLowerCase();



            drivers.forEach(driver=>{


                let name =
                driver.innerText.toLowerCase();



                if(name.includes(keyword)){

                    driver.style.display="block";

                }

                else{

                    driver.style.display="none";

                }


            });


        });


    }




    /* ===========================
        View Driver
    =========================== */


    const viewButtons =
    document.querySelectorAll(".btn-outline-info");


    viewButtons.forEach(button=>{


        button.addEventListener("click",()=>{


            const card =
            button.closest(".driver-card");


            const name =
            card.querySelector("h4").innerText;



            alert(

            "Opening profile of "+name

            );


        });


    });





    /* ===========================
        Edit Driver
    =========================== */


    const editButtons =
    document.querySelectorAll(".btn-outline-warning");



    editButtons.forEach(button=>{


        button.addEventListener("click",()=>{


            const card =
            button.closest(".driver-card");


            const name =
            card.querySelector("h4").innerText;



            alert(

            "Edit details for "+name

            );


        });


    });





    /* ===========================
        Delete Driver
    =========================== */


    const deleteButtons =
    document.querySelectorAll(".btn-outline-danger");



    deleteButtons.forEach(button=>{


        button.addEventListener("click",()=>{


            const card =
            button.closest(".driver-card");



            const name =
            card.querySelector("h4").innerText;




            const confirmDelete =
            confirm(

            "Remove driver "+name+"?"

            );



            if(confirmDelete){


                card.remove();


                updateDriverCount();


            }



        });


    });






    /* ===========================
        Update Driver Count
    =========================== */


    function updateDriverCount(){


        const totalDrivers =
        document.querySelectorAll(".driver-card").length;



        const countCard =
        document.querySelector(".fleet-stat h2");



        if(countCard){

            countCard.innerText =
            totalDrivers;

        }


    }





    /* ===========================
        Card Animation Delay
    =========================== */


    drivers.forEach((card,index)=>{


        card.style.animationDelay =
        `${index*0.1}s`;


    });




});