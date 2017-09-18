const ENTER = 13;

$(document).ready(function(){
    $('#input_screen').keypress(function(ev){
      console.log(ev.keyCode)
      if(ev.keyCode == ENTER){
        console.info("FIRING")

        command = $("#input_screen").val().replace(/[^a-z0-9 ]/gi,'')
        $("#input_screen").val("") //Clear input



        $("#output_screen").append("<br>")
        $("#output_screen").append(command)

      }
    });
});
