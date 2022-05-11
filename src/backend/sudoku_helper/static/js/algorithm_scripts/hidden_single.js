var y, x;

// Step 1
$(document).ready(function() {
    [y, x] = dict.field
    $(`input#${y}_${x}`).hide();

    // highlight the corresponding unit
    switch (dict.reason) {
        case 'block': mark_block_affected(y, x); break;
        case 'row': mark_row_affected(y); break;
        case 'column': mark_column_affected(x); break;
    }
})

// Step 2
function add_candidates() {
    $(`td#field_${y}_${x}`).append(EMPTY_CANDIDATE_TABLE);
    resize_all();
    get_candidate_field_by_nr(y, x, dict.value).children("img").attr("src", get_img_src(dict.value, del=false, use=false, lock=false));
}

// Step 3
function mark_candidates() {
    get_candidate_field_by_nr(y, x, dict.value).children("img").attr("src", get_img_src(dict.value, del=false, use=true, lock=false));
}

// Step 4
function enter_changes() {
    $(`#field_${y}_${x} .candidate-table`).hide();
    $(`#${y}_${x}`).show().addClass("field-new-value");
}