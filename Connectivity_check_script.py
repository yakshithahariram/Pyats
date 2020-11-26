from pyats import aetest
log = logging.getLogger(__name__)

###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################
class common_setup(aetest.CommonSetup):
  
    @aetest.subsection
    def sample_subsection_1(self):
        log.info("Aetest Common Setup ")

    @aetest.subsection
    def sample_subsection_2(self, testbed,
                       ios1_name = 'CiscoL3-1',
                       ios2_name = 'CiscoL3-2'):
        ios1 = testbed.devices[ios1_name]
        ios2 = testbed.devices[ios2_name]
        log.info("IOS devices are %s" % (ios1))

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

class tc_one(aetest.Testcase):

    @ aetest.test
    def simple_test_1(self):
        """ Sample test section. Only print """
        log.info("First test section ")

#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

class common_cleanup(aetest.CommonCleanup):
    @aetest.subsection
    def clean_everything(self):
        """ Common Cleanup Subsection """
        log.info("Aetest Common Cleanup ")

if __name__ == '__main__': # pragma: no cover
    aetest.main()
