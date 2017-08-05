# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import requests
import re
import numpy as np


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        page = requests.get('http://api.chbtc.com/data/v1/kline?currency=eth_cny&type=30min&size=90')
        page.encoding = page.apparent_encoding
        eos_close =  re.findall(r'(\d+.\d+),\d+.\d+][,|\]]',page.text)
        #print(eos_close)
        self.response.write(calAve(eos_close))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


def calAve(data):
    data = [float(i) for i in data]
    for i in range(0,len(data)-29):
        ma5 = np.average(data[25+i:30+i])
        ma10 = np.average(data[20+i:30+i])
        ma30 = np.average(data[i:30+i])
        print(i , ma5 , ma10  ,  ma30)
