document.addEventListener("DOMContentLoaded", () => {
  // Hide login error after 5 sec
  const loginError = document.getElementById("login-error");
  if (loginError) {
    setTimeout(() => {
      loginError.style.display = "none";
    }, 5000);
  }

  // Hide field errors while typing
  ["login_username", "login_password"].forEach(id => {
    const input = document.getElementById(id);
    const error = document.getElementById(id + "_error");
    if (input && error) {
      input.addEventListener("input", () => {
        error.style.display = "none";
      });
    }
  });
});

function validateLoginForm() {
  let isValid = true;

  const username = document.getElementById("login_username");
  const password = document.getElementById("login_password");

  if (username.value.trim() === "") {
    document.getElementById("login_username_error").style.display = "block";
    isValid = false;
  }

  if (password.value.trim() === "") {
    document.getElementById("login_password_error").style.display = "block";
    isValid = false;
  }

  return isValid;
}
