var fields;

// Step 1
$(document).ready(function() {
    // highlight the corresponding units
    mark_row_affected(dict.fields_row[0][0]);
    mark_column_affected(dict.fields_col[0][1]);
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    fields = [dict.fields_col, dict.fields_row].flat();
    mark_candidates_lock([dict.value], fields);
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);
}

// Step 4
function enter_changes() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);

    highlight_fields(fields, "field-locked-candidates");
    highlight_fields(parse_fields_from_removed_candidates(dict.removed_candidates), "field-removed-candidate")
}