// Step 1
$(document).ready(function() {
    let [y,x] = dict.fields[0];

    // highlight the corresponding unit
    switch (dict.reason) {
        case 'block': mark_block_affected(y, x); break;
        case 'row': mark_row_affected(y); break;
        case 'column': mark_column_affected(x); break;
    }
})

// Step 2
function add_candidates() {
    // candidates that were removed from other fields
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    // candidates to lock
    mark_candidates_lock(dict.values, dict.fields);

    // candidates to delete
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);
}

// Step 4
function enter_changes() {
    // remove candidates to delete and mark fields
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);
    let rm_fields = parse_fields_from_removed_candidates(dict.removed_candidates);
    highlight_fields(rm_fields, "field-removed-candidate")

    // Mark fields where candidates are locked
    highlight_fields(dict.fields, "field-locked-candidates");
}