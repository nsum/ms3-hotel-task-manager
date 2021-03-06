$(document).ready(function(){

    // Collapse tasks lists
    $(`#collapse-personal`).click(function () {
        $(`#personal-tasks`).slideToggle("medium", "linear");
    });

    $(`#collapse-dept`).click(function () {
        $(`#dept-tasks`).slideToggle("medium", "linear");
    });
    
    $(`#collapse-shared`).click(function () {
        $(`#shared-tasks`).slideToggle("medium", "linear");
    });

    // All below is MaterializeCSS's code and is used to initialize its features
    // Initialize floating action button
    $('.fixed-action-btn').floatingActionButton();

    // Initialize Modals
    $('.modal').modal();

    // Initialize mobile side nav
    $('.sidenav').sidenav({edge: "right"});

    // Initialize accordion
    $('.collapsible').collapsible();

    // Initialize tooltips
    $('.tooltipped').tooltip();

    // Initialize Drop-down lists
    $('select').formSelect();

    // Initialize Parallax
    $('.parallax').parallax();

    // Initialize date picker
    $('.datepicker').datepicker({
        format: "dd/mmm/yyyy",
        yearRange: 1,
        showClearBtn: true,
        // disables picking days in the past
        minDate: new Date(),
        i18n: {
            done: "Select"
        }
    });

    // Fix for dropdown validate bug
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});