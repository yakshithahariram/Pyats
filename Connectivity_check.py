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

@aetest.loop(device=('ios1', 'ios2'))
class PingTestcase(aetest.Testcase):

   @aetest.subsection
    def establish_connections(self, ios1, ios2):
            ios1.connect()
            ios2.connect()


class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, ios1, ios2):
            ios1.disconnect()
            ios2.disconnect()

if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
