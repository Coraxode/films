function open_add_film_menu() {
    document.getElementById("add-film-form").style.display = "block";
    document.getElementById("add-new-film-button").style.display = "none";
}

function prepare_document() {
    a = document.getElementsByClassName("actors-list")
    for (let i = 0; i < a.length; i++) {
        val = a[i].innerHTML
        a[i].innerHTML = val.substring(0, val.length - 2);
    }
    document.getElementById("id_year_of_release__gt").placeholder = 'From';
    document.getElementById("id_year_of_release__lt").placeholder = 'To';
}

function change_page(page) {
    const url = new URL(window.location.href);
    url.searchParams.delete('page');
    url.searchParams.set('page', page);
    return window.location.href = url.href;
}

function activate_add_form() {
    let form_style = document.getElementById("add_form").style;
    let form_change_style = document.getElementById("id_add_director_actor_form").style;
    form_style.display = (form_style.display === 'none' || form_style.display === '') ? 'flex' : 'none';
    form_change_style.display = 'none';
}

function activate_change_form(id, year, director) {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
    });
    let form_style = document.getElementById("add_form").style;
    let form_change_style = document.getElementById("id_add_director_actor_form").style;
    form_style.display = 'flex';
    form_change_style.display = 'block';

    let a = document.getElementById("id_a_change_film");
    let name = document.getElementById("id_film_" + id + "_name").value;
    let actors = document.getElementById("id_film_" + id + "_actors").innerHTML;
    let film_name = document.getElementById("id_change_film_name");
    let film_year = document.getElementById("id_change_film_year");
    let film_director = document.getElementById("id_change_film_director");
    let film_actors = document.getElementById("id_change_film_actors");
    let film_id = document.getElementById("id_change_film_id");
    a.innerHTML = 'Change film \"' + name + '\"' 
    film_name.value = name;
    film_year.value = year;
    film_director.value = director;
    film_actors.value = actors.split(":")[1].trim();
    film_id.value = id
}
