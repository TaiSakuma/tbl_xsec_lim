tbl_xsec_lim
============

Scripts to run [RooStatsCl95](https://twiki.cern.ch/twiki/bin/view/CMS/RooStatsCl95).


In a CMSSW environment


        cmsrel CMSSW_5_3_12_patch2
        cd CMSSW_5_3_12_patch2
        cvs co -r V00-02-06 StatisticalTools/RooStatsRoutines
        root -b
        gSystem -> SetIncludePath( "-I$ROOFITSYS/include" );
        .L StatisticalTools/RooStatsRoutines/root/roostats_cl95.C+
        .q
        git clone git@github.com:TaiSakuma/tbl_xsec_lim
        ./tbl_xsec_lim/tbl_xsec_lim.py -i ./tbl_xsec_lim/tbl_counts.txt


Without a CMSSW environment


        cvs co -r V00-02-06 StatisticalTools/RooStatsRoutines
        root -b
        gSystem -> SetIncludePath( "-I$ROOFITSYS/include" );
        .L StatisticalTools/RooStatsRoutines/root/roostats_cl95.C+
        git clone git@github.com:TaiSakuma/tbl_xsec_lim
        ./tbl_xsec_lim/tbl_xsec_lim.py -i ./tbl_xsec_lim/tbl_counts.txt
