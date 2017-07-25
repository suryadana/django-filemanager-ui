(function() {
  var editor_config;

  editor_config = {
    path_absolute: '',
    height: "480",
    theme: 'modern',
    plugins: ['advlist autolink lists link image charmap print preview hr anchor pagebreak', 'searchreplace wordcount visualblocks visualchars code fullscreen', 'insertdatetime media nonbreaking save table contextmenu directionality', 'emoticons template paste textcolor colorpicker textpattern imagetools codesample toc help'],
    toolbar: 'undo redo | insert | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image preview',
    toolbar1: 'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
    toolbar2: 'print preview media | forecolor backcolor emoticons',
    image_advtab: true,
    image_class_list: [
      {
        title: 'Image Responsive',
        value: 'img-responsive'
      }
    ],
    file_browser_callback: function(field_name, url, type, win) {
      var cmsURL, d, e, g, w, x, y;
      w = window;
      d = document;
      e = d.documentElement;
      g = d.getElementsByTagName('body')[0];
      x = w.innerWidth || e.clientWidth || g.clientWidth;
      y = w.innerHeight || e.clientHeight || g.clientHeight;
      cmsURL = editor_config.path_absolute + '?field_name=' + field_name + '&lang=' + tinymce.settings.language;
      tinyMCE.activeEditor.windowManager.open({
        file: cmsURL,
        title: 'Filemanager',
        width: x * 0.8,
        height: y * 0.8,
        resizable: 'yes',
        close_previous: 'no'
      });
    }
  };

  editor_config.selector = 'textarea';

  editor_config.path_absolute = "/filemanager/connector";

  tinymce.init(editor_config);

}).call(this);
