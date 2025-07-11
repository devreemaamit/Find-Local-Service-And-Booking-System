document.addEventListener("DOMContentLoaded", function () {
    // Live validation removal on input
    const fields = ['full_name', 'email', 'username', 'role', 'password1', 'password2'];

    fields.forEach(field => {
        const input = document.getElementById(field);
        const error = document.getElementById(`${field}_error`);

        if (input && error) {
            input.addEventListener("input", () => {
                error.style.display = "none";
            });
        }
    });
});

// Form validation before submit
function validateForm() {
    let isValid = true;

    // Full Name
    const fullName = document.getElementById("full_name");
    const fullNameError = document.getElementById("full_name_error");
    if (fullName.value.trim() === "") {
        fullNameError.style.display = "block";
        isValid = false;
    }

    // Email
    const email = document.getElementById("email");
    const emailRequired = document.getElementById("email_required");
    const emailInvalid = document.getElementById("email_invalid");

    emailRequired.style.display = "none"; // Hide all first
    emailInvalid.style.display = "none";

    if (email.value.trim() === "") {
        emailRequired.style.display = "block"; // ✅ Show required
        isValid = false;
    } else if (!/^\S+@\S+\.\S+$/.test(email.value)) {
        emailInvalid.style.display = "block"; // ✅ Show invalid
        isValid = false;
    }


    // Username
    const username = document.getElementById("username");
    const usernameError = document.getElementById("username_error");
    if (username.value.trim() === "") {
        usernameError.style.display = "block";
        isValid = false;
    }

    // Role
    const role = document.getElementById("role");
    const roleError = document.getElementById("role_error");
    if (role.value === "") {
        roleError.style.display = "block";
        isValid = false;
    }

    // Password
    const password1 = document.getElementById("password1");
    const password1Error = document.getElementById("password1_error");
    if (password1.value.length < 6) {
        password1Error.style.display = "block";
        isValid = false;
    }

    // Confirm Password
    const password2 = document.getElementById("password2");
    const password2Error = document.getElementById("password2_error");
    if (password2.value !== password1.value) {
        password2Error.style.display = "block";
        isValid = false;
    }

    return isValid;
}
