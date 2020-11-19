# -------
#   connectivity_check.py

from pyats import aetest

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(self,
                       testbed,
                       ios1_name = 'CiscoL3-1',
                       ios2_name = 'CiscoL3-2'):
        ios1 = testbed.devices[ios1_name]
        ios2 = testbed.devices[ios2_name]

        # add them to testscript parameters
        self.parent.parameters.update(ios1 = ios1, ios2 = ios2)

        # get corresponding links
        links = ios1.find_links(ios2)
        
        assert len(links) >= 1, 'require one link between ios1 and ios2'
    
    @aetest.subsection
    def establish_connections(self, steps, ios1, ios2):
        with steps.start('Connecting to %s' % ios1.name):
            ios1.connect()

        with steps.start('Connecting to %s' % ios2.name):
            ios2.connect()

@aetest.loop(device=('ios1', 'ios2'))
class PingTestcase(aetest.Testcase):

   @aetest.subsection
   def logInfo(self, device):
        logger.info('connecion to {} is successful'.format(device))
    
class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, steps, ios1, ios2):
        with steps.start('Disconnecting from %s' % ios1.name):
            ios1.disconnect()
        with steps.start('Disconnecting from %s' % ios2.name):
            ios2.disconnect()

if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed',
                        type = loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
