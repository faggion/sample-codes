$(document).ready(function(){
    //$('#log').text('hellojq');
    $('#unlockform').submit(function(){
        if($("input:first").val() == "abc"){
            $("#lockarea").show(1000);
            $("#unlockarea").hide();

            setTimeout(function(){
                $("#lockarea").hide();
                $("#unlockarea").show();
            }, 10000)
        }
        return false;
    });
});

