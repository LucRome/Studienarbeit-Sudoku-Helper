var fields;

// Step 1
$(document).ready(function() {
    fields = parse_fields_from_removed_candidates(dict.removed_candidates);

    // highlight the corresponding unit
    switch (dict.reason) {
        case 'block': mark_block_affected(y, x); break;
        case 'row': mark_row_affected(y); break;
        case 'column': mark_column_affected(x); break;
    }
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    // candidates to lock
    mark_candidates_lock(dict.values, fields);

    // candidates to delete
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);
}

// Step 4
function enter_changes() {
    // remove candidates to delete
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);
    
    // Highlight fields
    highlight_fields(fields, "field-locked-and-removed-candidates");
}