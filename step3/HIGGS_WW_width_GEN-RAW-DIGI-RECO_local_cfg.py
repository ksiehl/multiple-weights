# Auto generated configuration file
# using: 
# Revision: 1.372.2.1 
# Source: /local/reps/CMSSW.admin/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: STEP2 --step RAW2DIGI,L1Reco,RECO,VALIDATION:validation_prod,DQM:DQMOfflinePOGMC --conditions START50_V15::All --pileup 2012_Startup_50ns_PoissonOOTPU --datamix NODATAMIXER --eventcontent AODSIM --datatier AODSIM -n 10 --no_exec --mc --filein tc_RAWSIM.root --fileout tc_AODSIM.root --python_filename qiangli-WpWmEW_RECO_cfg.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2012_Startup_50ns_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('Configuration.StandardSequences.ReMixingSeeds_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-10)
)

input_string = '20150331_125151'

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring(#'rfio:HIGGS_WIDTH_WW_INTERFERENCE_CMSSW_5_3_14_GEN_SIM_RAW_HLT.root'
    #'/uscms_data/d3/ksiehl/CMSSW_5_3_20/src/step2/crab_' + input_string + '/results/SECOND_OUTPUT_1.root'
    #'file:/uscms_data/d3/ksiehl/CMSSW_5_3_20/src/step2/output.root'
    #'file:/uscms_data/d3/ksiehl/CMSSW_5_3_20/src/step2/SECOND_OUTPUT.root'
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_1.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_2.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_3.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_4.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_5.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_6.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_7.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_8.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_9.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_10.root',
    #'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_20.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_30.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_40.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_50.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_60.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_70.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_80.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_90.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_11.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_21.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_31.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_41.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_51.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_61.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_71.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_81.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_91.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_12.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_22.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_32.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_42.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_52.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_62.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_72.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_82.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_92.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_13.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_23.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_33.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_43.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_53.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_63.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_73.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_83.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_93.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_14.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_24.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_34.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_44.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_54.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_64.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_74.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_84.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_94.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_15.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_25.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_35.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_45.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_55.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_65.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_75.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_85.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_95.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_16.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_26.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_36.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_46.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_56.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_66.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_76.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_86.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_96.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_17.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_27.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_37.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_47.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_57.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_67.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_77.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_87.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_97.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_18.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_28.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_38.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_48.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_58.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_68.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_78.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_88.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_98.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_19.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_29.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_39.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_49.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_59.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_69.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_79.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_89.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_99.root',
    'root://cms-xrd-global.cern.ch//store/user/ksiehl/MinBias/FERMILAB_SL6_S2_ANOM_NotShowering/160513_172850/0000/SECOND_OUTPUT_100.root'
    )
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.372.2.1 $'),
    annotation = cms.untracked.string('STEP2 nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string('THIRD_OUTPUT.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('AODSIM')
    )
)
process.AODSIMoutput.outputCommands.append('keep *_allWeights_*_*')
process.AODSIMoutput.outputCommands.append('keep *_weightsMap_*_*')
# Additional output definition

# Other statements
process.mix.playback = True
process.GlobalTag.globaltag = 'START53_V19::All'

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.dqmoffline_step = cms.Path(process.DQMOfflinePOGMC)
process.validation_step = cms.EndPath(process.validation_prod)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.validation_step,process.dqmoffline_step,process.endjob_step,process.AODSIMoutput_step)

