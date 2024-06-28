$(document).ready(function(){

    var fEmail =  /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    $("#form").submit(function(event) {
        event.preventDefault();
    });

    $("#btn-enviar").click(function(){

        var flag = false;
        var email = $("#email").val();

        if ($("#nombre").val() == ""){
            $("#eNombre").fadeIn();
            flag = true;
        }else{
            $("#eNombre").fadeOut();
        }

        if (!fEmail.test(email)){
            $("#eEmail").fadeIn();
            flag = true;
        }else{
            $("#eEmail").fadeOut();
        }

        if ($("#asunto").val() == ""){
            $("#eAsunto").fadeIn();
            flag = true;
        }else{
            $("#eAsunto").fadeOut();
        }

        if ($("#mensaje").val() == ""){
            $("#eMensaje").fadeIn();
            flag = true;
        }else{
            $("#eMensaje").fadeOut();
        }

        if (!flag){
            $("#cont_modal").fadeIn();

            $("#nombre").val("");
            $("#email").val("");
            $("#asunto").val("");
            $("#mensaje").val("");
        }

        return !flag;

    });

    $("#mod_close").click(function(){
        $("#cont_modal").fadeOut();
    })

});
