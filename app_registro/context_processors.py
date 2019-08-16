def active_page(request):
	if 'page' in request.session:
		page_name = request.session['page']
	else:
		page_name = ''

	return {'page_name': page_name}