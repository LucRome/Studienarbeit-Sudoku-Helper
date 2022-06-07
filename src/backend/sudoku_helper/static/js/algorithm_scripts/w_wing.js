
// Step 1
$(document).ready(function() {
    // highlight the corresponding units
    [dict.fields_1, dict.fields_2].forEach(fields => {
        fields.forEach(coords => {
            mark_row_affected(coords[0]);
        })
    })
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);

    mark_candidates_lock(dict.values_locked, dict.fields_1);
    mark_candidates_lock(dict.values_locked, dict.fields_2);
}

// Step 4
function enter_changes() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);

    highlight_fields(dict.fields_1, "field-locked-candidates");
    highlight_fields(dict.fields_2, "field-locked-candidates");
    let rem_candidates = parse_fields_from_removed_candidates(dict.removed_candidates);
    highlight_fields(rem_candidates, "field-removed-candidate");
}