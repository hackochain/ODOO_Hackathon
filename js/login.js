/* ==========================================
   TransitOps Login JavaScript
========================================== */

document.addEventListener("DOMContentLoaded", () => {

    const passwordInput = document.getElementById("password");
    const togglePassword = document.getElementById("togglePassword");
    const loginForm = document.getElementById("loginForm");
    const loginButton = document.querySelector(".login-btn");

    /* ==============================
       Show / Hide Password
    ============================== */

    togglePassword.addEventListener("click", () => {

        const icon = togglePassword.querySelector("i");

        if (passwordInput.type === "password") {

            passwordInput.type = "text";

            icon.classList.remove("fa-eye");
            icon.classList.add("fa-eye-slash");

        } else {

            passwordInput.type = "password";

            icon.classList.remove("fa-eye-slash");
            icon.classList.add("fa-eye");

        }

    });

    /* ==============================
       Login Form
    ============================== */

    loginForm.addEventListener("submit", function (e) {

        e.preventDefault();

        const email = document.querySelector("input[type='email']").value.trim();
        const password = passwordInput.value.trim();

        if (email === "" || password === "") {

            showToast("Please fill all fields.", "danger");
            return;

        }

        loginButton.disabled = true;

        loginButton.innerHTML = `
            <span class="spinner-border spinner-border-sm me-2"></span>
            Signing In...
        `;

        setTimeout(() => {

            showToast("Login Successful!", "success");

            setTimeout(() => {

                window.location.href = "dashboard.html";

            }, 1200);

        }, 1800);

    });

    /* ==============================
       Demo User Button
    ============================== */

    const demoBtn = document.querySelector(".guest-btn");

    demoBtn.addEventListener("click", () => {

        showToast("Opening Demo Dashboard...", "primary");

        setTimeout(() => {

            window.location.href = "dashboard.html";

        }, 1200);

    });

});


/* ==========================================
            Toast Notification
========================================== */

function showToast(message, type = "primary") {

    const oldToast = document.querySelector(".custom-toast");

    if (oldToast) oldToast.remove();

    const toast = document.createElement("div");

    toast.className = `custom-toast bg-${type}`;

    toast.innerHTML = `
        <i class="fa-solid fa-circle-check me-2"></i>
        ${message}
    `;

    document.body.appendChild(toast);

    setTimeout(() => {

        toast.classList.add("show");

    }, 100);

    setTimeout(() => {

        toast.classList.remove("show");

        setTimeout(() => {

            toast.remove();

        }, 300);

    }, 2500);

}