function visualise_algorithm(dict) {
    coords = dict.field
    $(`input#${coords[0]}_${coords[1]}`).addClass("field-new-value");
}