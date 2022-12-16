
  window.onload = () =>  {
  $("#send").click(() => {

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
        error: function (data) {
          console.log("upload error", data);
          console.log(data.getAllResponseHeaders());
        },
        success: function (data) {

          $(link).css("visibility", "visible");
          $("#download").attr('target','_blank');
          $("#download").attr("href", "static/output/" + data);
          console.log(data);
          console.log('Success!');
        },
      });
    }
  });

};

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

