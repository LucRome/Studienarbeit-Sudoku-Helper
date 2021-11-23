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

        // Add the listeners for input events
        $(".sudoku input").on("change",
            function (e) {
                let [y,x] = get_indexes_from_id(e.target);
                // Add new value to value array
                sudoku_values[y][x] = Number.parseInt(e.target.value);
                if (check_input_allowed(y,x)) {
                    $(e.target).removeClass("sudoku-field-incorrect");
                } else {
                    $(e.target).addClass("sudoku-field-incorrect");
                }
            }
        )

        // Add Listener to clear sudoku button
        $("button#clear-sudoku-btn").on("click",
            function() {
                for (let y = 0; y < SUDOKU_SIZE; y++) {
                    for (let x = 0; x < SUDOKU_SIZE; x++) {
                        sudoku_values[y][x] = NaN;
                    }
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
    return check_per_row(y, x) && check_per_column(y, x) && check_per_block(y, x); 
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