# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: step1 --filein lhe:10267 --fileout file:HIG-Summer12pLHE-00244.root --mc --eventcontent LHE --datatier GEN --conditions START53_V7C::All --step NONE --python_filename HIG-Summer12pLHE-00244_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 2880

import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source all available *.lhe for a particular mode
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('file:unweighted_events.lhe')
    #fileNames = cms.untracked.vstring('rfio:gg2VV_INTERFERENCE_1_unweightedEvents.lhe',
    #	                      'rfio:gg2VV_INTERFERENCE_2_unweightedEvents.lhe',
    #			      'rfio:gg2VV_INTERFERENCE_3_unweightedEvents.lhe')
)

process.options = cms.untracked.PSet(

)

from Configuration.Generator.PythiaUEZ2Settings_cfi import * 
#from Configuration.Generator.Pythia8CommonSettings_cfi import *
process.generator = cms.EDFilter("Pythia6HadronizerFilter",
#process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(500),
    comEnergy = cms.double(8000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        #pythia8CommonSettingsBlock,
        processParameters = cms.vstring(
             'MSEL=0         ! User defined processes', 
             'PMAS(5,1)=4.4   ! b quark mass',
             'PMAS(6,1)=172.4 ! t quark mass',
             'MSTJ(1)=1       ! Fragmentation/hadronization on or off',
             'MSTP(61)=0      ! Parton showering on or off',
             'MSTP(71)=0      ! final state',
             'MSTP(81)=0      ! MPI',
             'MSTP(91)=0      ! pT smearing'),
             #'PartonLevel:ISR = off',
             #'PartonLevel:FSR = off',
             #'PartonLevel:MPI = off'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    ),
    ## jetMatching = cms.untracked.PSet(
    ##    scheme = cms.string("Madgraph"),
    ##    mode = cms.string("auto"),	# soup, or "inclusive" / "exclusive"
    ##    MEMAIN_etaclmax = cms.double(5.0),
    ##    MEMAIN_qcut = cms.double(0.), 
    ##    MEMAIN_minjets = cms.int32(-1), 
    ##    MEMAIN_maxjets = cms.int32(-1),
    ##    MEMAIN_showerkt = cms.double(0),   
    ##    MEMAIN_excres = cms.string(""),
    ##    MEMAIN_nqmatch = cms.int32(5),
    ##    outTree_flag = cms.int32(0)    
    ## )
                                 
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('-s nevts:10'), 
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('FIRST_OUTPUT.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
#process.GlobalTag.globaltag = 'MC_42_V12::All' START53_V7E::All
process.GlobalTag.globaltag = 'START53_V7C::All' #START53_V7E

process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)

# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 
