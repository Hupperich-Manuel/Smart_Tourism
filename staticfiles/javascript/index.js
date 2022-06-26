if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}

// function Check(el) {
//     var button = document.getElementById("submit");

//     var nbr_checked_radios = document.querySelectorAll('input[type=radio]:checked').length;

//     /*
//     var nbr_of_checked_no = document.querySelectorAll('input[type=radio][value="0"]:checked').length;
//         'nbr_of_checked_no>0' : mean if at least one of the 'no' options checked
//         'nbr_checked_radios==0' : mean if no radio button is checked 
//     */
//     if (nbr_checked_radios==16) {
//     button.disabled = false;
//     } else {
//     button.disabled = true;
//     }
// }
function validateForm()                                 
{ 
    var name = document.forms["myForm"];         
    if (name.value == ""){ 
        document.getElementById('answer1').innerHTML="Please dont forget to answer every question ;)";  
        name.focus(); 
        return false; 
    }else{
        document.getElementById('answer1').innerHTML=""; 

    }
}