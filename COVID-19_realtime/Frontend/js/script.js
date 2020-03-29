var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    const myObj = JSON.parse(this.responseText);
    
    //World
    document.getElementById("world_cases").innerHTML = (myObj.COVID19.World.COVID19Cases);
    document.getElementById("world_deads").innerHTML = (myObj.COVID19.World.Deaths);
    document.getElementById("world_dead_rate").innerHTML = (myObj.COVID19.World.DeathRate + '%');
    document.getElementById("world_recovered").innerHTML = (myObj.COVID19.World.Recoveries);
    document.getElementById("world_recovered_rate").innerHTML = (myObj.COVID19.World.RecoveredRate + '%');
    
    //Brazil
    document.getElementById("brazil_cases").innerHTML = (myObj.COVID19.Brazil.COVID19Cases);
    document.getElementById("brazil_deads").innerHTML = (myObj.COVID19.Brazil.Deaths);
    document.getElementById("brazil_dead_rate").innerHTML = (myObj.COVID19.Brazil.DeathRate) + '%';
    document.getElementById("brazil_recovered").innerHTML = (myObj.COVID19.Brazil.Recoveries);
    document.getElementById("brazil_recovered_rate").innerHTML = (myObj.COVID19.Brazil.RecoveredRate) + '%';
  }
};
xmlhttp.open("GET", "https://covid19search.herokuapp.com/", true);
xmlhttp.send();


