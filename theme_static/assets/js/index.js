
  window.onload = () =>  {
  $("#send").click(() => {
    var spinner ='<div class="spinner-border text-light" role="status"><span class="visually-hidden"></span></div> Generating'
    var button_send = $("#send");
    $("#send").prop('disable',true);
    button_send.html(spinner);
    link = $("#link");
    input = $("#imageinput")[0];
     model = $( "#type option:selected" ).val();
     model_use = $( "#type option:selected" ).text();
      console.log(model_use);
    if (input.files && input.files[0]) {
      let formData = new FormData();
      formData.append("file", input.files[0]);
      formData.append("model",model);
      $.ajax({
        url: '/detect', //point to server side location
        type: 'POST', // what to expect from server
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        beforeSend: function(){
        // Show loading
        $(spinner).show();
        },
        error: function (data) {
          console.log("upload error", data);
          console.log(data.getAllResponseHeaders());
        },
        success: function (data) {

          $(button_send).text("GENERATED");
          $(button_send).prop('disabled',true);
          $(link).css("visibility", "visible");
          console.log('Success! ' + data);
         
          
        },
        complete: function(){
          $(spinner).hide();
          //alert(data);
          //location.reload();
       }
      });
    }
  });

};


var form = document.forms.namedItem("formData");
form.addEventListener('submit', function (ev) {
    var oData = new FormData(form);
    oData.append('image_db', $('#image')[0].files[0])
    for (var p of oData) {
        console.log(p); // <- logs image in oData correctly
    }
    $.ajax({
        url: '/upload_DB',
        type: 'POST',
        data: oData,
        cache: false,
        contentType: false,
        enc-type: 'multipart/form-data',
        processData: false,
        error: function (data) {
          console.log("upload error", data);
          console.log(data.getAllResponseHeaders());
        },
        success: function (data) {
          console.log(data);

        },
    });
    ev.preventDefault();
}, false);




function disabledTab(){

  console.log("Tab disable.com");
  $('.nav-link li').not('.active').addClass('disabled');
  $('.nav-link li').not('.active').find('a').removeAttr("data-bs-toggle");
}

function readUrl(input) {

  console.log("evoked readUrl");
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.unload = function (e) {
      console.log(e.target);

    };
    reader.readAsDataURL(input.files[0]);
  }
}

/*
    function disabled(){
 $('.nav li').not('.active').addClass('disabled');
      $('.nav li').not('.active').find('a').removeAttr("data-toggle");
}


  $(document).ready(function() {

    var flag;
    //disable non active tabs

        $('#detect').click(function(){

        flag = 0;

    });

       $('#send').click(function(){
         flag = 2;

        //enable next tab
        //$('.nav li.active').next('li').removeClass('disabled');
        //$('.nav li.active').next('li').find('a').attr("data-toggle","tab")
    });

    if(flag == 0){


    }
    else if(flag == 2){
     $('.nav li').not('.active').addClass('disabled');
      $('.nav li').not('.active').find('a').removeAttr("data-toggle");

    }

});

*/

