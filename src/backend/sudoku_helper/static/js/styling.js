// Apply the font size of the sudoku to all texts and icons
$(document).ready(
    function() {
        // resize callbacks
        resize_all();
        $(window).resize(
            function() {
                resize_all();
            }
        );
        
        // callbacks to signal loading
        $(".compute-btn").click(function(e) {
            signal_loading(e.target);
        })
    }
)

function resize_all() {
    {
        // Resize Text around the sudoku form (also Spinner animations and images in legends)
        let fs_in_str = $($("#form-sudoku input")[1]).css("font-size");
        let unit = fs_in_str.substr(fs_in_str.length - 2);
        let size_inputs = fs_in_str.substr(0, fs_in_str.length - 2);
        let size_rest = Number.parseFloat(size_inputs) / 2;

        let fs_rest_str = size_rest + unit;

        $("p, span, button, a, strong, b").css("font-size", fs_rest_str)
        $(".spinner-grow").css("width", fs_rest_str);
        $(".spinner-grow").css("height", fs_rest_str);
        
        // Resize images in legends
        $(".candidate-legend img").css("height", fs_rest_str);
        $(".field-legend img").css("height", fs_rest_str).css("width", fs_rest_str);
    }
    {
        // Resize Candidates
        // First get size of the input fields
        let size_str = $($("#form-sudoku input")[1]).css("width");
        let unit = size_str.substr(size_str.length - 2);
        let size = size_str.substr(0, size_str.length - 2);

        let size_candidates = Number.parseFloat(size) / 3;
        let size_candidates_str = size_candidates + unit;
        $(".candidate-field img").css("width", size_candidates_str);
        $(".candidate-field img").css("height", size_candidates_str);
        $(".candidate-field div").css("height", size_candidates_str);
        $(".candidate-field div").css("width", size_candidates_str);
    }
}

const SPINNER_OBJECT = '<span class="spinner-grow spinner-grow-sm"></span>'

function signal_loading(button) {
    // change content of button and add spinner object
    let text = $(button).text().trim();
    if (text === "Validate") {
        text = "Validating..";
    } else if (text === "Solve") {
        text = "Solving..";
    }
    $(button).empty();
    $(button).append(SPINNER_OBJECT + '\n' + text);
    $(button).prop("disabled", true)

    // resize spinner
    let fs_in_str = $($("#form-sudoku input")[1]).css("font-size");
    let unit = fs_in_str.substr(fs_in_str.length - 2);
    let size_inputs = fs_in_str.substr(0, fs_in_str.length - 2);
    let size_rest = Number.parseFloat(size_inputs) / 2;

    let fs_rest_str = size_rest + unit;

    $(".spinner-grow").css("width", fs_rest_str);
    $(".spinner-grow").css("height", fs_rest_str);
}