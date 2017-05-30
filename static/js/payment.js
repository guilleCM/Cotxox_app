var price = parseFloat($('#price').text());
$(document).ready(function(){
	var tipPrice = price+1;
	$('#price').text(tipPrice);
});
$('#tip-list > li').click(function(){
	if($(this).attr('id') == 'other'){
		$(this).siblings().removeClass('active');
		$(this).addClass('active');
		$('#tipInput').show();
		$('#price').text(price);
	}else {
		$(this).siblings().removeClass('active');
		$(this).addClass('active');
		$('#tipInput').hide();
		$('#price').text(price+parseFloat($(this).val()));

	}
});

$('#othertip').on("change keyup", function(){
	var inputPrice = $(this).val();
	if(inputPrice> 0){
		$('#price').text(price + parseFloat($(this).val()));
	} else {
		$('#price').text(price);
	}
});