window.addEventListener("scroll", () => {
  const header = document.getElementById("header");
  header.classList.toggle("scrolled", window.scrollY > 50);
});

// login.js
function login() {
  const role = document.querySelector("select").value;

  localStorage.setItem("userRole", role);

  if(role === "funcionario"){
    alert("Entrou como FUNCIONÁRIO");
  } else {
    alert("Entrou como CLIENTE");
  }
}