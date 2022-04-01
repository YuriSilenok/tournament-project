list =  new XMLHttpRequest();
//ссылка на базу дынных
list.open(method='get','../tournament-project.sqlite3');
list.responseType = 'json';

 x = list.Tournament[0];
 for (i in list.Tournament) {
    x = list.Tournament[i].name;
	document.getElementById('tournament_list').innerHTML += x.link(list.Tournament[i].id) +"<br/>" ;
 };