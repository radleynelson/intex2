from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):
    utc_time = datetime.utcnow()
    print(1111111111)
    print()
    print()
    print()
    print()
    print()

    username = str(request.user.username)
    pageMessage = ''
    showMessage = False

    try:
        pageMessage = request.session['pageMessage']
    except:
        pageMessage = ''

    try:
        showMessage = request.session['showMessage']
    except:
        showMessage = False

    request.session['showMessage'] = False
    request.session['pageMessage'] = ''

    context = {
        # sent to index.html:
        'utc_time': utc_time,
        'user': username,
        # sent to index.html and index.js:
        jscontext('data'): {
            'showMessage': showMessage,
            'pageMessage': pageMessage,
            'user': username
        }
    }
    return request.dmp.render('index.html', context)