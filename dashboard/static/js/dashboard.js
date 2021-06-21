'use strict';

// Toggling sidebar.
const sideBarItems = document.querySelectorAll(".side-bar-item")
const navBarItems = document.querySelectorAll(".nav-item")
sideBarItems.forEach(item => {
    item.addEventListener("click", (e) => {
        document.querySelectorAll(".side-bar-item.active").forEach(e=>{
            if (e !== item)
            e.classList.remove("active")
        })
        item.classList.toggle("active")
    })
})

navBarItems.forEach(item => {
    item.addEventListener("click", (e) => {
        navBarItems.forEach(e => {
            if (e !== item)
                e?.classList.remove("active")
        })

        item.classList.toggle("active")
    })
})

// Mobile sidebar toggler
const toggler = document.querySelector("#toggler")
const sidebar = document.querySelector("#sidebar")
toggler.addEventListener("click", (e) => {
    sidebar.classList.toggle("fold")
    toggler.classList.toggle("open")
    $("html, body").animate({ scrollTop: 0 }, "slow");
})

// Activate current sidebar element
const activeId = sidebar.dataset.active
document.getElementById(activeId).classList.add("active")

// Show alert when deleting items.
const deletionForms = document.querySelectorAll(".confirmation-form")
deletionForms.forEach(form => {
    form.addEventListener('submit', (event) => {
        const response = confirm("Confirm to proceed with action.");
        if (!response) {
            event.preventDefault()
        }
    })
})


const dateInputElements = document.querySelectorAll(".js-update-date")
dateInputElements.forEach(element => {
    const value = element.getAttribute('value')
    if (!Boolean(value)) return

    var year = parseInt(value.split('T')[0].split('-')[0]);
    var month = parseInt(value.split('T')[0].split('-')[1]);
    var day = parseInt(value.split('T')[0].split('-')[2]);
    var hour = parseInt(value.split('T')[1].split(':')[0]);
    var minute = parseInt(value.split('T')[1].split(':')[1]);
    var second = value.split('T')[1].split(':')[2];
    var localDatetime = year + "-" +
        (month < 10 ? "0" + month.toString() : month) + "-" +
        (day < 10 ? "0" + day.toString() : day) + "T" +
        (hour < 10 ? "0" + hour.toString() : hour) + ":" +
        (minute < 10 ? "0" + minute.toString() : minute) +
        `:00`
    element.value = localDatetime;
})