#!/usr/bin/python
from  nfs4client import NFS4Client

import nfs4_ops as op

n = NFS4Client()
n.compound([op.advise(2)])
