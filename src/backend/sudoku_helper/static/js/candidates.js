var candidates_visible = false;

const BTN_TEXT_SHOW = "Show Candidates";
const BTN_TEXT_HIDE = "Hide Candidates";

$(document).ready(
    function() {
        $("#show-candidates").on("click", function() {
            if (candidates_visible) {
                $(".candidate-table").addClass("invisible");
                $("#show-candidates").text(BTN_TEXT_SHOW);
                candidates_visible = false;
            } else {
                $(".candidate-table").removeClass("invisible");
                $("#show-candidates").text(BTN_TEXT_HIDE);
                candidates_visible = true;
            }
        });
    }
)