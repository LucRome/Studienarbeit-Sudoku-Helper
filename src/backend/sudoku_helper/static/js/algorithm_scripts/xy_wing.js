
// Step 1
$(document).ready(function() {
    // highlight the corresponding units
    let [y_blk, x_blk] = dict.fields[0];
    mark_block_affected(y_blk, x_blk);
    highlight_fields([dict.fields[1], dict.fields[2]], "field-affected")
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);

    mark_candidates_lock(dict.values, dict.fields);
}

// Step 4
function enter_changes() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);

    highlight_fields(dict.fields, "field-locked-candidates");
    let rem_fields = parse_fields_from_removed_candidates(dict.removed_candidates);
    highlight_fields(rem_fields, "field-removed-candidate");
}