var uploading_component = `
<div id="uploading_div" style="display:inline-block;">
    <div id="bar-2" class="bar-main-container blue" >
        <div class="wrap">
            <div class="bar-percentage" data-percentage="94" id="progress_bar_percent"></div>
            <div class="bar-container">
                <div class="bar"></div>


            </div>
        </div>
    </div>
    <div>
      <input type="cancel" id="cancel_upload" style="float:left;" class="cancelUpload" />
      <label for="cancel_upload" id="cancel_upload_label" style="float:left;">Cancel</label>
    </div>
`;

var start_upload_component = `
<div id="file_selection_div">
    <input type="file" id="new_file_upload" class="inputfile" />
    <label id="upload_label" for="new_file_upload"><i class="fa fa-cloud-upload"></i> New Upload</label>
</div>

`;


$('#upload_container').on('change', '#new_file_upload', function(evt) {
    var files;
    files = evt.target.files;
    var file_to_upload = files[0];
    var file_name = this.value.split('\\').pop();
    var public_key = $('#public_key_input').val();
    var eva = new Evaporate({
        signerUrl: '/analysis/sign_auth_aws',
        aws_key: public_key,
        aws_url: 'https://s3-us-west-1.amazonaws.com',
        bucket: 'bd2k-proteoseq-dev',

    });





    $('#file_selection_div').replaceWith(uploading_component);

    var progress_bar = $('#progress_bar_percent');

    $('#cancel_upload').on('click',function(event){
          eva.cancel(0);
          $('#uploading_div').replaceWith(start_upload_component);

    });
    eva.add({
        name: 'user-uploads/' + file_name,
        file: file_to_upload,

        complete: function() {
            console.log('complete................yay!');
            $('#uploading_div').replaceWith(start_upload_component);

        },
        progress: function(progress) {
            console.log('making progress: ' + progress);
            var pct = Math.floor(progress*100) + '%';
            progress_bar.text(pct) && progress_bar.siblings().children().css('width',pct);
        }
    });


});



// $('.bar-percentage[data-percentage]').each(function () {
//   var progress = $(this);
//   var percentage = Math.ceil($(this).attr('data-percentage'));
//   $({countNum: 0}).animate({countNum: percentage}, {
//     duration: 2000,
//     easing:'linear',
//     step: function() {
//       // What todo on every count
//       var pct = Math.floor(this.countNum) + '%';
//       // progress.text(pct) && progress.siblings().children().css('width',pct);
//       progress.text(pct);
//
//       progress.siblings().children().css('width','55%');
//     }
//   });
// });
