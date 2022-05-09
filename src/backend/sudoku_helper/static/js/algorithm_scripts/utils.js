// A empty candidate Table
EMPTY_CANDIDATE_TABLE = 
    `<table class="candidate-table">
        <tr class="p-0">
            <td class="candidate-field">
                <img nr="1" src="${img_folder}/white.svg" />
            </td>
            <td class="candidate-field">
                <img nr="2" src="${img_folder}/white.svg" />
            </td>
            <td class="candidate-field">
                <img nr="3" src="${img_folder}/white.svg" />
            </td>
        </tr>
        <tr class="p-0">
            <td class="candidate-field">
                <img nr="4" src="${img_folder}/white.svg" />
            </td>
            <td class="candidate-field">
                <img nr="5" src="${img_folder}/white.svg" />
            </td>
            <td class="candidate-field">
                <img nr="6" src="${img_folder}/white.svg" />
            </td>
        </tr>
        <tr class="p-0">
            <td class="candidate-field">
                <img nr="7" src="${img_folder}/white.svg" />
            </td>
            <td class="candidate-field">
                <img nr="8" src="${img_folder}/white.svg" />
            </td>
            <td class="candidate-field">
                <img nr="9" src="${img_folder}/white.svg" />
            </td>
        </tr>
    </table>`

function get_candidate_field_by_nr(row, col, nr) {
    nr_str = nr.toString();
    candidate_fields = $(`#field_${row}_${col} .candidate-field`);
    return candidate_fields.filter(
        function(index) {return $(this).children("img").attr("nr") === nr_str; }
    )
}

function get_img_src(nr, del, use) {
    if (del) {
        return `${img_folder}/candidates_marked_delete/${nr}.svg`;
    } else if (use) {
        return `${img_folder}/candidates_marked_use/${nr}.svg`;
    } else {
        return `${img_folder}/candidates/${nr}.svg`
    }
}