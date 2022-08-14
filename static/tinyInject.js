var script = document.createElement("script");
script.type = "text/javascript";
script.src =
  "https://cdn.tiny.cloud/1/w2r64a0ykku5ugs83jb9prkd40y547zqqbiik1jmwpf7s44sy/tinymce/6/tinymce.min.js";
document.head.appendChild(script);

script.onload = function () {
  tinymce.init({
    selector: "#id_content",
    height: '680',
    plugins: "advlist lists",
    plugins:
      "preview lists advlist image autolink link lists charmap print preview hr anchor pagebreak searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking table emoticons template paste help",
    toolbar:
      "preview bullist image undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | " +
      "bullist numlist outdent indent | link image | print preview media fullpage | " +
      "forecolor backcolor emoticons | help",
    menu: {
      favs: {
        title: "My Favorites",
        items: "code visualaid | searchreplace | emoticons",
      },
    },
    advlist_bullet_styles: "square",
    content_css: "css/content.css",
  });
};
