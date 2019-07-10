    x = navigator.geolocation;
    x.getCurrentPosition(sendPosition);
    function sendPosition(position){
        var myLat = position.coords.latitude;
        var myLong = position.coords.longitude;
        $.ajax({
            type : "POST",
            url : "/weather", 
            data : {latitude: myLat, longitude: myLong},
            success: function (res) { console.log(res) }, 
            error: function (error) { console.log(error) }
        });
    }