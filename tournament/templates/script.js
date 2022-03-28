//ссылка на базу дынных
//list.open(method='get','../../db.sqlite3');
//list.responseType = 'json';
//иммитируем получение

var list = {
    "Tournament":[
	{"name":"Турнир 1", "id":"0","status":"Завершён","date":"20.03.22"},
	{"name":"Турнир 2", "id":"1","status":"Завершён","date":"20.03.22"},
	{"name":"Турнир 3", "id":"2","status":"Завершён","date":"20.03.22"},
	{"name":"Турнир 4", "id":"4","status":"Не Завершён","date":"20.03.22"},
	{"name":"Турнир 5", "id":"6","status":"Не Завершён,","date":"20.03.22"}]
};
  x = list.Tournament[0];
 for (i in list.Tournament) {
    x = list.Tournament[i].name;
	document.getElementById('tournament_list').innerHTML += x.link(list.Tournament[i].id) +"<br/>" ;
 };
 //list.send();