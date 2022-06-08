
// Step 1
$(document).ready(function() {
    // highlight the corresponding units (all blocks which contain >= 1 affected field)
    dict.fields.forEach(lst => {
        lst.forEach(coords => {
            let [y,x] = coords;
            mark_block_affected(y, x);
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

    dict.fields.forEach(lst => {
        mark_candidates_lock([dict.value], lst);
    })
}

// Step 4
function enter_changes() {
    handle_removed_candidates(dict.removed_candidates, marked_to_delete=false, remove=true);

    highlight_fields(dict.fields[0], "field-locked-candidates");
    highlight_fields(dict.fields[1], "field-locked-candidates-2");
    let rem_fields = parse_fields_from_removed_candidates(dict.removed_candidates);
    highlight_fields(rem_fields, "field-removed-candidate");
}