var fields_rem;

// Step 1
$(document).ready(function() {
    fields_rem = parse_fields_from_removed_candidates(dict.removed_candidates);

    // highlight the corresponding units
    dict.fields_not_removed.forEach(coords => {
        mark_row_affected(coords[0]);
    })
    fields_rem.forEach(coords => {
        mark_row_affected(coords[0]);
    })
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    mark_candidates_lock([dict.value_removed, dict.value_2nd], dict.fields_not_removed);
    mark_candidates_lock([dict.value_2nd], fields_rem);
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);
}

// Step 4
function enter_changes() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);
    highlight_fields(dict.fields_not_removed, "field-locked-candidates");
    highlight_fields(fields_rem, "field-locked-and-removed-candidates");
}