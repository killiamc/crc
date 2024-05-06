
function usuario_cambio(){
    let container = document.getElementsByClassName("panel_cambiousr")[0];
    if(container.style.visibility == 'visible'){
        container.style.visibility ='hidden';
    }else{
        container.style.visibility = 'visible';
    }
}