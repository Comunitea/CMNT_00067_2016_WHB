/////////////////////////////////////
// Red Social Facebook             //
/////////////////////////////////////

$(".socialNetwork").empty();
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

/////////////////////////////////////
// Cargar Ultima Noticia           //
/////////////////////////////////////

$.ajax({
    url: 'https://globaldiet.es/feed/',
    type: 'GET',
    //crossDomain: true,
    //beforeSend: setHeader,
    dataType: "xml",
    success: function(data) {
      //console.log(data);
      xmlDoc = $.parseXML( data );
      $xml = $( data );

      $title = $xml.find('item').first().find('title').first();
      $description = $xml.find('item').first().find('description').first();
      $url = $xml.find('item').first().find('link');

      $(".blog-title").empty();
      $(".blog-description").empty();

      $(".blog-title").append($title.text());
      $(".blog-description").append($description.text());
      $(".blog-link").attr("href", $url.text());
    }
});

/////////////////////////////////////
// Reducir Tamaño Titulo producto  //
/////////////////////////////////////

$('[itemprop="name"]').each(function(){
  var original_text = $(this).text();
  var final_text = $(this).text();
  if($(this).text().length > 28){
   var text =  $(this).text().substring(0,25);
   text = text + "...";
   final_text = text;
  }
  //console.log(final_text);
  $(this).text(final_text); 
  $(this).attr("title", original_text);
});

$('.oe_subdescription [itemprop="short_summary"]').each(function(){
  var original_text = $(this).text();
  var final_text = $(this).text();
  if($(this).text().length > 75){
   var text =  $(this).text().substring(0,72);
   text = text + "...";
   final_text = text;
  }
  console.log(final_text);
  $(this).text(final_text); 
  $(this).attr("title", original_text);
});

/////////////////////////////////////
// Titulo Categoria                //
/////////////////////////////////////

if($('#products_grid_before li.active')){
  var category = $('#products_grid_before li.active').text();
  $('.product-category').text(category);
}

/////////////////////////////////////
// Quitar separador Menu Principal //
/////////////////////////////////////

$("ul#top_menu .divider").remove();

/////////////////////////////////////
// Correcion Buscador              //
/////////////////////////////////////
var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

$('.buscadorhome input[name="search"]').val(getUrlParameter('search'));

/////////////////////////////////////
// Doble menu categorias           //
/////////////////////////////////////

//var all_products = '<a href="/shop" data-oe-source-id="919" data-oe-id="921" data-oe-model="ir.ui.view" data-oe-field="arch" data-oe-xpath="/data/xpath[1]/ul/li[1]/a[1]">Todos los productos</a>';
var a_p = $('#products_grid_before .mt16 > li').first()[0];
$('#products_grid_before .mt16 > li').first().remove();
$('#products_grid_before .mt16 > li > ul > li:eq(0)').before(a_p);
$('#products_grid_before .mt16 > li > ul > li:eq(0)').css('font-weight','bolder');
$('#products_grid_before .mt16 > li > ul > li:eq(0)').css('font-size','1.2em');

$('#products_grid_before .mt16 > li > a').each(function(i){
    var categoryHeader = $(this).text();
    $(this).replaceWith('<h3>'+categoryHeader+'</h3>');
});


/////////////////////////////////////
/////////////////////////////////////
/////////////////////////////////////

/*
$.urlParam = function(name){
	var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
	return results[1] || 0;
}

console.log($.urlParam('search'));
*/
