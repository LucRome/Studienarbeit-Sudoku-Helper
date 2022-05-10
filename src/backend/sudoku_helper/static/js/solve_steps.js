var current_step = 1;

$(document).ready( function() {
    $("#nxt-hint-btn").click(function() {
        current_step += 1;
        if (current_step == 2) {
            // Show candidates
            add_candidates();
            $(".candidate-table").removeClass("invisible");
            $(".candidate-legend").show();
        }
        if (current_step == 3) {
            // mark candidates
            // function from the algorithm scripts
            mark_candidates();
            $(".quickinfo-step[step=1]").hide();
            $(".quickinfo-step[step=3]").show();
        }
        if (current_step == 4) {
            // enter changes
            // function from algorithm scripts
            enter_changes();
            $(".quickinfo-step[step=3]").hide();
            $(".quickinfo-step[step=4]").show();
            $("#nxt-hint-btn").hide();
            $("#solve-sudoku-btn").show();
            $(".field-legend").show();
        }
    })
})