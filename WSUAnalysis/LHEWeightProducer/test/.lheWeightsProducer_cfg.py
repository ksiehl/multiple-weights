import FWCore.ParameterSet.Config as cms

process = cms.Process("WEIGHTS")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 25

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:/afs/cern.ch/user/s/sturdy/work/WSUAnalysis/anomalous_couplings/GEN_TO_RECO/step1/NEWER_TRY_multi.root'
        'file:/uscms_data/d3/ksiehl/CMSSW_5_3_20/src/step1/FIRST_OUTPUT.root'
    )
)


MGWeightsFromLHE = cms.EDProducer('LHEWeightProducer',
    lheSrc            = cms.InputTag("source"),
    #lheSrc            = cms.InputTag("generator"),
    weightLabel       = cms.string("mg_reweight_13"),
    makeWeightsMap    = cms.untracked.bool(True),
    produceAllWeights = cms.untracked.bool(False),
    numWeights        = cms.int32(30),
    debug             = cms.untracked.bool(False)
)

#identical copy of the producer
process.weightsMap = MGWeightsFromLHE.clone()


#template copy, change to no make weights map, no produce all weights
process.weight00   = process.weightsMap.clone(
    makeWeightsMap    = cms.untracked.bool(False),
    weightLabel       = cms.string("mg_reweight_10"),
    )


process.weight01   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_01"),
    )
process.weight02   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_02"),
    )
process.weight03   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_03"),
    )
process.weight04   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_04"),
    )
process.weight05   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_05"),
    )
process.weight06   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_06"),
    )
process.weight07   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_07"),
    )
process.weight08   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_08"),
    )
process.weight09   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_09"),
    )
process.weight10   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_10"),
    )
process.weight11   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_11"),
    )
process.weight12   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_12"),
    )
process.weight13   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_13"),
    )
process.weight14   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_14"),
    )
process.weight15   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_15"),
    )
process.weight16   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_16"),
    )
process.weight17   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_17"),
    )
process.weight18   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_18"),
    )
process.weight19   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_19"),
    )
process.weight20   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_20"),
    )
process.weight21   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_21"),
    )
process.weight22   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_22"),
    )
process.weight23   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_23"),
    )
process.weight24   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_24"),
    )
process.weight25   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_25"),
    )
process.weight26   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_26"),
    )
process.weight27   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_27"),
    )
process.weight28   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_28"),
    )
process.weight29   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_29"),
    )
process.weight30   = process.weight00.clone(
    weightLabel       = cms.string("mg_reweight_30"),
    )


#different template, not used, no for make weights map and yes for produce all weights
process.allWeights = MGWeightsFromLHE.clone(
    makeWeightsMap    = cms.untracked.bool(False),
    produceAllWeights = cms.untracked.bool(True),
)

process.out = cms.OutputModule("PoolOutputModule",
    #fileName = cms.untracked.string('testOut.root')
    fileName = cms.untracked.string('INTERMEDIATE_OUTPUT.root')
)

process.MGWeights = cms.Sequence(
      process.weight01
      + process.weight02
      + process.weight03
      + process.weight04
      + process.weight05
      + process.weight06
      + process.weight07
      + process.weight08
      + process.weight09
      + process.weight10
      + process.weight11
      + process.weight12
      + process.weight13
      + process.weight14
      + process.weight15
      + process.weight16
      + process.weight17
      + process.weight18
      + process.weight19
      + process.weight20
      + process.weight21
      + process.weight22
      + process.weight23
      + process.weight24
      + process.weight25
      + process.weight26
      + process.weight27
      + process.weight28
      + process.weight29
      + process.weight30
      + process.allWeights
      #process.weightsMap
      )
process.p = cms.Path(process.MGWeights)

process.e = cms.EndPath(process.out)
