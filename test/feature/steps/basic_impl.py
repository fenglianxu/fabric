# Copyright IBM Corp. 2017 All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from behave import *
import time


ORDERER_TYPES = ["solo",
                 "kafka",
                 "solo-msp"]

PROFILE_TYPES = {"solo": "SampleInsecureSolo",
                 "kafka": "SampleInsecureKafka",
                 "solo-msp": "SampleSingleMSPSolo"}


@given(u'I wait "{seconds}" seconds')
@when(u'I wait "{seconds}" seconds')
@then(u'I wait "{seconds}" seconds')
def step_impl(context, seconds):
    time.sleep(float(seconds))

@given(u'we compose "{composeYamlFile}"')
def compose_impl(context, composeYamlFile):
    pass

@given(u'I have a bootstrapped fabric network')
def step_impl(context):
    bootstrapped_impl(context, "solo")

@given(u'I have a bootstrapped fabric network of type {networkType}')
def bootstrapped_impl(context, networkType):
    pass

@given(u'{component} is taken down')
def step_impl(context, component):
    pass

@given(u'{component} comes back up')
def step_impl(context, component):
    pass
