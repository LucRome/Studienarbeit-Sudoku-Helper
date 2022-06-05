
// Step 1
$(document).ready(function() {
   // highlight the corresponding units
   dict.fields.forEach(coords => {
       let [y, x] = coords;
       mark_block_affected(y, x);
   });
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    mark_candidates_lock(dict.values_locked, dict.fields);
    mark_candidates_lock([dict.value_removed], dict.fields_cricled_candidates);
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);
}

// Step 4
function enter_changes() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);

    highlight_fields(dict.fields, "field-locked-candidates")
    let rem = parse_fields_from_removed_candidates(dict.removed_candidates)
    highlight_fields(rem, "field-removed-candidate")
}