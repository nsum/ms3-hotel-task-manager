$(document).ready(function(){
    // Initialize mobile side nav
    $('.sidenav').sidenav({edge: "right"});

    // Initialize accordion
    $('.collapsible').collapsible();

    // Initialize tooltips
    $('.tooltipped').tooltip();

    // Initialize date picker
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 1,
        showClearBtn: true,
        // disables picking days in the past
        minDate: new Date(),
        i18n: {
            done: "Select"
        }
    });
});