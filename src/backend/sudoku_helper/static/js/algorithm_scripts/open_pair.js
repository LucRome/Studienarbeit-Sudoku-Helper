var y1, x1, y2, x2;

// Step 1
$(document).ready(function() {
    [[y1, x1], [y2, x2]] = dict.fields
    $(`input#${y1}_${x1}`).hide();
    $(`input#${y2}_${x2}`).hide();

    // highlight the corresponding unit
    switch (dict.reason) {
        case 'block': mark_block_affected(y1, x1); break;
        case 'row': mark_row_affected(y1); break;
        case 'column': mark_column_affected(x1); break;
    }
})

// Step 2
function add_candidates() {
    // candidates were removed from other fields
    let array = Object.entries(dict.removed_candidates);
    array.forEach(element => {
        let pos_nr = Number.parseInt(element[0]);
        y = Math.floor(pos_nr / 10);
        x = pos_nr % 10;

        let candidates = element[1];
        candidates.forEach(candidate => {
            get_candidate_field_by_nr(y, x, candidate).children("img").attr("src", get_img_src(candidate, del=false, use=false, lock=false));
        })
    });
}

// Step 3
function mark_candidates() {
    // candidates to lock
    dict.values.forEach(value => {
        get_candidate_field_by_nr(y1, x1, value).children("img").attr("src", get_img_src(value, del=false, use=false, lock=true));
        get_candidate_field_by_nr(y2, x2, value).children("img").attr("src", get_img_src(value, del=false, use=false, lock=true));
    });

    // candidates to delete
    let array = Object.entries(dict.removed_candidates);
    array.forEach(element => {
        let pos_nr = Number.parseInt(element[0]);
        y = Math.floor(pos_nr / 10);
        x = pos_nr % 10;

        let candidates = element[1];
        candidates.forEach(candidate => {
            get_candidate_field_by_nr(y, x, candidate).children("img").attr("src", get_img_src(candidate, del=true, use=false, lock=false));
        })
    });
}

// Step 4
function enter_changes() {
    // remove candidates to delete
    let array = Object.entries(dict.removed_candidates);
    array.forEach(element => {
        let pos_nr = Number.parseInt(element[0]);
        y = Math.floor(pos_nr / 10);
        x = pos_nr % 10;

        let candidates = element[1];
        candidates.forEach(candidate => {
            get_candidate_field_by_nr(y, x, candidate).children("img").attr("src", "");
        })
    })
}