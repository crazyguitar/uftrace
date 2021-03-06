#!/usr/bin/env python

from runtest import TestBase

class TestCase(TestBase):
    def __init__(self):
        TestBase.__init__(self, 'lib', """
# DURATION    TID     FUNCTION
            [17457] | lib_a() {
   6.911 us [17457] |   lib_b();
   8.279 us [17457] | } /* lib_a */
""", sort='simple')

    def build(self, name, cflags='', ldflags=''):
        return TestBase.build_libabc(self, name, cflags, ldflags)

    def runcmd(self):
        return '%s --force --no-libcall -T lib_b@libabc_test,depth=1 %s' % (TestBase.ftrace, 't-' + self.name)
