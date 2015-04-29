from behave.formatter.base import Formatter
from behave.model_describe import ModelDescriptor
from teamcity import messages


class TeamcityFormatter(Formatter):
    description = "Test"

    def __init__(self, stream_opener, config):
        super(TeamcityFormatter, self).__init__(stream_opener, config)
        self.current_feature = None
        self.current_scenario = None
        self.current_step = None
        self.msg = messages.TeamcityServiceMessages()

    def feature(self, feature):
        self.current_feature = feature
        self.current_scenario = None
        self.current_step = None
        self.msg.testSuiteStarted(self.current_feature.name)

    def scenario(self, scenario):
        if self.current_scenario and self.current_scenario.status == "skipped":
            self.msg.testIgnored(self.current_scenario.name)

        self.current_scenario = scenario
        self.current_step = None
        self.msg.testStarted(self.current_scenario.name, captureStandardOutput='false')

    def step(self, step):
        self.current_step = step

    def result(self, step_result):
        if self.current_scenario.status == "untested":
            return

        if self.current_scenario.status == "passed":
            self.msg.message('testFinished', name=self.current_scenario.name,
                             duration=str(self.current_scenario.duration), flowId=None)

        if self.current_scenario.status == "failed":
            name = self.current_step.name

            error_msg = "Step failed: {}".format(name)
            if self.current_step.table:
                table = ModelDescriptor.describe_table(self.current_step.table, None)
                error_msg = "{}\nTable:\n{}".format(error_msg, table)

            if self.current_step.text:
                text = ModelDescriptor.describe_docstring(self.current_step.text, None)
                error_msg = "{}\nText:\n{}".format(error_msg, text)

            error_details = self.current_step.error_message

            self.msg.testFailed(self.current_scenario.name, message=error_msg, details=error_details)
            self.msg.message('testFinished', name=self.current_scenario.name,
                             duration=str(self.current_scenario.duration), flowId=None)

    def eof(self):
        self.msg.testSuiteFinished(self.current_feature.name)