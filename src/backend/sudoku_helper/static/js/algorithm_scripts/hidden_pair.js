var y1, x1, y2, x2;

// Step 1
$(document).ready(function() {
    let fields_str = Object.keys(dict.removed_candidates);
    let [f1,f2] = [Number.parseInt(fields_str[0]), Number.parseInt(fields_str[1])];
    [y1, x1] = [Math.floor(f1 / 10), f1%10];
    [y2, x2] = [Math.floor(f2 / 10), f2%10];

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
        let y = Math.floor(pos_nr / 10);
        let x = pos_nr % 10;

        let candidates = element[1];
        candidates.forEach(candidate => {
            get_candidate_field_by_nr(y, x, candidate).children("img").attr("src", "");
        })
    })

    // Highlight fields
    $(`#field_${y1}_${x1}`).addClass("field-locked-and-removed-candidates");
    $(`#field_${y2}_${x2}`).addClass("field-locked-and-removed-candidates");
}