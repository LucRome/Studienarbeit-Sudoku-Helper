
$(document).ready(function() {
    coords = dict.field
    $(`input#${coords[0]}_${coords[1]}`).hide();
    $(`td#field_${coords[0]}_${coords[1]}`).append(EMPTY_CANDIDATE_TABLE);
    get_candidate_field_by_nr(coords[0], coords[1], dict.value).children("img").attr("src", get_img_src(dict.value, false, false));
})

function visualise_algorithm(dict) {
    coords = dict.field
    $(`input#${coords[0]}_${coords[1]}`).addClass("field-new-value");
}