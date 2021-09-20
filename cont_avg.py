FontUV='HOPS-169_cont_avg'

listobs(vis='HOPS-169.ms', listfile='HOPS-169.listobs.txt', verbose=True)

split(vis='HOPS-169.ms',
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
FontUV='HOPS-169_cont_avg'

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
FontUV='HOPS-169_cont_avg'

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
FontUV='HOPS-169_cont_avg'

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

tclean(vis= FontUV + '.Slfc3.ms',	# ['...12E', '...12W']
    imagename= FontUV + '.3',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',	# 'mosaic'
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,	# 0.1
    mask= FontUV + '.2.mask',
    niter= 1000000,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')


# peak: 
# noselfcal: 202.045 mJy,	1st selfcal: 209.176 mJy,	2nd_selfcal: 209.152 mJy,	3rd_selcal: 210.312 mJy

# rms:
# noselfcal: 0.321 mJy,	1st selfcal: 0.106 mJy,	2nd_selfcal: 0.101 mJy,	3rd_selcal: 0.091 mJy
    

#################################################### Stokes QUV #####################################################    
FontUV='HOPS-169_cont_avg'

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
# rms_StokesQ: 0.072		rms_StokesU: 0.074		rms_StokesQ: 0.074



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
    threshold= '0.144mJy',
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
    threshold= '0.148mJy',
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
    threshold= '0.148mJy',
    interactive= False,
    savemodel= 'modelcolumn')


# rms of 3rd_selfcal StokesQUV:
# rms_StokesQ: 0.071		rms_StokesU: 0.073		rms_StokesQ: 0.074


#################################################### POLI POLA RATIO #####################################################  
FontUV='HOPS-169_cont_avg'

immath(outfile=FontUV+'.POLI',
    mode='poli',
    imagename=[FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    sigma='0.0mJy/beam')
    
# POLI_rms: 0.102 mJy

# 'HOPS-169_cont_avg.POLA'['HOPS-169_cont_avg.POLI'>0.000306]

immath(outfile=FontUV+'.POLA',
    mode='pola',
    imagename=[FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    sigma='0.306mJy/beam')

immath(outfile=FontUV+'.RATIO',
    mode='evalexpr',
    imagename=[FontUV+'.3.image', FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    expr='sqrt((IM1^2+IM2^2)/IM0[IM0>5e-3]^2)')






#################################################### uvcontsub #####################################################  
FontUV='HOPS-169_cont_avg'

split(vis='HOPS-169.ms',
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
    fitspw= '0:15~20, 0:24~27, 0:66~69, 0:82~86, 0:93~98, 0:107~110, 0:177~178, 0:273~276, 0:295~297, 0:304~308, 0:332~333, 0:355~356, 0:360~361, 0:449~450, 0:475~476, 0:561~562, 0:602~605, 0:609~610, 0:617~620, 0:634~636, 0:686~687, 0:707~709, 0:719~720, 0:724~725, 0:739~740, 0:755~756, 0:1159~1160, 0:1174~1175, 0:1213~1214, 0:1243~1244, 0:1253~1254, 0:1289~1290, 0:1337~1340, 0:1345~1348, 0:1354~1365, 0:1369~1371, 0:1374~1376, 0:1386~1388, 0:1578~1580, 0:1599~1601, 0:1612~1617, 0:1653~1657, 0:1665~1667, 0:1846~1847, 0:1860~1864, 0:1899~1907, 0:1911~1915',
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
    chans= '830~950',      # Channels to use. Default is to use all channels
    outfile= 'moments0_830-950.image')
    
   
immoments(imagename= FontUV + '_CO32.selfcal.ms.contsub.final.image',
    moments=[0],      # integrated value of the spectrum
    axis= 'spectral',
    chans= '1003~1165',      # Channels to use. Default is to use all channels
    outfile= 'moments0_1003-1165.image')
    
# 'HOPS-169_cont_avg.POLA'['HOPS-169_cont_avg.POLI'>0.000306]






