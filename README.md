tbl_xsec_lim
============

        cmsrel CMSSW_5_3_12_patch2
        cd CMSSW_5_3_12_patch2
        export CVSROOT=:ext:sakuma@cmssw.cvs.cern.ch:/local/reps/CMSSW
        cvs co -r V00-02-06 StatisticalTools/RooStatsRoutines
        root -b
        gSystem -> SetIncludePath( "-I$ROOFITSYS/include" );
        .L StatisticalTools/RooStatsRoutines/root/roostats_cl95.C+
        git clone git@github.com:TaiSakuma/tbl_xsec_lim
        ./tbl_xsec_lim/tbl_xsec_lim.py -i ./tbl_xsec_lim/tbl_cls_input_pas_repro.txt 





