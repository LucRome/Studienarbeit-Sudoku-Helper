var intersect_fields;
var removed_fields;

var row1, row2, col1, col2;

// Step 1
$(document).ready(function() {
    intersect_fields = dict.intersect_fields;
    removed_fields = parse_fields_from_removed_candidates(dict.removed_candidates);

    // get the rows and cols that contribute to the x-wing
    [row1, col1] = intersect_fields[0];
    for (let i = 1; i < intersect_fields.length; i++) {
        let [row, col] = intersect_fields[i];
        if (row != row1) { row2 = row; }
        if (col != col1) { col2 = col; }
    }

    // highlight the corresponding units
    mark_row_affected(row1);
    mark_row_affected(row2);
    mark_column_affected(col1);
    mark_column_affected(col2);
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