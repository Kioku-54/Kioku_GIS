# =================================================================
#
# Authors: Timo Tuunanen <timo.tuunanen@rdvelho.com>
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2019 Timo Tuunanen
# Copyright (c) 2022 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import json
import sys
from pymongo import MongoClient
from pymongo import GEOSPHERE

monogourl = 'mongodb://localhost:27017/'
mongodb = 'testdb'
mongocollection = 'testplaces'

if len(sys.argv) == 1:
    print(f'Usage: {sys.argv[0]} <path/to/data.geojson>')
    sys.exit(1)

myclient = MongoClient(monogourl)
mydb = myclient[mongodb]
mycol = mydb[mongocollection]
mycol.drop()

with open(sys.argv[1]) as fh:
    d = json.load(fh)

mycol.create_index([("geometry", GEOSPHERE)])
mycol.insert_many(d['features'])
