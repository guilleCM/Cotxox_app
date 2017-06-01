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
		$('#other').val(parseFloat($(this).val()));
	} else {
		$('#price').text(price);
		$('#other').val(0);
	}
});

$('#btn-next').click(function() {
	var price = parseFloat($('#price').html());
	var creditCard = $('#creditCard').html();
	var tip = parseFloat($('#tip-list > li.active').val());
	var data = JSON.parse($('#data').val());
	data["cost"] = price;
	data["creditCard"] = creditCard;
	data['tip'] = tip;
	var output = JSON.stringify(data);
	$('#data').val(output);
});