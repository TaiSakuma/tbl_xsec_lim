#!/usr/bin/env python
# Tai Sakuma <sakuma@fnal.gov>
import ROOT
import sys
import numpy
import pandas
import StringIO
from optparse import OptionParser

##____________________________________________________________________________||
ROOT.gROOT.SetBatch(1)
ROOT.gSystem.Load("StatisticalTools/RooStatsRoutines/root/roostats_cl95_C.so")
# ROOT.SetParameter("Verbosity", 3);

##____________________________________________________________________________||
parser = OptionParser()
parser.add_option('-i', '--inputPath', default = "./tbl_xsec_lim/tbl_counts.txt", action = 'store', type = 'string')
parser.add_option('-o', '--outputPath', default = "./tbl_xsec_lim.txt", action = 'store', type = 'string')
parser.add_option("-n", "--nrows", action = "store", default = None, type = 'long')
(options, args) = parser.parse_args(sys.argv)

##____________________________________________________________________________||
file_noInitialSpace  = StringIO.StringIO("".join([l.lstrip() for l in open(options.inputPath).readlines()]))
p = pandas.read_table(file_noInitialSpace, header = 0, delim_whitespace = True, nrows = options.nrows)

##____________________________________________________________________________||
if 'xsec_lim_exp' not in p.columns:
    p['xsec_lim_exp'] = -1.0

if 'xsec_lim_obs' not in p.columns:
    p['xsec_lim_obs'] = -1.0

for i in xrange(0, len(p)):
    r =  p.iloc[i]
    print r
    if r['xsec_lim_exp'] > 0 and r['xsec_lim_obs'] > 0: continue
    try:
        l = ROOT.GetClsLimit(r['ilum'], r['slum'], r['eff'], r['seff'], r['bck'], r['sbck'], int(r['n']))
        p['xsec_lim_exp'][i] = l.GetExpectedLimit()
        p['xsec_lim_obs'][i] = l.GetObservedLimit()
    except:
        print sys.exc_info()[0]

f = open(options.outputPath, 'w')
p.to_string(f, index = False)
f.close()

##____________________________________________________________________________||
if __name__ == '__main__':
    # main()
    pass
