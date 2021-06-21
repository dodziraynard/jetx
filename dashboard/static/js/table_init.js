// Load tables when page is done loading.
$(document).ready(() => {
    table = document.querySelector("table")
    $(table)?.DataTable()
});
