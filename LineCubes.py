###################################################  START  ###################################################
############################################ continuum subtraction ############################################
###############################################################################################################

FontUV=raw_input("Please input the source name: ")

Channels_cont_spw01=raw_input("Please input the channels of continuum in spw0 and spw1: ")
Channels_cont_spw23=raw_input("Please input the channels of continuum in spw2 and spw3: ")

print('\n' + "The channels of continuum in spw0 and spw1 are: "+str(Channels_cont_spw01))
print('\n' + "The channels of continuum in spw2 and spw3 are: "+str(Channels_cont_spw23))

baseline_spw0=input("Please input the baseline in spw0 (mJy): ")
baseline_0="{:.3f}".format(2*baseline_spw0)+'mJy'
baseline_spw1=input("Please input the baseline in spw1 (mJy): ")
baseline_1="{:.3f}".format(2*baseline_spw1)+'mJy'
baseline_spw2=input("Please input the baseline in spw2 (mJy): ")
baseline_2="{:.3f}".format(2*baseline_spw2)+'mJy'
baseline_spw3=input("Please input the baseline in spw3 (mJy): ")
baseline_3="{:.3f}".format(2*baseline_spw3)+'mJy'

print('\n' + "The baselines of each spw are: "+str(baseline_0)+'\t'+str(baseline_1)+'\t'+str(baseline_2)+'\t'+str(baseline_3))


#### sutract continuum channels which identify in the previous dirty cubes images
print('\n' + "######## Sutract continuum channels with spw='0,1' ......")
uvcontsub(vis= FontUV+'.noflagging.selfcal.ms',
    spw= '0,1',
    fitspw=Channels_cont_spw01,
    excludechans= False,          # fit the region in fitspw
    solint= 'int',             # no time averaging, do a fit for each integration and let the noise fits average out in the image
    fitorder= 1,            # polynomial order for the fits of the continuum
    want_cont= False)        # create vis+'.contsub' to hold the continuum estimate


#### delmol the contsub file
delmod(vis= FontUV+'.noflagging.selfcal.ms.contsub')


#### use tclean to make Selfcaled, continuum-subtracted images cubes
print('\n' + "######## Make selfcaled, continuum-subtracted images cubes with StokesI (dirty images cubes in StokesQUV), with spw=0/1, separately ......")
# Stokes I:
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw0.selfcal.contsub.finalcube_StokesI',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '0',
    specmode= 'cube',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,
    threshold=baseline_0,
    pblimit= -1,
    niter= 100000,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw1.selfcal.contsub.finalcube_StokesI',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '1',
    specmode= 'cube',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    threshold=baseline_1,
    pblimit= -1,
    niter= 100000,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    


# Stokes Q:
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw0.selfcal.contsub.finaldirtycube_StokesQ',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '0',
    specmode= 'cube',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw1.selfcal.contsub.finaldirtycube_StokesQ',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '1',
    specmode= 'cube',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    


# Stokes U:
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw0.selfcal.contsub.finaldirtycube_StokesU',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '0',
    specmode= 'cube',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw1.selfcal.contsub.finaldirtycube_StokesU',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '1',
    specmode= 'cube',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    

# Stokes V:
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw0.selfcal.contsub.finaldirtycube_StokesV',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '0',
    specmode= 'cube',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    

tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw1.selfcal.contsub.finaldirtycube_StokesV',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '1',
    specmode= 'cube',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    

#################################################################################### split line ##################################################################

os.system('rm -r '+FontUV+'.noflagging.selfcal.ms.contsub')

uvcontsub(vis= FontUV+'.noflagging.selfcal.ms',
    spw= '2,3',
    fitspw=Channels_cont_spw23,
    excludechans= False,          # fit the region in fitspw
    solint= 'int',             # no time averaging, do a fit for each integration and let the noise fits average out in the image
    fitorder= 1,            # polynomial order for the fits of the continuum
    want_cont= False)        # create vis+'.contsub' to hold the continuum estimate


#### delmol the con
delmod(vis= FontUV+'.noflagging.selfcal.ms.contsub')


#### use tclean to make Selfcaled, continuum-subtracted images cubes
print('\n' + "######## Make selfcaled, continuum-subtracted images cubes with StokesI (dirty images cubes in StokesQUV), with spw=2/3 (0/1 in tclean), separately ......")
# Stokes I:
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw2.selfcal.contsub.finalcube_StokesI',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '0',
    specmode= 'cube',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    threshold=baseline_2,
    pblimit= -1,
    niter= 100000,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw3.selfcal.contsub.finalcube_StokesI',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '1',
    specmode= 'cube',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    threshold=baseline_3,
    pblimit= -1,
    niter= 100000,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory

# Stokes Q:
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw2.selfcal.contsub.finaldirtycube_StokesQ',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '0',
    specmode= 'cube',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw3.selfcal.contsub.finaldirtycube_StokesQ',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '1',
    specmode= 'cube',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)


# Stokes U:
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw2.selfcal.contsub.finaldirtycube_StokesU',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '0',
    specmode= 'cube',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw3.selfcal.contsub.finaldirtycube_StokesU',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '1',
    specmode= 'cube',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)


# Stokes V:
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw2.selfcal.contsub.finaldirtycube_StokesV',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '0',
    specmode= 'cube',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory
    
tclean(vis= FontUV + '.noflagging.selfcal.ms.contsub',
    imagename= FontUV + '.spw3.selfcal.contsub.finaldirtycube_StokesV',
    imsize= 256,
    cell= ['0.1arcsec'],
    spw= '1',
    specmode= 'cube',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    pblimit= -1,
    niter= 0,
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)


os.system('rm -r '+FontUV+'.noflagging.selfcal.ms.contsub')

###################################################   END   ###################################################
############################################ continuum subtraction ############################################
###############################################################################################################
