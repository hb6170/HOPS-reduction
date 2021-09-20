FontUV='HOPS-12W_flagging'

os.system('cp -r HOPS-12W.ms tmp.ms')

tclean(vis='tmp.ms',     
    imagename=FontUV+'.spw0.dirty',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='0',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

flagdata(vis='tmp.ms',
    spw='0:700~1150',
    flagbackup=False)
    
tclean(vis='tmp.ms',     
    imagename=FontUV+'.spw0.check.dirty',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='0',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

split(vis='tmp.ms',
    spw='0,1,2,3',
    outputvis=FontUV+'.CO32.ms',
    width=[240,240,240,240],
    datacolumn='data')

tclean(vis=FontUV+'.CO32.ms',
    imagename=FontUV+'.CO32.StokesI_noselfcal',
    spw='0,1,2,3',
    specmode='mfs',
    deconvolver='hogbom',
    stokes='I',
    gridder='standard',
    imsize=512,
    cell=['0.1arcsec'],
    weighting='briggs',
    robust=0.5,
    threshold='0.0mJy',
    pblimit=-1,
    pbcor=True,
    niter=1000000,
    interactive=True,
    savemodel='modelcolumn')
    


#################################################### 1st selfcal #####################################################
FontUV='HOPS-12W_flagging'

gaincal(vis=FontUV+'.CO32.ms',
    caltable=FontUV+'.CO32.slfcal.1',
    refant='DA43',
    spw='0,1,2,3',
    gaintype='T',
    calmode='p',
    solint='600s')

plotcal(caltable=FontUV+'.CO32.slfcal.1',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=True,
    figfile='Gain_'+FontUV+'.CO32_slfcal1.png')
    
applycal(vis=FontUV+'.CO32.ms',
    gaintable=FontUV+'.CO32.slfcal.1',
    calwt=False,
    applymode='calonly',
    flagbackup=False)

split(vis=FontUV+'.CO32.ms',
    outputvis=FontUV+'.CO32.Slfc1.ms',
    datacolumn='corrected')

tclean(vis= FontUV + '.CO32.Slfc1.ms',
    imagename= FontUV + '.CO32.1',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.CO32.StokesI_noselfcal.mask',
    niter= 1000000,
    threshold= '0.0mJy',
    interactive= True,
    savemodel= 'modelcolumn')


#################################################### 2nd selfcal #####################################################
FontUV='HOPS-12W_flagging'

gaincal(vis=FontUV+'.CO32.Slfc1.ms',
    caltable=FontUV+'.CO32.slfcal.2',
    refant='DA43',
    spw='0,1,2,3',
    gaintype='T',
    calmode='p',
    solint='30s')

plotcal(caltable=FontUV+'.CO32.slfcal.2',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=True,
    figfile='Gain_'+FontUV+'.CO32_slfcal2.png')
    
applycal(vis=FontUV+'.CO32.Slfc1.ms',
    gaintable=FontUV+'.CO32.slfcal.2',
    calwt=False,
    applymode='calonly',
    flagbackup=False)

split(vis=FontUV+'.CO32.Slfc1.ms',
    outputvis=FontUV+'.CO32.Slfc2.ms',
    datacolumn='corrected')

tclean(vis= FontUV + '.CO32.Slfc2.ms',
    imagename= FontUV + '.CO32.2',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.CO32.1.mask',
    niter= 1000000,
    threshold= '0.0mJy',
    interactive= True,
    savemodel= 'modelcolumn')
    
#################################################### 3rd selfcal #####################################################
FontUV='HOPS-12W_flagging'

gaincal(vis=FontUV+'.CO32.Slfc2.ms',
    caltable=FontUV+'.CO32.slfcal.3',
    refant='DA43',
    spw='0,1,2,3',
    gaintype='T',
    calmode='p',
    solint='10s')

plotcal(caltable=FontUV+'.CO32.slfcal.3',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=True,
    figfile='Gain_'+FontUV+'.CO32_slfcal3.png')
    
applycal(vis=FontUV+'.CO32.Slfc2.ms',
    gaintable=FontUV+'.CO32.slfcal.3',
    calwt=False,
    applymode='calonly',
    flagbackup=False)

split(vis=FontUV+'.CO32.Slfc2.ms',
    outputvis=FontUV+'.CO32.Slfc3.ms',
    datacolumn='corrected')

tclean(vis= FontUV + '.CO32.Slfc3.ms',
    imagename= FontUV + '.CO32.3',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.CO32.2.mask',
    niter= 1000000,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')
    

#rms:
#noselfcal: 0.278 mJy		1st_selfcal: 0.099 mJy		2nd_selfcal: 0.096 mJy		3rd_selfcal: 0.089 mJy

#peak:
#noselfcal: 89.995 mJy		1st_selfcal: 96.229 mJy	2nd_selfcal: 96.444 mJy	3rd_selfcal: 97.320 mJy

    
##################################################### Stokes QUV #####################################################   
tclean(vis= FontUV + '.CO32.Slfc3.ms',
    imagename= FontUV + '.CO32.3.StokesQ.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.CO32.2.mask',
    niter= 0,
    threshold= '0.146mJy',
    interactive= False,
    savemodel= 'modelcolumn')

tclean(vis= FontUV + '.CO32.Slfc3.ms',
    imagename= FontUV + '.CO32.3.StokesU.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.CO32.2.mask',
    niter= 0,
    threshold= '0.146mJy',
    interactive= False,
    savemodel= 'modelcolumn')

tclean(vis= FontUV + '.CO32.Slfc3.ms',
    imagename= FontUV + '.CO32.3.StokesV.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.CO32.2.mask',
    niter= 0,
    threshold= '0.146mJy',
    interactive= False,
    savemodel= 'modelcolumn')


# rms_StokesQ: 0.076 mJy		# rms_StokesU: 0.079 mJy		# rms_StokesV: 0.078 mJy


tclean(vis= FontUV + '.CO32.Slfc3.ms',
    imagename= FontUV + '.CO32.3.StokesQ',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.CO32.2.mask',
    niter= 1000000,
    threshold= '0.152mJy',
    interactive= False,
    savemodel= 'modelcolumn')

tclean(vis= FontUV + '.CO32.Slfc3.ms',
    imagename= FontUV + '.CO32.3.StokesU',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.CO32.2.mask',
    niter= 1000000,
    threshold= '0.158mJy',
    interactive= False,
    savemodel= 'modelcolumn')

tclean(vis= FontUV + '.CO32.Slfc3.ms',
    imagename= FontUV + '.CO32.3.StokesV',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.CO32.2.mask',
    niter= 1000000,
    threshold= '0.156mJy',
    interactive= False,
    savemodel= 'modelcolumn')

# rms_StokesQ: 0.075 mJy		# rms_StokesU: 0.079 mJy		# rms_StokesV: 0.077 mJy

    
#################################################################################################################################
########################################## apply selfcal solution to the original data ##########################################
#################################################################################################################################
FontUV='HOPS-12W'

split(vis='HOPS-12W.ms',
    field='0',
    spw='0,1,2,3',
    outputvis=FontUV+'_noflagging.ms',
    datacolumn='data')
     
     
applycal(vis=FontUV+'_noflagging.ms',
    gaintable= [FontUV+'_flagging.CO32.slfcal.1', FontUV+'_flagging.CO32.slfcal.2', FontUV+'_flagging.CO32.slfcal.3'],
    calwt=False,
    applymode='calonly',
    spwmap=[0,1,2,3],
    flagbackup=False)
    
    
split(vis=FontUV+'_noflagging.ms',
    outputvis=FontUV+'_noflagging.selfcal.ms',
    datacolumn='corrected')


##################################################### Stokes IQUV without any flagging ######################################################
FontUV='HOPS-12W'

tclean(vis=FontUV+'_noflagging.selfcal.ms',
    imagename=FontUV+'_noflagging.selfcal.StokesI.final.mfs',
    imsize=512,
    cell=['0.1arcsec'],
    field='0',
    spw='0,1,2,3',
    specmode='mfs',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.178mJy',  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

tclean(vis=FontUV+'_noflagging.selfcal.ms',
    imagename=FontUV+'_noflagging.selfcal.StokesQ.final.mfs',
    imsize=512,
    cell=['0.1arcsec'],
    field='0',
    spw='0,1,2,3',
    specmode='mfs',
    stokes='Q',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.15mJy',  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

tclean(vis=FontUV+'_noflagging.selfcal.ms',
    imagename=FontUV+'_noflagging.selfcal.StokesU.final.mfs',
    imsize=512,
    cell=['0.1arcsec'],
    field='0',
    spw='0,1,2,3',
    specmode='mfs',
    stokes='U',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.158mJy',  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

tclean(vis=FontUV+'_noflagging.selfcal.ms',
    imagename=FontUV+'_noflagging.selfcal.StokesV.final.mfs',
    imsize=512,
    cell=['0.1arcsec'],
    field='0',
    spw='0,1,2,3',
    specmode='mfs',
    stokes='V',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.154mJy',  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)


#################################################### POLI, POLA and Pfrac without flagging #####################################################
FontUV='HOPS-12W'

immath(outfile=FontUV+'_noflagging.POLI',
    mode='poli',
    imagename=[FontUV+'_noflagging.selfcal.StokesQ.final.mfs.image', FontUV+'_noflagging.selfcal.StokesU.final.mfs.image'],
    sigma='0.0mJy/beam')

# rms_POLI: 0.106mJy

# 'HOPS-12W_noflagging.POLA'['HOPS-12W_noflagging.POLI'>0.000318]

immath(outfile=FontUV+'_noflagging.POLA',
    mode='pola',
    imagename=[FontUV+'_noflagging.selfcal.StokesQ.final.mfs.image', FontUV+'_noflagging.selfcal.StokesU.final.mfs.image'],
    sigma='0.318mJy/beam')

immath(outfile=FontUV+'_noflagging.RATIO',
    mode='evalexpr', 
    imagename=[FontUV+'_noflagging.selfcal.StokesI.final.mfs.image', FontUV+'_noflagging.selfcal.StokesQ.final.mfs.image',FontUV+'_noflagging.selfcal.StokesU.final.mfs.image'],
    expr='sqrt((IM1^2+IM2^2)/IM0[IM0>5e-3]^2)')






######################################################### dirty cube images ##########################################################
FontUV='HOPS-12W_flagging'

os.system('cp -r HOPS-12W_noflagging.selfcal.ms HOPS-12W_flagging.selfcal.ms')

tclean(vis=FontUV+'.selfcal.ms',     
    imagename=FontUV+'.selfcal.spw0.dirty',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='0',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.18mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

tclean(vis=FontUV+'.selfcal.ms',     
    imagename=FontUV+'.selfcal.spw1.dirty',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='1',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.18mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)
    
tclean(vis=FontUV+'.selfcal.ms',     
    imagename=FontUV+'.selfcal.spw2.dirty',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='2',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.18mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)
    
tclean(vis=FontUV+'.selfcal.ms',     
    imagename=FontUV+'.selfcal.spw3.dirty',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='3',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.18mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)
    
    
######################################################### flagging bright lines for spw=1,2,3 ##########################################################
FontUV='HOPS-12W_flagging'

flagdata(vis=FontUV+'.selfcal.ms',
    spw='0:736~1107, 0:1409~1421, 1:1839~1845, 1:1903~1908, 2:364~369, 3:0~2, 3:52~54, 3:217~220, 3:293~298, 3:493~500, 3:932~934, 3:1807~1813, 3:1918~1919',
    flagbackup=False)

    
######################################################### dirty images for checking flagging ##########################################################
FontUV='HOPS-12W_flagging'

tclean(vis=FontUV+'.selfcal.ms',     
    imagename=FontUV+'.selfcal.spw0.dirty.check',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='0',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.18mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

tclean(vis=FontUV+'.selfcal.ms',     
    imagename=FontUV+'.selfcal.spw1.dirty.check',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='1',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.18mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)
    
tclean(vis=FontUV+'.selfcal.ms',     
    imagename=FontUV+'.selfcal.spw2.dirty.check',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='2',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.18mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)
    
tclean(vis=FontUV+'.selfcal.ms',     
    imagename=FontUV+'.selfcal.spw3.dirty.check',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='3',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.18mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)


######################################################### POLI POLA and PFRAC after flagging ##########################################################
#########################################################             spw=0,1,2,3            ##########################################################
FontUV='HOPS-12W_flagging'

tclean(vis=FontUV+'.selfcal.ms',
    imagename=FontUV+'.selfcal.allspws.StokesI.final.mfs',
    imsize=512,
    cell=['0.1arcsec'],
    field='0',
    spw='0,1,2,3',
    specmode='mfs',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.178mJy',  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

tclean(vis=FontUV+'.selfcal.ms',
    imagename=FontUV+'.selfcal.allspws.StokesQ.final.mfs',
    imsize=512,
    cell=['0.1arcsec'],
    field='0',
    spw='0,1,2,3',
    specmode='mfs',
    stokes='Q',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.15mJy',  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

tclean(vis=FontUV+'.selfcal.ms',
    imagename=FontUV+'.selfcal.allspws.StokesU.final.mfs',
    imsize=512,
    cell=['0.1arcsec'],
    field='0',
    spw='0,1,2,3',
    specmode='mfs',
    stokes='U',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.158mJy',  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)
    
tclean(vis=FontUV+'.selfcal.ms',
    imagename=FontUV+'.selfcal.allspws.StokesV.final.mfs',
    imsize=512,
    cell=['0.1arcsec'],
    field='0',
    spw='0,1,2,3',
    specmode='mfs',
    stokes='V',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.154mJy',  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

immath(outfile=FontUV+'.POLI',
    mode='poli',
    imagename=[FontUV+'.selfcal.allspws.StokesQ.final.mfs.image', FontUV+'.selfcal.allspws.StokesU.final.mfs.image'],
    sigma='0.0mJy/beam')

# rms_POLI: 0.108 mJy

# 'HOPS-12W_flagging.POLA'['HOPS-12W_flagging.POLI'>0.000324]

immath(outfile=FontUV+'.POLA',
    mode='pola',
    imagename=[FontUV+'.selfcal.allspws.StokesQ.final.mfs.image', FontUV+'.selfcal.allspws.StokesU.final.mfs.image'],
    sigma='0.324mJy/beam')

immath(outfile=FontUV+'.RATIO',
    mode='evalexpr',
    imagename=[FontUV+'.selfcal.allspws.StokesI.final.mfs.image', FontUV+'.selfcal.allspws.StokesQ.final.mfs.image', FontUV+'.selfcal.allspws.StokesU.final.mfs.image'],
    expr='sqrt((IM1^2+IM2^2)/IM0[IM0>5e-3]^2)')


    


