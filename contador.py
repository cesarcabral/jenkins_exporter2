#!/usr/bin/python

import json
import requests
import get_build_info
import jenkins_exporter


class NumBuildsStats(Stats):
    """ generated source for class NumBuildsStats """
    success = int()
    unstable = int()
    fail = int()

    def __init__(self):
        """ generated source for method __init__ """
        super(NumBuildsStats, self).__init__()
        self.success = 0
        self.unstable = 0
        self.fail = 0

    def compute(self, job):
        """ generated source for method compute """
        builds = job.getBuilds()
        for build in builds:
            #  a build result can be null if the build is currently building (JENKINS-15067)
            if build.getResult() != None:
                if build.get_build_info().isBetterOrEqualTo(result.SUCCESS):
                    addSuccess()
                elif build.getResult().isBetterOrEqualTo(result.UNSTABLE):
                    addUnstable()
                elif build.getResult().isBetterOrEqualTo(result.FAILURE):
                    addFail()

    def addSuccess(self):
        """ generated source for method addSuccess """
        self.success += 1

    def addUnstable(self):
        """ generated source for method addUnstable """
        self.unstable += 1

    def addFail(self):
        """ generated source for method addFail """
        self.fail += 1

    def getSuccess(self):
        """ generated source for method getSuccess """
        return self.success

    def getUnstable(self):
        """ generated source for method getUnstable """
        return self.unstable

    def getFail(self):
        """ generated source for method getFail """
        return self.fail

    def getSuccessPct(self):
        """ generated source for method getSuccessPct """
        total = self.success + self.unstable + self.fail
        return (float(self.success) / total) if total != 0 else 0

    def getUnstablePct(self):
        """ generated source for method getUnstablePct """
        total = self.success + self.unstable + self.fail
        return (float(self.unstable) / total) if total != 0 else 0

    def getFailPct(self):
        """ generated source for method getFailPct """
        total = self.success + self.unstable + self.fail
        return (float(self.fail) / total) if total != 0 else 0