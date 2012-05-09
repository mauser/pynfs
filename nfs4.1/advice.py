#!/usr/bin/python
from  nfs4client import NFS4Client
from nfs4_type import stateid4
import nfs4_ops as op

print "<----- Starting advice!!! ------------->"
n = NFS4Client()
stateid = stateid4(0, "12")
n.compound([op.advise(stateid,20,10,2)])
