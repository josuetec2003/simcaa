$(function () {

	$('.btn-registrar').on('click', function () {
		var pid = $(this).data('id'),
			url = $(this).data('url');

		$.get(url, {'pid': pid, 'accion': 'registrar'}, function (response) {
			alert(response.mensaje);

			if (response.exito)
			{
				$(`#tr-${pid}`).fadeOut('slow', function () {
					$(this).remove();
				})
			}
		}, 'json')

	})

	$('.btn-pagar').on('click', function () {
		var pid = $(this).data('id'),
			url = $(this).data('url');

		var pago = prompt('Ingrese el monto del pago');

		if (pago.trim().length == 0)
			return;

		$.get(url, {'pid': pid, 'accion': 'pagar', 'pago': pago}, function (response) {
			alert(response.mensaje);

			if (response.exito)
			{
				$(`#tr-${pid}`).fadeOut('slow', function () {
					$(this).remove();
				})
			}
		}, 'json')

	})

	$('.btn-regalar').on('click', function () {
		var $me = $(this),
			pid = $me.data('id'),
			url = $me.data('url');

		$.get(url, {'pid': pid, 'accion': 'regalar'}, function (response) {
			alert(response.mensaje);

			if (response.exito)
				$me.attr('disabled', true);
		}, 'json')

	})

})