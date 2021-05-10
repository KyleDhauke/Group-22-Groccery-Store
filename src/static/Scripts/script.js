let map;

function initMap() {
          if(navigator.geolocation){
              navigator.geolocation.getCurrentPosition(
                (position) => {
                  var loc = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                  };
                  map.setCenter(loc);
                  loc = {lat: 0, lng: 0};
                  map.setZoom(16);
                }
              );
          }
            var mapProp = {
                center:new google.maps.LatLng(51.475, -3.17),
                zoom:13,
                mapTypeId:google.maps.MapTypeId.ROADMAP
                }
            map=new google.maps.Map(document.getElementById("googleMap"), mapProp);

            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(51.4846,-3.1892),
                map: map,
                title: "Hello World!",
            });
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
                icon: "static/icons/landmark.png"
                
              });
              const infoWindow = new google.maps.InfoWindow({
                content: "<p>Relaxing Spot to read my favourite book!</p>",
              });
              marker.addListener("click",()=>{
               // window.alert("Thats a marker!");
                markerClick(marker, infoWindow);
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