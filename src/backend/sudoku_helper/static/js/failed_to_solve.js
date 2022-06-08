var solution_shown;

$(document).ready(function() {
    $(".solution-value").hide();
    solution_shown = false;

    $("#toggle-solution-btn").click(function() {
        if (solution_shown) {
            $(".solution-value").hide();
        } else {
            $(".solution-value").show();
        }
        solution_shown = !solution_shown;
    })
})