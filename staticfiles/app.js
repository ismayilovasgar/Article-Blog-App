// // suppose the `id` attribute of element is `message_container`.
// let message_ele = document.getElementById("message");
// setTimeout(function () {
//   console.log("hello");
//   message_ele.style.display = "none";
// }, 5000);
// message_ele.remove;
// // Timeout is 3 sec, you can change it
const dropdownElement = document.getElementById("dropdown");
const dropdownMenu = document.querySelector(".dropdown__menu");
const downIcon = document.getElementById("down__icon");
const upIcon = document.getElementById("up__icon");

dropdownElement.addEventListener("click", () => {
  dropdownMenu.classList.toggle("show");
  upIcon.classList.toggle("show");
  downIcon.classList.toggle("show");
});
