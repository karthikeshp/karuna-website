$(document).ready(function() {
    var i = 0;
    $(".marqueeElement").each(function() {
          var $this = $(this);
          $this.css("top", i);
          i += 50;
          doScroll($this);
    });
    $('#mholder').mouseenter(function(){
        $(this).addClass('pause')
    }).mouseleave(function(){
        $(this).removeClass('pause')

    });
});
function doScroll(e) {
    var top = parseInt(e.css("top"));
    if(top < -50) {
        top = 150;
        e.css("top", top);
    }
    if(!$('#mholder').hasClass('pause')) {
        var new_top = parseInt(top) - 50
    }else{
        var new_top = parseInt(top)
    }
    e.animate({
            top: new_top
        }, 1000, 'linear',
        function() {
            doScroll($(this))
    });
}
