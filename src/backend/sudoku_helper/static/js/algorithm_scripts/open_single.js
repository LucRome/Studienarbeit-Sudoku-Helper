var y,x;

// Step 1
$(document).ready(function() {
    [y, x] = dict.field
    $(`input#${y}_${x}`).hide();

    // highlight the corresponding row
    for (i = 0; i < 10; i++) {
        $(`#field_${y}_${i}`).addClass("field-affected");
    }
})

// Step 2
function add_candidates() {
    $(`td#field_${y}_${x}`).append(EMPTY_CANDIDATE_TABLE);
    get_candidate_field_by_nr(y, x, dict.value).children("img").attr("src", get_img_src(dict.value, del=false, use=false));
}

// Step 3
function mark_candidates() {
    get_candidate_field_by_nr(y, x, dict.value).children("img").attr("src", get_img_src(dict.value, del=false, use=true));
}

// Step 4
function enter_changes() {
    $(`#field_${y}_${x} .candidate-table`).hide();
    $(`#${y}_${x}`).show();
}