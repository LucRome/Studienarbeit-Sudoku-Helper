// A empty candidate Table
const EMPTY_CANDIDATE_TABLE = 
    `<table class="candidate-table">
        <tr class="p-0">
            <td class="candidate-field">
                <img nr="1" src="" />
            </td>
            <td class="candidate-field">
                <img nr="2" src="" />
            </td>
            <td class="candidate-field">
                <img nr="3" src="" />
            </td>
        </tr>
        <tr class="p-0">
            <td class="candidate-field">
                <img nr="4" src="" />
            </td>
            <td class="candidate-field">
                <img nr="5" src="" />
            </td>
            <td class="candidate-field">
                <img nr="6" src="" />
            </td>
        </tr>
        <tr class="p-0">
            <td class="candidate-field">
                <img nr="7" src="" />
            </td>
            <td class="candidate-field">
                <img nr="8" src="" />
            </td>
            <td class="candidate-field">
                <img nr="9" src="" />
            </td>
        </tr>
    </table>`

function get_candidate_field_by_nr(row, col, nr) {
    let nr_str = nr.toString();
    let candidate_fields = $(`#field_${row}_${col} .candidate-field`);
    return candidate_fields.filter(
        // filter the candidate fields by the attribute number of the <img>
        function(index) {return $(this).children("img").attr("nr") === nr_str; }
    )
}

function get_img_src(nr, del=false, use=false, lock=false) {
    if (del) {
        return `${img_folder}/candidates_marked_delete/${nr}.svg`;
    } else if (use) {
        return `${img_folder}/candidates_marked_use/${nr}.svg`;
    } else if (lock){
        return `${img_folder}/candidates_marked_lock/${nr}.svg`
    }else{
        return `${img_folder}/candidates/${nr}.svg`;
    }
}

function mark_row_affected(row_nr) {
    for (let i = 0; i < 10; i++) {
        $(`#field_${row_nr}_${i}`).addClass("field-affected");
    }
}

function mark_column_affected(col_nr) {
    for (let i = 0; i < 10; i++) {
        $(`#field_${i}_${col_nr}`).addClass("field-affected");
    }
}

function mark_block_affected(y_field, x_field) {
    y_start = Math.floor(y_field / 3) * 3;
    x_start = Math.floor(x_field / 3) * 3;
    for (let y = y_start; y < (y_start + 3); y++) {
        for (let x = x_start; x < (x_start + 3); x++) {
            $(`#field_${y}_${x}`).addClass("field-affected");
        }
    }
}