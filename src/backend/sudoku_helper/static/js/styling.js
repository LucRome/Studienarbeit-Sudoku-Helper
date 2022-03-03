// Apply the font size of the sudoku to all texts and icons
$(document).ready(
    function() {
        resize_all_texts();
        $(window).resize(
            function() {
                resize_all_texts();
            }
        );
    }
)

function resize_all_texts() {
    fs_in_str = $("input#0_0").css("font-size");
    unit = fs_in_str.substr(fs_in_str.length - 2);
    size_inputs = fs_in_str.substr(0, fs_in_str.length - 2);
    size_rest = Number.parseFloat(size_inputs) / 2;

    fs_rest_str = size_rest + unit;

    $("p, span, button, a").css("font-size", fs_rest_str)
}