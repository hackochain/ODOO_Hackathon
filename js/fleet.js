/* ==========================================
   TransitOps Fleet Management
========================================== */

document.addEventListener("DOMContentLoaded", () => {

    /* ===========================
        Sidebar Toggle
    =========================== */

    const menuBtn = document.getElementById("menuBtn");
    const sidebar = document.querySelector(".sidebar");

    if (menuBtn) {

        menuBtn.addEventListener("click", () => {

            sidebar.classList.toggle("active");

        });

    }

    /* ===========================
        Vehicle Search
    =========================== */

    const searchInput = document.querySelector(
        ".search-box input"
    );

    const rows = document.querySelectorAll("tbody tr");

    searchInput.addEventListener("keyup", () => {

        const keyword = searchInput.value.toLowerCase();

        rows.forEach(row => {

            const text = row.innerText.toLowerCase();

            row.style.display =
                text.includes(keyword) ? "" : "none";

        });

    });

    /* ===========================
        Status Filter
    =========================== */

    const statusSelect =
        document.querySelectorAll(".form-select")[0];

    statusSelect.addEventListener("change", () => {

        const value =
            statusSelect.value.toLowerCase();

        rows.forEach(row => {

            const status =
                row.cells[7].innerText.toLowerCase();

            if (
                value === "all status" ||
                status.includes(value)
            ) {

                row.style.display = "";

            }

            else{

                row.style.display = "none";

            }

        });

    });

    /* ===========================
        Vehicle Type Filter
    =========================== */

    const typeSelect =
        document.querySelectorAll(".form-select")[1];

    typeSelect.addEventListener("change", () => {

        const value =
            typeSelect.value.toLowerCase();

        rows.forEach(row => {

            const type =
                row.cells[2].innerText.toLowerCase();

            if (
                value === "all types" ||
                type.includes(value)
            ) {

                row.style.display = "";

            }

            else{

                row.style.display = "none";

            }

        });

    });

    /* ===========================
        Row Hover Effect
    =========================== */

    rows.forEach(row => {

        row.addEventListener("mouseenter", () => {

            row.style.transform = "scale(1.01)";
            row.style.transition = ".25s";

        });

        row.addEventListener("mouseleave", () => {

            row.style.transform = "scale(1)";

        });

    });

    /* ===========================
        View Button
    =========================== */

    document
    .querySelectorAll(".btn-outline-info")
    .forEach(btn=>{

        btn.addEventListener("click",()=>{

            alert("Vehicle Details page coming soon.");

        });

    });

    /* ===========================
        Edit Button
    =========================== */

    document
    .querySelectorAll(".btn-outline-warning")
    .forEach(btn=>{

        btn.addEventListener("click",()=>{

            alert("Edit Vehicle feature coming soon.");

        });

    });

    /* ===========================
        Delete Button
    =========================== */

    document
    .querySelectorAll(".btn-outline-danger")
    .forEach(btn=>{

        btn.addEventListener("click",()=>{

            if(confirm("Delete this vehicle?")){

                btn.closest("tr").remove();

                updateStats();

            }

        });

    });

    /* ===========================
        Add Vehicle
    =========================== */

    const addBtn =
        document.querySelector(".btn-primary");

    addBtn.addEventListener("click",()=>{

        alert(
            "Vehicle Registration Module will open here."
        );

    });

    /* ===========================
        Update Statistics
    =========================== */

    function updateStats(){

        const totalRows =
            document.querySelectorAll("tbody tr").length;

        const totalCard =
            document.querySelector(".fleet-stat h2");

        totalCard.innerText = totalRows;

    }

});