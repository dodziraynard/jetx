passwordInputs = document.querySelectorAll("input[type=password]");
forms = document.querySelectorAll("form");

forms.forEach((form) => {
  form.addEventListener("submit", (event) => {
    const password = passwordInputs[0].value;
    passwordInputs.forEach((input) => {
      if (input.value !== password) {
        event.preventDefault();
        alert("Passwords do not match.");
      }
    });
  });
});
