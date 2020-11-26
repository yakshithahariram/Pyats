import logging
import os

from pyats import aetest
from pyats.topology import loader
log = logging.getLogger(__name__)
#testbed = loader.load('/home/vagrant/pyats/Pyats/IOS_testbed.yml')
###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################

class common_setup(aetest.CommonSetup):
    """ Common Setup section --- optional"""

    @aetest.subsection
    def sample_subsection_1(self):
        log.info("Aetest Common Setup ")

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

class tc_one(aetest.Testcase):
    """ This is user Testcases section---mandatory"""
    @ aetest.test
    def ping_test(self):
        log.info("checking whether routers are up/down by using ping ")
        ip = ["192.168.1.150", "192.168.1.151", "192.168.1.152", "192.168.1.153"]
        list = ["32769","32770","32771","32782"]
        ports_up = []
        ports_down = []
        i=0
        while(i<4):
                z = ip[i]
                result = os.system(" ping -c 1 " +z)
                if result == 0:
                        ports_up.append(list[i])
                        log.info("%s is up" %(list[i]))
                        i = i+1
                else:
                        ports_down.append(list[i])
                        log.info("%s is down" %(list[i]))
                        i=i+1
        log.info("ports up %s" %(ports_up))
        log.info("ports down %s" %(ports_down))

#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test ---optional"""
    @aetest.subsection
    def clean_everything(self):
        log.info("Aetest Common Cleanup ")

if __name__ == '__main__': # pragma: no cover
    aetest.main()
