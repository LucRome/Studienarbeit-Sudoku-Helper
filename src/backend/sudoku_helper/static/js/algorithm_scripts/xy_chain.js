// Step 1
$(document).ready(function() {
    // highlight the corresponding units
    highlight_fields(dict.end_fields, "field-affected");
    highlight_fields([dict.middle_field], "field-locked-candidates-2");
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);

    mark_candidates_lock([dict.value], dict.end_fields);
}

// Step 4
function enter_changes() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);

    highlight_fields(dict.end_fields, "field-locked-candidates");
    let rem_fields = parse_fields_from_removed_candidates(dict.removed_candidates);
    highlight_fields(rem_fields, "field-removed-candidate");
}