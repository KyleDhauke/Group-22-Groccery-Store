let map;
const overlay = document.getElementById("controls");

function initMap() {
//          var icon1 = {
//                url:"static/icons/landmark.png",
//                size: new google.maps.Size(50,50)
//                origin: new google.maps.Point(0,0),
//                anchor: new google.maps.Point(0,0)
//          }
    getLocation()
    function getLocation(){
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    var loc = {
                        lat: position.coords.latitude,
                        lng: position.coords.longitude,
                    };
                    map.setCenter(loc)
                    loc = {lat: 0, lng: 0};
                    map.setZoom(16);
                }
            );
        }
    }
    var mapProp = {
        center:new google.maps.LatLng(51.475, -3.17),
        zoom:13,
        mapTypeId:google.maps.MapTypeId.ROADMAP
    }
    map=new google.maps.Map(document.getElementById("googleMap"), mapProp);
    const getloc = document.createElement("button");
    getloc.style.backgroundColor = "white";
    getloc.style.borderRadius = "5px";
    getloc.style.width = "50px";
    getloc.style.height = "50px"
    getloc.textContent =  "📍";
    map.controls[google.maps.ControlPosition.RIGHT_CENTER].push(getloc);
    getloc.addEventListener("click", () =>{
        getLocation();
    });

            // var marker = new google.maps.Marker({
            //     position: new google.maps.LatLng(51.4846,-3.1892),
            //     map: map,
            //     title: "Hello World!",
            // });
            // var marker = new google.maps.Marker({
            //     position: new google.maps.LatLng(51.4546,-3.1892),
            //     map: map,
            //     title: "Hello World!",
            // });

    map.addListener("dblclick", (e) => {
        placemarker(e, map);
    });
    function placemarker(e){
        let marker = new google.maps.Marker({
            position: {
                lat: e.latLng.lat(),
                lng: e.latLng.lng()
            },
            map: map,
            title: "Check",
//            icon: icon1
//            icon: "static/icons/landmark.png"
        });
        // const info = document.createElement("div");
        // overlay.appendChild(info);
        var lnd_title = window.prompt("What Would You Like To Title This Landmark?");
        var description = window.prompt("What Description would you like to give?");
        var tags = window.prompt("What Tags Would You Like? (separate the tags with a comma)");
        var trial =  '<div id="content">' +
                         '<div id="siteNotice">' +
                         "</div>" +
                         '<h1 id="firstHeading" class="firstHeading">'+lnd_title+'</h1>' +
                         '<div id="bodyContent">' +
                         "<p>"+description+"</p>" +
                         "<p><b>Tags: </b>"+tags+"</p>" + 
                        //  '<button type="button">Add to List</button>'+
                         "</div>" +
                      "</div>";

        const infoWindow = new google.maps.InfoWindow({
            content:  trial,
        });
        //addmarker_to_db(lnd_title,description,tags);
        marker.addListener("click",()=>{
        // window.alert("Thats a marker!");
            setTimeout(markerClick(marker, infoWindow), 6000);
        });
        marker.addListener("dblclick",()=>{
        // window.alert("Thats a marker!");
            marker.setMap(null);
        });
    };
    function markerClick(e, info){
    //window.alert(marker);
       map.setCenter(e.getPosition());
       info.open(map, e);
    }

}
google.maps.event.addDomListener(window, 'load', initMap);

function addmarker_to_db(lnd_title,description,tags){
    var mysql = require('mysql');
    var connection = mysql.createConnection({
        host: 'csmysql.cs.cf.ac.uk',
        user: 'c1932063',
        password: 'Team22project',
        database: 'c1932063_Team22Year2',
    })
    connection.connect();

//    var addSql = 'INSERT INTO landmark(name,description,tags) VALUES('lnd_title','description','tags')';
    var addSql = 'INSERT INTO landmark(name,description,tags) VALUES('+lnd_title.toString()+','+description.toString()+','+tags.toString()+')';
    connection.query(addSql,function (err, result) {
        if(err){
         console.log('[INSERT ERROR] - ',err.message);
         return;
        }

       console.log('--------------------------INSERT----------------------------');
       //console.log('INSERT ID:',result.insertId);
       console.log(result);
       console.log('-----------------------------------------------------------------\n\n');
    });
}