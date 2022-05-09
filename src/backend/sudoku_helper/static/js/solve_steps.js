current_step = 1;

$(document).ready( function() {
    $("#nxt-hint-btn").click(function() {
        // TODO: implement show/hide for modal
        current_step += 1;
        if (current_step == 2) {
            // Show candidates
            $(".candidate-table").removeClass("invisible");
            $("#candidate-legend").removeAttr("hidden");
        }
        if (current_step == 3) {
            // mark candidates
            // function from the algorithm scripts
            mark_candidates();
            $("#quickinfo-step-1").addAttr("hidden");
            $("#quickinfo-step-3").removeAttr("hidden");
        }
        if (current_step == 4) {
            // enter changes
            // function from algorithm scripts
            enter_changes();
            $("#quickinfo-step-3").addAttr("hidden");
            $("#quickinfo-step-4").removeAttr("hidden");
            $("#nxt-hint-btn").addAttr("hidden");
            $("#solve-sudoku-btn").removeAttr("hidden");
            $("#field-legend").removeAttr("hidden");
        }
    })
})