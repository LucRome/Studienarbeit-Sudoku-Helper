
// Step 1
$(document).ready(function() {
   // highlight the corresponding units
   dict.fields.forEach(field => {
       let [y, x] = field;
       mark_block_affected(y, x);
   });
})

// Step 2
function add_candidates() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=false);
}

// Step 3
function mark_candidates() {
    mark_candidates_lock(dict.values, dict.fields);
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=true, remove=false);
}

// Step 4
function enter_changes() {
   handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);

   highlight_fields(dict.fields, "field-locked-candidates");
   let rm_fields = parse_fields_from_removed_candidates(dict.removed_candidates);
   reverse_highlight_fields(rm_fields, "field-locked-candidates");
   highlight_fields(rm_fields, "field-removed-candidate");
}