#!/user/bin/env python
########################################################################################################################
# THIS FILE CONTAINS THE JENKINS API TOOLS TO GET AND UPDATE THE JENKINS OBJECTS CONFIG, PLUGINS, USERS, NODES, ETC    #
# THE IDEA OF HAVING THIS TOOL TO AVOID MAKING ANY CHANGES FROM THE UI AND AVOID ANY UNEXPECTED CHANGES TO OCCUR       #
# V.1.0                                                                                                                #
# USAGE: import jenkinstools                                                                                           #
#                                                                                                                      #
########################################################################################################################
from jenkins import Jenkins
from pprint import pprint


class JenkinsTools(object):
    """
    This is to expose the functional capability of jenkins for the various operations that it can perform programatically without having access to console.
    """

    _jenkins_url = None
    _login_id = None
    _password = None

    def __init__(self, jenkins_url, login_id, password):
        """
        Initialize the jenkins connection object
        :param jenkins_url:
        :param login_id:
        :param password:
        """
        self._jenkins_url = jenkins_url
        self._login_id = login_id
        self._password = password
        self.server_obj = Jenkins(jenkins_url, username=self._login_id, password=self._password)

    def get_jenkins_version(self):
        """
        To get the Jenkins version
        :return:
        """
        return self.server_obj.get_version()

    def get_job_details(self):
        """
        Get the jenkins job details.
        :return:
        """
        for job in self.server_obj.get_jobs():
            job_instance = self.server_obj.get_job(job[0])
            print 'Job Name:%s' % job_instance.name
            print 'Job Description:%s' %(job_instance.get_description())
            print 'Is Job running:%s' %(job_instance.is_running())
            print 'Is Job enabled:%s' %(job_instance.is_enabled())

    def get_job_count(self):
        """
        To get the count of jobs in Jenkins
        :return:
        """
        return self.server_obj.jobs_count()

    def disable_jenkins_job(self, job_name=None):
        """
        To  disable the jobs from jenkins.
        :return:
        """
        if self.server_obj.has_job(job_name):
            job_instance = self.server_obj.get_job(job_name)
            job_instance.disable()
            print 'Name:%s,Is Job Enabled ?:%s' % (job_name, job_instance.is_enabled())

    def get_jenkins_plugin_details(self):
        """
        To get the details of existing plugins in jenkins.
        :return:
        """
        for plugin in self.server_obj.get_plugins().values():
            print "Short Name:%s" % plugin.shortName
            print "Long Name:%s" % plugin.longName
            print "Version:%s" % plugin.version
            print "URL:%s" % plugin.url
            print "Active:%s" % plugin.active
            print "Enabled:%s" % plugin.enabled

    def get_plugin_details(self, plugin_name):
        """
        TO get the new plugin details
        :param plugin_name:
        :return:
        """
        plugins_metadata = self.server_obj.get_plugin_info(plugin_name)
        pprint(plugins_metadata)

    def getSCMInfroFromLatestGoodBuild(url, jobName, username=None, password=None):
        """
        To get the latest SCM from the latest good builds.
        :param url:
        :param jobName:
        :param username:
        :param password:
        :return:
        """
        J = Jenkins(url, username, password)
        job = J[jobName]
        lgb = job.get_last_good_build()
        return lgb.get_revision()

if __name__ == '__main__':
    pass
