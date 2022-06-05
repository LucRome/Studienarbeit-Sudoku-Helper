
// Step 1
$(document).ready(function() {
   // highlight the corresponding units
   mark_row_affected(dict.row);
   mark_row_affected(dict.fields[0][0]);
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);

    mark_candidates_lock([dict.value], dict.fields);
    mark_candidates_lock([dict.value], dict.path_complex);
}

// Step 4
function enter_changes() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);

    highlight_fields(dict.fields, "field-locked-candidates");
    highlight_fields(dict.path_complex, "field-locked-candidates");
    highlight_fields(parse_fields_from_removed_candidates(dict.removed_candidates), "field-removed-candidate");
}