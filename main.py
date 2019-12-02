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

from __future__ import print_function
import webapp2
import jinja2
import os

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# The handler section
class IndexPage(webapp2.RequestHandler):
    def get(self):
        index_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(index_template.render())  # the response

    def post(self):
        pass

class EventsPage(webapp2.RequestHandler):
    def get(self):
        events_template = the_jinja_env.get_template('templates/events.html')
        self.response.write(events_template.render())  # the response

    def post(self):
        pass
        
class TeamPage(webapp2.RequestHandler):
    def get(self):
        team_template = the_jinja_env.get_template('templates/team.html')
        self.response.write(team_template.render())  # the response

    def post(self):
        pass

class JoinPage(webapp2.RequestHandler):
    def get(self):
        join_template = the_jinja_env.get_template('templates/join.html')
        self.response.write(join_template.render())  # the response

    def post(self):
        pass

app = webapp2.WSGIApplication([
    ('/', IndexPage),
    ('/events', EventsPage),
    ('/team', TeamPage),
    ('/join', JoinPage)
], debug=True)