FontUV='HOPS-12E_flagging'

os.system('cp -r HOPS-12E.ms tmp.ms')

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
    spw='0:910~1050',
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
FontUV='HOPS-12E_flagging'

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
FontUV='HOPS-12E_flagging'

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
FontUV='HOPS-12E_flagging'

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
#noselfcal: 0.222 mJy		1st_selfcal: 0.093 mJy		2nd_selfcal: 0.090 mJy		3rd_selfcal: 0.082 mJy

#peak:
#noselfcal: 112.085 mJy	1st_selfcal: 117.949 mJy	2nd_selfcal: 118.076 mJy	3rd_selfcal: 119.084mJy

    
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


# rms_StokesQ: 0.073 mJy		# rms_StokesU: 0.069 mJy		# rms_StokesV: 0.071 mJy


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
    threshold= '0.146mJy',
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
    threshold= '0.138mJy',
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
    threshold= '0.142mJy',
    interactive= False,
    savemodel= 'modelcolumn')

# rms_StokesQ: 0.073 mJy		# rms_StokesU: 0.069 mJy		# rms_StokesV: 0.071 mJy

    
#################################################################################################################################
########################################## apply selfcal solution to the original data ##########################################
#################################################################################################################################
FontUV='HOPS-12E'

split(vis='HOPS-12E.ms',
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
FontUV='HOPS-12E'

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
    threshold='0.164mJy',  # 2sigma rms of 3rd_selfcal
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
    threshold='0.146mJy',  # 2sigma rms of 3rd_selfcal
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
    threshold='0.138mJy',  # 2sigma rms of 3rd_selfcal
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
    threshold='0.142mJy',  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)


#################################################### POLI, POLA and Pfrac without flagging #####################################################
FontUV='HOPS-12E'

immath(outfile=FontUV+'_noflagging.POLI',
    mode='poli',
    imagename=[FontUV+'_noflagging.selfcal.StokesQ.final.mfs.image', FontUV+'_noflagging.selfcal.StokesU.final.mfs.image'],
    sigma='0.0mJy/beam')

# rms_POLI: 0.101mJy

# 'HOPS-12E_noflagging.POLA'['HOPS-12E_noflagging.POLI'>0.000303]

immath(outfile=FontUV+'_noflagging.POLA',
    mode='pola',
    imagename=[FontUV+'_noflagging.selfcal.StokesQ.final.mfs.image', FontUV+'_noflagging.selfcal.StokesU.final.mfs.image'],
    sigma='0.303mJy/beam')

immath(outfile=FontUV+'_noflagging.RATIO',
    mode='evalexpr', 
    imagename=[FontUV+'_noflagging.selfcal.StokesI.final.mfs.image', FontUV+'_noflagging.selfcal.StokesQ.final.mfs.image',FontUV+'_noflagging.selfcal.StokesU.final.mfs.image'],
    expr='sqrt((IM1^2+IM2^2)/IM0[IM0>5e-3]^2)')






######################################################### dirty cube images ##########################################################
FontUV='HOPS-12E_flagging'

os.system('cp -r HOPS-12E_noflagging.selfcal.ms HOPS-12E_flagging.selfcal.ms')

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
FontUV='HOPS-12E_flagging'

flagdata(vis=FontUV+'.selfcal.ms',
    spw='0:701~705, 0:710~714, 0:733~1105, 0:1407~1428, 0:1471~1487, 1:1839~1845, 1:1902~1907, 2:1918~1919, 3:357~363',
    flagbackup=False)

    
######################################################### dirty images for checking flagging ##########################################################
FontUV='HOPS-12E_flagging'

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
FontUV='HOPS-12E_flagging'

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
    threshold='0.164mJy',  # 2sigma rms of 3rd_selfcal
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
    threshold='0.146mJy',  # 2sigma rms of 3rd_selfcal
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
    threshold='0.138mJy',  # 2sigma rms of 3rd_selfcal
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
    threshold='0.142mJy',  # 2sigma rms of 3rd_selfcal
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

# rms_POLI: 0.101 mJy

# 'HOPS-12E_flagging.POLA'['HOPS-12E_flagging.POLI'>0.000303]

immath(outfile=FontUV+'.POLA',
    mode='pola',
    imagename=[FontUV+'.selfcal.allspws.StokesQ.final.mfs.image', FontUV+'.selfcal.allspws.StokesU.final.mfs.image'],
    sigma='0.303mJy/beam')

immath(outfile=FontUV+'.RATIO',
    mode='evalexpr',
    imagename=[FontUV+'.selfcal.allspws.StokesI.final.mfs.image', FontUV+'.selfcal.allspws.StokesQ.final.mfs.image', FontUV+'.selfcal.allspws.StokesU.final.mfs.image'],
    expr='sqrt((IM1^2+IM2^2)/IM0[IM0>5e-3]^2)')



immath(outfile=FontUV+'.subtraction.POLA',
    mode='evalexpr',
    imagename=['HOPS-12E_cont_avg.flagging.POLA','HOPS-12E_cont_avg.POLA'],
    expr='iif(iif((IM0+IM1>IM0&&IM0+IM1>IM1) || (IM0+IM1<IM0&&IM0+IM1<IM1),IM0-IM1,IM0+IM1)>-20 && iif((IM0+IM1>IM0&&IM0+IM1>IM1) || (IM0+IM1<IM0&&IM0+IM1<IM1),IM0-IM1,IM0+IM1)<20, iif((IM0+IM1>IM0&&IM0+IM1>IM1) || (IM0+IM1<IM0&&IM0+IM1<IM1),IM0-IM1,IM0+IM1), 0)')
    
immath(outfile=FontUV+'.subtraction.POLI',
    mode='evalexpr',
    imagename=['HOPS-12E_cont_avg.flagging.POLI','HOPS-12E_cont_avg.POLI'],
    expr='IM0-IM1')
    


