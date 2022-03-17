// Apply the font size of the sudoku to all texts and icons
$(document).ready(
    function() {
        resize_all();
        $(window).resize(
            function() {
                resize_all();
            }
        );
    }
)

function resize_all() {
    // Resize Text around the sudoku form
    fs_in_str = $($("#form-sudoku input")[1]).css("font-size");
    unit = fs_in_str.substr(fs_in_str.length - 2);
    size_inputs = fs_in_str.substr(0, fs_in_str.length - 2);
    size_rest = Number.parseFloat(size_inputs) / 2;

    fs_rest_str = size_rest + unit;

    $("p, span, button, a, strong").css("font-size", fs_rest_str)

    // Resize Candidates
    // First get size of the input fields
    size_str = $($("#form-sudoku input")[1]).css("width");
    unit = size_str.substr(size_str.length - 2);
    size = size_str.substr(0, size_str.length - 2);

    size_candidates = Number.parseFloat(size) / 3;
    size_candidates_str = size_candidates + unit;
    $(".candidate-table td").css("width", size_candidates_str);
    $(".candidate-table td").css("height", size_candidates_str);

    console.log(`inputs: ${size_str} \nCandidates: ${size_candidates_str}`)
}