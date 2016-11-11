# Copyright 2015 Peter Beverloo. All rights reserved.
# Use of this source code is governed by the MIT license, a copy of which can
# be found in the LICENSE file.

# Bottle servlet to run tests.peter.sh//notification-generator/ locally.
# To run it, install bottle (pip install bottle).
# Then simply run python run_local.py and visit
# localhost:8080/ in your browser.
# TODO(miguelg) load the css. That needs a refactor on the php code.

from bottle import route, run
from bottle import static_file

@route('/')
@route('/notification-generator')
@route('/notification-generator/')
def server_static():
    return static_file('notification-generator.html', root='./tests/cases/')

@route('/notification-generator-sw.js')
@route('/notification-generator/notification-generator-sw.js')
def server_static():
    return static_file('notification-generator-sw.js', root='./tests/cases/')

@route('/cases/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./tests/cases/')

@route('/resources/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./tests/resources/')


run(host='localhost', port=8080, debug=True)
