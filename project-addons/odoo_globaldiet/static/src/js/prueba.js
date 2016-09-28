$(".socialNetwork").append("<div id='fb-root'></div>");
$(".socialNetwork").append('<div class="fb-page" data-href="https://www.facebook.com/globaldiet.es" data-tabs="timeline" data-height="460" data-small-header="false" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true"><blockquote cite="https://www.facebook.com/GrupoNuevaDietetica" class="fb-xfbml-parse-ignore"><a href"https://www.facebook.com/globaldiet.es">Globaldiet</a></blockquote></div>');
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/es_ES/sdk.js#xfbml=1&version=v2.7&appId=1518486771745505";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk')); 


//$("#wrap").append("<div id='news'></div>");

$.ajax({
    url: 'https://globaldiet.es/feed/',
    type: 'GET',
    //crossDomain: true,
    //beforeSend: setHeader,
    dataType: "xml",
    success: function(data) {
    	console.log(data);
	    xmlDoc = $.parseXML( data );
	    $xml = $( data );

	    $title = $xml.find('item').first().find('title').first();
	    $description = $xml.find('item').first().find('description').first();
      $url = $xml.find('item').first().find('link');

	    $(".blog-title").append($title.text());
	    $(".blog-description").append($description.text());
      $(".blog-link").attr("href", $url.text());
    }
});

$('[itemprop="name"]').each(function(){
  var original_text = $(this).text();
  var final_text = $(this).text();
  if($(this).text().length > 20){
   var text =  $(this).text().substring(0,17);
   text = text + "...";
   final_text = text;
  }
  console.log(final_text);
  $(this).text(final_text); 
  $(this).attr("title", original_text);
});


if($('#products_grid_before li.active')){
  var category = $('#products_grid_before li.active').text();
  $('.product-category').text(category);
}


/*
$.urlParam = function(name){
	var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
	return results[1] || 0;
}

console.log($.urlParam('search'));
*/
