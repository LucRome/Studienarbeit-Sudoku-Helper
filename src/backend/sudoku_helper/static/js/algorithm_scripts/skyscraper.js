var x_1, x_2
var fields

// Step 1
$(document).ready(function() {
    [x_1, x_2] = [dict.fields_staggered[0][1], dict.fields_staggered[1][1]]

    // highlight the corresponding units
    mark_row_affected(dict.row_same_height)
    mark_column_affected(x_1)
    mark_column_affected(x_2)
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    fields = [dict.fields_staggered[0], dict.fields_staggered[1], [dict.row_same_height, x_1], [dict.row_same_height, x_2]];
    mark_candidates_lock([dict.value], fields);
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);
}

// Step 4
function enter_changes() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);

    // mark fields
    highlight_fields(fields, "field-locked-candidates");
    let rm_fields = parse_fields_from_removed_candidates(dict.removed_candidates);
    highlight_fields(rm_fields, "field-removed-candidate")
}