function open_add_film_menu() {
    document.getElementById("add-film-form").style.display = "block";
    document.getElementById("add-new-film-button").style.display = "none";
}

function change_actors_list() {
    a = document.getElementsByClassName("actors-list")
    for (let i = 0; i < a.length; i++) {
        val = a[i].innerHTML
        a[i].innerHTML = val.substring(0, val.length - 2);
    }
    document.getElementById("id_year_of_release__gt").placeholder = 'From';
    document.getElementById("id_year_of_release__lt").placeholder = 'To';
}