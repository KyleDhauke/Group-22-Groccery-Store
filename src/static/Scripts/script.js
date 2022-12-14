var map;
function initMap() {
//          var icon1 = {
//                url:"static/icons/landmark.png",
//                size: new google.maps.Size(50,50)
//                origin: new google.maps.Point(0,0),
//                anchor: new google.maps.Point(0,0)
//          }
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
    getLocation();
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

        });
        var lnd_title = window.prompt("What Would You Like To Title This Landmark?");
        var description = window.prompt("What Description would you like to give?");
        var tags = window.prompt("What Tags Would You Like? (separate the tags with a comma)");
        var lat = e.latLng.lat()
        var lng = e.latLng.lng()
        form = document.forms["info"];
        form.elements["name"].value = lnd_title;
        form.elements["description"].value = description;
        form.elements["tags"].value = tags;
        form.elements["lat"].value = lat;
        form.elements["lng"].value = lng;
        form.submit();
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
        marker.addListener("click",()=>{
            setTimeout(markerClick(marker, infoWindow), 600);
        });
        marker.addListener("dblclick",()=>{
            marker.setMap(null);
        });
    };
    function markerClick(e, info){
       map.setCenter(e.getPosition());
       info.open(map, e);
    };
    
    function loadMarkers(){
        var nice = "";
        let marker;
        marker = new google.maps.Marker({
            position: {
                lat: parseFloat(latt),
                lng: parseFloat(lngg),
            },
            map: map,
            title: ":)",
        }),

        nice = '<div id="content">' +
            '<div id="siteNotice">' +
            "</div>" +
            '<h1 id="firstHeading" class="firstHeading">'+String(n)+'</h1>' +
            '<div id="bodyContent">' +
            "<p>"+String(d)+"</p>" +
            "<p><b>Tags: </b>"+String(t)+"</p>" + 
            //  '<button type="button">Add to List</button>'+
            "</div>" +
            "</div>";
        
            const Iw = new google.maps.InfoWindow({
            content: nice,
            });
        marker.addListener("click",()=>{
            setTimeout(markerClick(marker, Iw), 600);
        });
        marker.addListener("dblclick",()=>{
            marker.setMap(null);
        });
    
    }
    loadMarkers();
    
}
google.maps.event.addDomListener(window, 'load', initMap);
