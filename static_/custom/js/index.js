
window.onload = () => {
  $("#send").click(() => {

    link = $("#link");
    input = $("#imageinput")[0];
    model = $("#type option:selected").val();
    model_use = $("#type option:selected").text();
    console.log(model_use);
    if (input.files && input.files[0]) {
      let formData = new FormData();
      formData.append("file", input.files[0]);
      formData.append("model", model);
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
          $("#download").attr('target', '_blank');
          $("#download").attr("href", +data);
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




