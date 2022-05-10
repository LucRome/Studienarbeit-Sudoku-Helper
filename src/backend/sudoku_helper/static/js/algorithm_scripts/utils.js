// A empty candidate Table
const EMPTY_CANDIDATE_TABLE = 
    `<table class="candidate-table">
        <tr class="p-0">
            <td class="candidate-field">
                <img nr="1" src="" />
            </td>
            <td class="candidate-field">
                <img nr="2" src="" />
            </td>
            <td class="candidate-field">
                <img nr="3" src="" />
            </td>
        </tr>
        <tr class="p-0">
            <td class="candidate-field">
                <img nr="4" src="" />
            </td>
            <td class="candidate-field">
                <img nr="5" src="" />
            </td>
            <td class="candidate-field">
                <img nr="6" src="" />
            </td>
        </tr>
        <tr class="p-0">
            <td class="candidate-field">
                <img nr="7" src="" />
            </td>
            <td class="candidate-field">
                <img nr="8" src="" />
            </td>
            <td class="candidate-field">
                <img nr="9" src="" />
            </td>
        </tr>
    </table>`

function get_candidate_field_by_nr(row, col, nr) {
    let nr_str = nr.toString();
    let candidate_fields = $(`#field_${row}_${col} .candidate-field`);
    return candidate_fields.filter(
        // filter the candidate fields by the attribute number of the <img>
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