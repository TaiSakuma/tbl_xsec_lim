#!/usr/bin/env python
# Tai Sakuma <sakuma@fnal.gov>
import ROOT
import sys
import numpy
from numpy.lib import recfunctions
import matplotlib.mlab
from optparse import OptionParser

##____________________________________________________________________________||
ROOT.gROOT.SetBatch(1)
ROOT.gSystem.Load("StatisticalTools/RooStatsRoutines/root/roostats_cl95_C.so")
# ROOT.SetParameter("Verbosity", 3);

##____________________________________________________________________________||
parser = OptionParser()
parser.add_option('-i', '--inputPath', default = "./tbl_xsec_lim/tbl_counts.txt", action = 'store', type = 'string')
parser.add_option('-o', '--outputPath', default = "./tbl_xsec_lim.txt", action = 'store', type = 'string')
(options, args) = parser.parse_args(sys.argv)

##____________________________________________________________________________||
p = numpy.recfromtxt(options.inputPath, names = True)

##____________________________________________________________________________||
if p.size == 1:
    p = numpy.rec.array([p.item()], p.dtype)

##____________________________________________________________________________||
if 'xsec_lim_exp' not in p.dtype.names:
    p = numpy.rec.array(recfunctions.append_fields(p, "xsec_lim_exp", [-1.0]*len(p)))

if 'xsec_lim_obs' not in p.dtype.names:
    p = numpy.rec.array(recfunctions.append_fields(p, "xsec_lim_obs", [-1.0]*len(p)))

for r in p:
    if r['xsec_lim_exp'] > 0 and r['xsec_lim_obs'] > 0: continue
    try:
        l = ROOT.GetClsLimit(r['ilum'], r['slum'], r['eff'], r['seff'], r['bck'], r['sbck'], int(r['n']))
        r['xsec_lim_exp'] = l.GetExpectedLimit()
        r['xsec_lim_obs'] = l.GetObservedLimit()
    except:
        print sys.exc_info()[0]

matplotlib.mlab.rec2csv(p, options.outputPath, delimiter = " ")

##____________________________________________________________________________||
if __name__ == '__main__':
    pass
