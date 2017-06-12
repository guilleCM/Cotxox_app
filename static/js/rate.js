$('.rates i').click(function() {
	var index = $(this).index();
	var position = 0;
	for(var i = 0; i<= index; i++){
		$('.rates :nth-child('+(i+1)+')').addClass('active');
		$('.rates :nth-child('+(i+1)+')').removeAttr('id', 'selected');
		position++;
	}
	for(var i = position; i<= 4; i++){
		$('.rates :nth-child('+(i+1)+')').removeClass('active');
		$('.rates :nth-child('+(i+1)+')').removeAttr('id', 'selected');
	}
	$(this).attr('id', 'selected');
});
$('.rates i').hover(function() {
	var index = $(this).index();
	var position = 0;
	for(var i = 0; i<= index; i++){
		$('.rates :nth-child('+(i+1)+')').addClass('active');
		position++;
	}
	for(var i = position; i<= 4; i++){
		$('.rates :nth-child('+(i+1)+')').removeClass('active');
	}
});

$('#btn-rate').click(function(){
	var rate = $('#selected').index() + 1;
	var dict = JSON.parse($('#data').val());
	dict['rate'] = rate;
	var output = JSON.stringify(dict);
	$('#data').val(output);
	console.log(dict);
});