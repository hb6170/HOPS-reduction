FontUV='HOPS-11_cont_avg'

listobs(vis='HOPS-11.ms', listfile='HOPS-11.listobs.txt', verbose=True)

split(vis='HOPS-11.ms',
    spw='1,2,3',
    outputvis=FontUV+'.ms',
    width=[240,240,240],
    datacolumn='data')

tclean(vis=FontUV+'.ms',
    imagename=FontUV+'.StokesI_noselfcal.tclean',
    spw='0,1,2',
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
    pbcor=False,
    niter=1000000,
    interactive=True,
    savemodel='modelcolumn')
    
    
#################################################### 1st selfcal #####################################################
FontUV='HOPS-11_cont_avg'

gaincal(vis=FontUV+'.ms',
    caltable=FontUV+'.slfcal.1',
    refant='DA43',
    spw='0,1,2',
    gaintype='T',
    calmode='p',
    solint='600s')

plotcal(caltable=FontUV+'.slfcal.1',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=True,
    figfile='Gain_'+FontUV+'_slfcal1.png')
    
applycal(vis=FontUV+'.ms',
    gaintable=FontUV+'.slfcal.1',
    calwt=False,
    applymode='calonly',
    spwmap=[0,1,2],
    flagbackup=False)

split(vis=FontUV+'.ms',
    outputvis=FontUV+'.Slfc1.ms',
    datacolumn='corrected')

tclean(vis= FontUV + '.Slfc1.ms',
    imagename= FontUV + '.1',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.StokesI_noselfcal.tclean.mask',
    niter= 1000000,
    threshold= '0.0mJy',
    interactive= True,
    savemodel= 'modelcolumn')


#################################################### 2nd selfcal #####################################################
FontUV='HOPS-11_cont_avg'

gaincal(vis=FontUV+'.Slfc1.ms',
    caltable=FontUV+'.slfcal.2',
    refant='DA43',
    spw='0,1,2',
    gaintype='T',
    calmode='p',
    solint='30s')

plotcal(caltable=FontUV+'.slfcal.2',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=True,
    figfile='Gain_'+FontUV+'_slfcal2.png')
    
applycal(vis=FontUV+'.Slfc1.ms',
    gaintable=FontUV+'.slfcal.2',
    calwt=False,
    applymode='calonly',
    spwmap=[0,1,2],
    flagbackup=False)

split(vis=FontUV+'.Slfc1.ms',
    outputvis=FontUV+'.Slfc2.ms',
    datacolumn='corrected')

tclean(vis= FontUV + '.Slfc2.ms',
    imagename= FontUV + '.2',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.1.mask',
    niter= 1000000,
    threshold= '0.0mJy',
    interactive= True,
    savemodel= 'modelcolumn')
    
    
    
#################################################### 3rd selfcal #####################################################
FontUV='HOPS-11_cont_avg'

gaincal(vis=FontUV+'.Slfc2.ms',
    caltable=FontUV+'.slfcal.3',
    refant='DA43',
    spw='0,1,2',
    gaintype='T',
    calmode='p',
    solint='10s')

plotcal(caltable=FontUV+'.slfcal.3',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=True,
    figfile='Gain_'+FontUV+'_slfcal3.png')
    
applycal(vis=FontUV+'.Slfc2.ms',
    gaintable=FontUV+'.slfcal.3',
    calwt=False,
    applymode='calonly',
    spwmap=[0,1,2],
    flagbackup=False)

split(vis=FontUV+'.Slfc2.ms',
    outputvis=FontUV+'.Slfc3.ms',
    datacolumn='corrected')

tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.2.mask',
    niter= 1000000,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')


# peak: 
# noselfcal: 224.976 mJy,	1st selfcal: 237.045 mJy,	2nd_selfcal: 238.055 mJy,	3rd_selcal: 239.485 mJy

# rms:
# noselfcal: 0.384 mJy,	1st selfcal: 0.101 mJy,	2nd_selfcal: 0.094 mJy,	3rd_selcal: 0.088 mJy
    

#################################################### Stokes QUV #####################################################    
FontUV='HOPS-11_cont_avg'

tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesQ.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 0,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')
    
tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesU.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 0,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')
    
tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesV.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 0,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')

# rms of dirty StokesQUV:
# rms_StokesQ: 0.063		rms_StokesU: 0.062		rms_StokesQ: 0.062



tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesQ',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 1000000,
    threshold= '0.126mJy',
    interactive= False,
    savemodel= 'modelcolumn')
    
tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesU',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 1000000,
    threshold= '0.124mJy',
    interactive= False,
    savemodel= 'modelcolumn')
    
tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesV',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 1000000,
    threshold= '0.124mJy',
    interactive= False,
    savemodel= 'modelcolumn')


# rms of 3rd_selfcal StokesQUV:
# rms_StokesQ: 0.063		rms_StokesU: 0.062		rms_StokesQ: 0.062


#################################################### POLI POLA RATIO #####################################################  
FontUV='HOPS-11_cont_avg'

immath(outfile=FontUV+'.POLI',
    mode='poli',
    imagename=[FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    sigma='0.0mJy/beam')
    
# POLI_rms: 0.089 mJy

# 'HOPS-11_cont_avg.POLA'['HOPS-11_cont_avg.POLI'>0.000267]

immath(outfile=FontUV+'.POLA',
    mode='pola',
    imagename=[FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    sigma='0.267mJy/beam')

immath(outfile=FontUV+'.RATIO',
    mode='evalexpr',
    imagename=[FontUV+'.3.image', FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    expr='sqrt((IM1^2+IM2^2)/IM0[IM0>5e-3]^2)')






#################################################### uvcontsub #####################################################  
FontUV='HOPS-11_cont_avg'

split(vis='HOPS-11.ms',
    field='0',
    spw='0',
    outputvis= FontUV + '_CO32.ms',
    datacolumn='data')
    
applycal(vis = FontUV+'_CO32.ms',
    gaintable= [FontUV+'.slfcal.1', FontUV+'.slfcal.2', FontUV+'.slfcal.3'],
    calwt= False,
    applymode= 'calonly',
    spwmap=[0],
    flagbackup= False)
    
split(vis = FontUV + '_CO32.ms',
    outputvis= FontUV + '_CO32.selfcal.ms',
    datacolumn= 'corrected')

delmod(vis= FontUV + '_CO32.selfcal.ms')
    
tclean(vis=FontUV+'_CO32.selfcal.ms',     
    imagename=FontUV+'_CO32.selfcal.dirty',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='0',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.184mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

uvcontsub(vis= FontUV + '_CO32.selfcal.ms',
    spw= '0',             # spw to do continuum subtraction on
    fitspw= '0:1~6, 0:12~16, 0:32~47, 0:58~61, 0:69~88, 0:95~168, 0:183~189, 0:220~224, 0:253~255, 0:265~295, 0:301~312, 0:317~322, 0:341~351, 0:482~484, 0:494~508, 0:565~572, 0:620~624, 0:632~640, 0:694~700, 0:840~850, 0:1239~1242, 0:1251~1255, 0:1265~1267, 0:1275~1276, 0:1341~1355, 0:1374~1376, 0:1386~1389, 0:1398~1340, 0:1505~1507, 0:1520~1523, 0:1539~1541, 0:1552~1564, 0:1567~1585, 0:1594~1600, 0:1604~1613, 0:1616~1623, 0:1626~1660, 0:1861~1864, 0:1904~1906',
    excludechans= False,          # fit the region in fitspw
    solint= 'int',             # no time averaging, do a fit for each integration and let the noise fits average out in the image
    fitorder= 1,            # polynomial order for the fits of the continuum
    want_cont= False)        # create vis+'.contsub' to hold the continuum estimate

delmod(vis= FontUV + '_CO32.selfcal.ms.contsub')

tclean(vis= FontUV + '_CO32.selfcal.ms.contsub',
    imagename= FontUV + '_CO32.selfcal.ms.contsub.dirty',
    imsize= 256,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0',
    specmode= 'cube',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    threshold= '0.008mJy',     # the same as 3rd selfcal, 2sigma
    pblimit= -1,
    niter= 0,
    usemask='auto-multithresh',
    negativethreshold=0.0,    # the 75th percentile of baselines >300m
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)

tclean(vis= FontUV + '_CO32.selfcal.ms.contsub',
    imagename= FontUV + '_CO32.selfcal.ms.contsub.final',
    imsize= 256,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0',
    specmode= 'cube',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    threshold= '0.008mJy',     # the same as 3rd selfcal, 2sigma
    pblimit= -1,
    niter= 100000,
    usemask='auto-multithresh',
    negativethreshold=0.0,    # the 75th percentile of baselines >300m
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory


immoments(imagename= FontUV + '_CO32.selfcal.ms.contsub.final.image',
    moments=[0],      # integrated value of the spectrum
    axis= 'spectral',
    chans= '715~960',      # Channels to use. Default is to use all channels
    outfile= 'moments0_715-960.image')
    
   
immoments(imagename= FontUV + '_CO32.selfcal.ms.contsub.final.image',
    moments=[0],      # integrated value of the spectrum
    axis= 'spectral',
    chans= '982~1230',      # Channels to use. Default is to use all channels
    outfile= 'moments0_982-1230.image')
    
# 'HOPS-11_cont_avg.POLA'['HOPS-11_cont_avg.POLI'>0.000267]
