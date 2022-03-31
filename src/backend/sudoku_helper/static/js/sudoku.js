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
        
        // parse all fields (may be already filled)
        let inputs = $(".sudoku input")
        for (let i = 1; i < inputs.length; i++) {
            // first value of array is ignored (its the prototype and not a relevant object)
            parse(inputs[i])
        }
        // check all rows, columns and blocks
        for (let y = 0; y < SUDOKU_SIZE; y++) {
            check_row(y);
        }
        for (let x = 0; x < SUDOKU_SIZE; x++) {
            check_column(x);
        }
        for (let y = 0; y < SUDOKU_SIZE; y = y+3) {
            for (let x = 0; x < SUDOKU_SIZE; x = x+3) {
                check_block(y, x);
            }
        }
        check_validation_possible();

        // Add the listeners for input events
        $(".sudoku input").on("change",
            function (e) {
                let [y, x] = parse(e.target);
                check_input(y, x);
                check_validation_possible(y, x);
            }
        )

        // Add Listener to clear sudoku button
        $("button#clear-sudoku-btn").on("click",
            function() {
                let inputs = $(".sudoku input")
                // first value of array is ignored (its the prototype and not a relevant object)
                for (let i = 1; i < inputs.length; i++) {
                    inputs[i].value = NaN
                    parse(inputs[i])
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
function check_input(y, x) {
    if (check_number(y, x)) {
        clear_blk_col_row(y, x);
        check_row(y);
        check_column(x); 
        check_block(y, x); 
    }
}

// clear block, column, row
function clear_blk_col_row(y, x) {
    // column
    for (let i = 0; i < SUDOKU_SIZE; i++) {
        $(`#${i}_${x}`).removeClass("sudoku-field-incorrect");
    }
    // row
    for (let i = 0; i < SUDOKU_SIZE; i++) {
        $(`#${y}_${i}`).removeClass("sudoku-field-incorrect");        
    }
    // block
    let [y_strt, x_strt] = get_block_starts(y, x);
    let y_end = y_strt + 3;
    let x_end = x_strt + 3;
    for (let i = y_strt; i < y_end; i++) {
        for (let k = x_strt; k < x_end; k++) {
            $(`#${i}_${k}`).removeClass("sudoku-field-incorrect");
        }
    }
}

// check number
function check_number(y, x) {
    let number = sudoku_values[y][x];
    if (!(((number >= 1) && (number <= 9)) || isNaN(number))) {
        $(`#${y}_${x}`).addClass("sudoku-field-incorrect");
        return false;
    }
    return true;
}

// check row
function check_row(y) {
    // first sort the indexes of the input fields according to their value
    let value_indexes = [[], [], [], [], [], [], [], [], []]
    for (let x = 0; x < SUDOKU_SIZE; x++) {
        let val = sudoku_values[y][x];
        if (!isNaN(val)) {
            value_indexes[val - 1].push(x);
        }
    }

    // add class sudoku-field-incorrect to the fields whose value occurs > 1
    value_indexes.forEach(indexes => {
        if(indexes.length > 1) {
            // mark all fields
            indexes.forEach(x => {
                $(`#${y}_${x}`).addClass("sudoku-field-incorrect");
            })
        }
    })
}

// check by column
function check_column(x) {
    // first sort the indexes of the input fields according to their value
    let value_indexes = [[], [], [], [], [], [], [], [], []]
    for (let y = 0; y < SUDOKU_SIZE; y++) {
        let val = sudoku_values[y][x];
        if (!isNaN(val)) {
            value_indexes[val - 1].push(y);
        }
    }

    // add class sudoku-field-incorrect to the fields whose value occurs > 1
    value_indexes.forEach(indexes => {
        if(indexes.length > 1) {
            // mark all fields
            indexes.forEach(y => {
                $(`#${y}_${x}`).addClass("sudoku-field-incorrect");
            })
        }
    })
}

// check block
function check_block(y, x) {
    // first sort the indexes of the input fields according to their value
    let value_indexes = [[], [], [], [], [], [], [], [], []];
    let [y_strt, x_strt] = get_block_starts(y, x);
    let [y_end, x_end] = [y_strt + 3, x_strt + 3]
    for (let i = y_strt; i < y_end; i++) {
        for (let k = x_strt; k < x_end; k++) {
            let val = sudoku_values[i][k];
            if (!isNaN(val)) {
                value_indexes[val - 1].push([i, k]);
            }
        }
    }

    // add class sudoku-field-incorrect to the fields whose value occurs > 1
    value_indexes.forEach(indexes => {
        if(indexes.length > 1) {
            // mark all fields
            indexes.forEach(coords => {
                let [y_field, x_field] = coords;
                $(`#${y_field}_${x_field}`).addClass("sudoku-field-incorrect");
            })
        }
    })
}

// get block start nodes (top left)
// returns: [y_min, x_min]
function get_block_starts(y,x) {
    let starts = [NaN, NaN];
    starts[0] = Math.floor(y / 3) * 3;
    starts[1] = Math.floor(x / 3) * 3;
    return starts;
}

// parse
function parse(input_field) {
    let [y,x] = get_indexes_from_id(input_field);
    // Add new value to value array
    sudoku_values[y][x] = Number.parseInt(input_field.value);
    check_number(y, x);
    return [y, x];
}

// check validation possible
function check_validation_possible() {
    if($(".sudoku-field-incorrect").length > 0) {
        $("#submit-sudoku-btn").prop("disabled", true);  // disable Validate Button
    } else {
        $("#submit-sudoku-btn").prop("disabled", false);  // enable Validate Button
    }
}