// Value Array
let sudoku_values = [];
let initialised = false;

const SUDOKU_SIZE = 9;

// initialise Value Array
if (sudoku_values.length < SUDOKU_SIZE) {
    sudoku_values = [];
    for(let i = 0; i < 9; i++) {
        sudoku_values.push([]);
        for(let k = 0; k < 9; k++) {
            sudoku_values[i].push(NaN);
        }
    }
}

$(document).ready(
    function() {
        // Only accept number inputs
        $(".sudoku input").on("keypress", 
            function(e) {
                return e.charCode >= 48 && e.charCode <= 57;
                // 48 = '0'; 58 = '9'
            }
        )
        
        {
            let inputs = $(".sudoku input")
            // first value of array is ignored (its the prototype and not a relevant object)
            for (let i = 1; i < inputs.length; i++) {
                parse_and_check(inputs[i])
            }
        }

        // Add the listeners for input events
        $(".sudoku input").on("change",
            function (e) {
                parse_and_check(e.target)
            }
        )

        // Add Listener to clear sudoku button
        $("button#clear-sudoku-btn").on("click",
            function() {
                let inputs = $(".sudoku input")
                // first value of array is ignored (its the prototype and not a relevant object)
                for (let i = 1; i < inputs.length; i++) {
                    inputs[i].value = NaN
                    parse_and_check(inputs[i])
                }
            }
        )
    }
)

// get the field indexes from the input id
function get_indexes_from_id(input_object) {
    // ID Format: "y_x"
    str = input_object.id;
    y = Number.parseInt(str[0]);
    x = Number.parseInt(str[2]);
    return [y, x];
}

// perform the simple checks whether the input is allowed
function check_input_allowed(y, x) {
    return check_number(y, x) && check_per_row(y, x) && check_per_column(y, x) && check_per_block(y, x); 
}

// check number
function check_number(y, x) {
    let number = sudoku_values[y][x];
    return ((number >= 1) && (number <= 9)) || isNaN(number)
}

// check by row
function check_per_row(y, x_chk) {
    let number = sudoku_values[y][x_chk];
    let valid = true;
    for(let x_cur = 0; x_cur < SUDOKU_SIZE; x_cur++) {
        if (x_chk != x_cur) {
            valid = !(sudoku_values[y][x_cur] === number);
            if (!valid) { break; }
        }
    }
    return valid;
}

// check by column
function check_per_column (y_chk, x) {
    let number = sudoku_values[y_chk][x];
    let valid = true;
    for (let y_cur = 0; y_cur < SUDOKU_SIZE; y_cur++) {
        if (y_chk != y_cur) {
            valid = !(sudoku_values[y_cur][x] === number);
            if (!valid) { break; }
        }
    }
    return valid;
}

// check by block
function check_per_block(y_chk, x_chk) {
    let number = sudoku_values[y][x];
    let [y_strt, x_strt] = get_block_starts(y_chk, x_chk);
    let valid = true;
    for (let y_cur = y_strt; y_cur < y_strt + 3; y_cur++) {
        if (valid) {
            for (let x_cur = x_strt; x_cur < x_strt + 3; x_cur++) {
                if (y_cur != y_chk || x_cur != x_chk) {
                    valid = !(sudoku_values[y_cur][x_cur] === number);
                    if (!valid) { break; }
                }
            }
        }
    } 
    return valid;
}

// get block start nodes (top left)
// returns: [y_min, x_min]
function get_block_starts(y,x) {
    let starts = [NaN, NaN];
    starts[0] = Math.floor(y / 3) * 3;
    starts[1] = Math.floor(x / 3) * 3;
    return starts;
}

// parse and check the value of a given sudoku field
function parse_and_check(input_field) {
    let [y,x] = get_indexes_from_id(input_field);
    // Add new value to value array
    sudoku_values[y][x] = Number.parseInt(input_field.value);
    if (check_input_allowed(y,x)) {
        $(input_field).removeClass("sudoku-field-incorrect");
        if ($(".sudoku-field-incorrect").length === 0) {
            $("#submit-sudoku-btn").prop("disabled", false);  // enable Validate Button when no incorrect fields are left
        }
    } else {
        $(input_field).addClass("sudoku-field-incorrect");
        $("#submit-sudoku-btn").prop("disabled", true);  // disable Validate Button
    }
}