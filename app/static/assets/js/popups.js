function characterPopupListener(type) {
    $("."+type+"-name-ref").mouseenter( function() {
        let p = $(this).attr('id').split("-");
        let pk = p[p.length-1];
        let v = "#"+type+"-popup-"+pk;
        if ($(v).children().length == 0) {
            $.get("/api/charactersByID?search="+pk, function(resp) {
            let char = resp[0];
            $(v).append('<img src='+char.image+'>'); 
            });
        }
        $(v).show();
    });
    
    $("."+type+"-name-ref").mouseleave( function() {
        let p = $(this).attr('id').split("-");
        let pk = p[p.length-1];
        let v = "#"+type+"-popup-"+pk;
        $(v).hide();
    });
}

function characterSlugPopupListener() {
    $(".character-slug-ref").mouseenter( function() {
        let p = $(this).attr('id').split("-");
        let pk = p[p.length-1];
        let v = "#slug-popup-"+pk;
        id = $(this).attr('data-charId')
        if ($(v).children().length == 0) {
            console.log("searching");
            $.get("/api/charactersByID?search="+id, function(resp) {
            let char = resp[0];
            $(v).append('<img src='+char.image+'>'); 
            });
        }
        $(v).show();
    });
    
    $(".character-slug-ref").mouseleave( function() {
        let p = $(this).attr('id').split("-");
        let pk = p[p.length-1];
        let v = "#slug-popup-"+pk;
        $(v).hide();
    });
}

function housePopupListener(type) {
    $("."+type+"-name-ref").mouseenter( function() {
        let p = $(this).attr('id').split("-");
        let pk = p[p.length-1];
        let v = "#"+type+"-popup-"+pk;
        if ($(v).children().length == 0) {
            $.get("/api/housesByID?search="+pk, function(resp) {
            let char = resp[0];
            $(v).append('<img src='+char.logoURL+'>'); 
            });
        }
        $(v).show();
    });
    
    $("."+type+"-name-ref").mouseleave( function() {
        let p = $(this).attr('id').split("-");
        let pk = p[p.length-1];
        let v = "#"+type+"-popup-"+pk;
        $(v).hide();
    });
}

characterPopupListener("character");
characterPopupListener("father");
characterPopupListener("mother");
characterPopupListener("sibling");

characterSlugPopupListener();

housePopupListener("house");
