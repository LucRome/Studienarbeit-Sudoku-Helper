var intersect_fields;
var removed_fields;

// Step 1
$(document).ready(function() {
    intersect_fields = dict.intersect_fields;
    removed_fields = parse_fields_from_removed_candidates(dict.removed_candidates);

    // highlight the corresponding units
    let [y, x] = intersect_fields[0];
    mark_block_affected(y, x);
    mark_row_affected(y);
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    // candidates to lock
    mark_candidates_lock([dict.value], intersect_fields);

    // candidates to delete
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);
}

// Step 4
function enter_changes() {
    // remove candidates to delete
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);
    // Highlight fields
    highlight_fields(intersect_fields, "field-locked-candidates");
    highlight_fields(removed_fields, "field-removed-candidate");
}