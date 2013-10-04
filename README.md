tbl_xsec_lim
============

Scripts to run [RooStatsCl95](https://twiki.cern.ch/twiki/bin/view/CMS/RooStatsCl95).


In a CMSSW environment


        $ cmsrel CMSSW_5_3_12_patch2
        $ cd CMSSW_5_3_12_patch2
        $ cvs co -r V00-02-06 StatisticalTools/RooStatsRoutines
        $ root -b
        root [0] gSystem -> SetIncludePath( "-I$ROOFITSYS/include" );
        root [1] .L StatisticalTools/RooStatsRoutines/root/roostats_cl95.C+
        root [2] .q
        $ git-clone https://github.com/TaiSakuma/tbl_xsec_lim.git # or git@github.com:TaiSakuma/tbl_xsec_lim
        $ ./tbl_xsec_lim/tbl_xsec_lim.py -i ./tbl_xsec_lim/tbl_counts.txt


Without a CMSSW environment

        $ cvs co -r V00-02-06 StatisticalTools/RooStatsRoutines
        $ root -b
        root [0] gSystem -> SetIncludePath( "-I$ROOFITSYS/include" );
        root [1] .L StatisticalTools/RooStatsRoutines/root/roostats_cl95.C+
        root [2] .q
        $ git-clone https://github.com/TaiSakuma/tbl_xsec_lim.git # or git@github.com:TaiSakuma/tbl_xsec_lim
        $ ./tbl_xsec_lim/tbl_xsec_lim.py -i ./tbl_xsec_lim/tbl_counts.txt
