$(document).ready(function(){
    $("#image").css("display","none");
    $("#analyze").css("display","none");
})

function readURL(input) {
    if (input.files && input.files[0]) {
        $("#image").css("display","block");
        $("#analyze").css("display","block");
        
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#image')
                .attr('src', e.target.result)
                .width(300)
                .height(300);
        };

        reader.readAsDataURL(input.files[0]);
    }
}
var click = false;
function clicked(){
    if(click == false){
        document.getElementById("demo").innerHTML = "Hello World";
        click = true;
    }
    else{
        click = false;
        document.getElementById("demo").innerHTML = "bye World";
    }
}
