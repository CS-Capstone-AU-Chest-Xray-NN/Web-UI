window.onload = function() {
    init();


    function init() {
        document.querySelector('input[type="file"]').addEventListener('change', function() {
          if (this.files && this.files[0]) {
              document.getElementById('upload-form').submit();
            //   var img = document.querySelector('img');  // $('img')[0]
            //   img.src = URL.createObjectURL(this.files[0]); // set src to blob url
              //img.onload = imageIsLoaded;
          }
        });

        load_profiles();
    }

    //function that loads in each profile picture grabbed from the creators github.
    function load_profiles() {
        let one_profile_picture = "url('https://avatars.githubusercontent.com/kennedy15')";
        let two_profile_picture = "url('https://avatars.githubusercontent.com/justicesuh')";
        let three_profile_picture = "url('https://avatars.githubusercontent.com/Drew-Meseck')";

        $('#one').css("background-image", one_profile_picture);
        $('#two').css("background-image", two_profile_picture);
        $('#three').css("background-image", three_profile_picture);

    }
};
